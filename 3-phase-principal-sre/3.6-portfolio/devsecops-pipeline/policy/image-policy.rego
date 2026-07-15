package devsecops

# Image Security Policy - OPA Rules

# Deny: Image runs as root
deny[msg] {
  input.image.user == "root"
  msg := "Image must not run as root user"
}

# Deny: Privileged container
deny[msg] {
  input.image.securityContext.privileged == true
  msg := "Privileged containers are not allowed"
}

# Deny: Allow privilege escalation
deny[msg] {
  input.image.securityContext.allowPrivilegeEscalation == true
  msg := "Privilege escalation must be disabled (allowPrivilegeEscalation: false)"
}

# Deny: Root filesystem is not read-only
deny[msg] {
  input.image.readOnlyRootFilesystem == false
  msg := "Root filesystem must be read-only"
}

# Deny: Image not pinned to digest
deny[msg] {
  not contains(input.image.imageRef, "@sha256:")
  msg := "Image must be pinned to specific digest (use @sha256:hash, not :tag)"
}

# Deny: Missing resource limits
deny[msg] {
  not input.image.resources.limits.cpu
  msg := "CPU resource limit must be defined"
}

# Deny: SYS_ADMIN capability not dropped
deny[msg] {
  not contains(input.image.securityContext.capabilities.drop, "SYS_ADMIN")
  msg := "CAP_SYS_ADMIN must be in capabilities.drop list"
}

# Warn: No memory limit
warn[msg] {
  not input.image.resources.limits.memory
  msg := "Memory resource limit is recommended"
}

# Warn: RunAsNonRoot not explicitly set
warn[msg] {
  input.image.securityContext.runAsNonRoot != true
  msg := "runAsNonRoot should be explicitly true"
}

# Helper function
contains(arr, val) {
  arr[_] == val
}
