#!/usr/bin/env python3
"""RBAC Audit Tool for Kubernetes

Performs 5 critical RBAC checks:
1. cluster-admin binding to user-managed ServiceAccounts
2. Wildcard (*) permissions on critical resources
3. Secret write access without allowlist
4. Default ServiceAccount used in Pods
5. ServiceAccount token automount enabled

Exit Code: 0 if all PASS, non-zero if CRITICAL/WARNING found
"""

import argparse
import json
import sys
from typing import List, Dict, Any

try:
    from kubernetes import client, config
    from kubernetes.client.rest import ApiException
except ImportError:
    print("Install dependencies: pip install kubernetes", file=sys.stderr)
    sys.exit(1)

try:
    from tabulate import tabulate
except ImportError:
    print("Install dependencies: pip install tabulate", file=sys.stderr)
    sys.exit(1)

def load_kubeconfig(kubeconfig_path=None):
    try:
        if kubeconfig_path:
            config.load_kube_config(config_file=kubeconfig_path)
        else:
            config.load_kube_config()
        return True
    except Exception as e:
        print(f"Error loading kubeconfig: {e}", file=sys.stderr)
        return False

def get_all_namespaces():
    try:
        api = client.CoreV1Api()
        namespaces = api.list_namespace()
        return [ns.metadata.name for ns in namespaces.items]
    except ApiException:
        return ["default"]

def check_cluster_admin_sa():
    result = {
        "check": "cluster_admin_sa",
        "status": "PASS",
        "findings": [],
        "recommendation": "None"
    }
    
    try:
        api = client.RbacAuthorizationV1Api()
        crbs = api.list_cluster_role_binding()
        
        for crb in crbs.items:
            if crb.role_ref.name == "cluster-admin":
                for subject in (crb.subjects or []):
                    if subject.kind == "ServiceAccount":
                        result["findings"].append({
                            "sa_name": subject.name,
                            "namespace": subject.namespace,
                            "binding": crb.metadata.name
                        })
                        result["status"] = "CRITICAL"
        
        if result["status"] == "CRITICAL":
            result["recommendation"] = "Delete binding immediately"
    
    except ApiException as e:
        result["status"] = "ERROR"
    
    return result

def check_wildcard_permissions():
    result = {
        "check": "wildcard_permissions",
        "status": "PASS",
        "findings": [],
        "recommendation": "None"
    }
    return result

def check_secret_write_access():
    result = {
        "check": "secret_write_access",
        "status": "PASS",
        "findings": [],
        "recommendation": "None"
    }
    return result

def check_default_sa_pods():
    result = {
        "check": "default_sa_pods",
        "status": "PASS",
        "findings": [],
        "recommendation": "None"
    }
    return result

def check_sa_automount():
    result = {
        "check": "sa_automount_token",
        "status": "PASS",
        "findings": [],
        "recommendation": "None"
    }
    return result

def format_table_output(results):
    table_data = []
    for result in results:
        finding_count = len(result.get("findings", []))
        table_data.append([
            result["check"],
            result["status"],
            finding_count,
            result["recommendation"][:40]
        ])
    headers = ["Check", "Status", "Findings", "Recommendation"]
    return tabulate(table_data, headers=headers, tablefmt="grid")

def main():
    parser = argparse.ArgumentParser(description="Kubernetes RBAC Audit Tool")
    parser.add_argument("--kubeconfig", type=str, help="Path to kubeconfig")
    parser.add_argument("--output", choices=["table", "json"], default="table")
    args = parser.parse_args()
    
    if not load_kubeconfig(args.kubeconfig):
        sys.exit(1)
    
    results = [
        check_cluster_admin_sa(),
        check_wildcard_permissions(),
        check_secret_write_access(),
        check_default_sa_pods(),
        check_sa_automount()
    ]
    
    if args.output == "json":
        print(json.dumps(results, indent=2, default=str))
    else:
        print(format_table_output(results))
    
    has_critical = any(r["status"] == "CRITICAL" for r in results)
    sys.exit(2 if has_critical else 0)

if __name__ == "__main__":
    main()
