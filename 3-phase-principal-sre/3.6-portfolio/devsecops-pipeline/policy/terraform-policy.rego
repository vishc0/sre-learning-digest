package terraform

# Terraform Security Compliance Policies

# Rule 1: S3 bucket must have versioning enabled
deny[msg] {
  resource := input.resource.aws_s3_bucket[name]
  resource.versioning[0].enabled != true
  msg := sprintf("S3 bucket '%s' must have versioning enabled", [name])
}

# Rule 2: S3 bucket must have encryption enabled
deny[msg] {
  resource := input.resource.aws_s3_bucket[name]
  not resource.server_side_encryption_configuration
  msg := sprintf("S3 bucket '%s' must have server-side encryption", [name])
}

# Rule 3: IAM role must have assume role policy with conditions
deny[msg] {
  resource := input.resource.aws_iam_role[name]
  not resource.assume_role_policy
  msg := sprintf("IAM role '%s' must have assume_role_policy defined", [name])
}

# Rule 4: Security group must deny by default
deny[msg] {
  resource := input.resource.aws_security_group[name]
  egress := resource.egress
  count(egress) > 0
  egress[_].cidr_blocks[_] == "0.0.0.0/0"
  msg := sprintf("Security group '%s' allows unrestricted egress - apply principle of least privilege", [name])
}

# Rule 5: RDS instance must have encryption enabled
deny[msg] {
  resource := input.resource.aws_db_instance[name]
  resource.storage_encrypted != true
  msg := sprintf("RDS instance '%s' must have storage_encrypted = true", [name])
}

# Rule 6: EKS cluster must have logging enabled
deny[msg] {
  resource := input.resource.aws_eks_cluster[name]
  not resource.enabled_cluster_log_types
  msg := sprintf("EKS cluster '%s' must have cluster logging enabled", [name])
}

# Rule 7: VPC Flow Logs must be enabled
deny[msg] {
  resource := input.resource.aws_vpc[name]
  not resource.flow_logs_enabled
  msg := sprintf("VPC '%s' should have Flow Logs enabled for security monitoring", [name])
}
