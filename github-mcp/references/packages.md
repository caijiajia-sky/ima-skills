# GitHub MCP - Packages

## 概述

本Skill提供GitHub API的 **Packages** 相关操作能力，包含 **26** 个工具。

## 工具列表

### 1. github_packages_list_docker_migration_conflicting_packages_for_organization

**描述**: Get list of conflicting packages during Docker migration for organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 2. github_packages_list_packages_for_organization

**描述**: List packages for an organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 3. github_packages_get_package_for_organization

**描述**: Get a package for an organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 4. github_packages_delete_package_for_org

**描述**: Delete a package for an organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 5. github_packages_restore_package_for_org

**描述**: Restore a package for an organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 6. github_packages_get_all_package_versions_for_package_owned_by_org

**描述**: List package versions for a package owned by an organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 7. github_packages_get_package_version_for_organization

**描述**: Get a package version for an organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 8. github_packages_delete_package_version_for_org

**描述**: Delete package version for an organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 9. github_packages_restore_package_version_for_org

**描述**: Restore package version for an organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 10. github_packages_list_docker_migration_conflicting_packages_for_authenticated_user

**描述**: List packages for the authenticated user's namespace

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| package_type | 是 | The type of supported package. Packages in GitHub's Gradle registry have the type `maven`. Docker images pushed to GitHub's Container registry (`ghcr.io`) have the type `container`. You can use the type `docker` to find images that were pushed to GitHub's Docker registry (`docker.pkg.github.com`), even if these have now been migrated to the Container registry. |

---

### 11. github_packages_get_package_for_authenticated_user

**描述**: Get a package for the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| package_type | 是 | package_type |

---

### 12. github_packages_delete_package_for_authenticated_user

**描述**: Delete a package for the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| package_type | 是 | package_type |

---

### 13. github_packages_restore_package_for_authenticated_user

**描述**: Restore a package for the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| package_type | 是 | package_type |

---

### 14. github_packages_get_all_package_versions_for_package_owned_by_authenticated_user

**描述**: List package versions for a package owned by the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| package_type | 是 | package_type |

---

### 15. github_packages_get_package_version_for_authenticated_user

**描述**: Get a package version for the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| package_type | 是 | package_type |

---

### 16. github_packages_delete_package_version_for_authenticated_user

**描述**: Delete a package version for the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| package_type | 是 | package_type |

---

### 17. github_packages_restore_package_version_for_authenticated_user

**描述**: Restore a package version for the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| package_type | 是 | package_type |

---

### 18. github_packages_list_docker_migration_conflicting_packages_for_user

**描述**: Get list of conflicting packages during Docker migration for user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| username | 是 | username |

---

### 19. github_packages_list_packages_for_user

**描述**: List packages for a user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| username | 是 | username |

---

### 20. github_packages_get_package_for_user

**描述**: Get a package for a user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| username | 是 | username |

---

### 21. github_packages_delete_package_for_user

**描述**: Delete a package for a user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| username | 是 | username |

---

### 22. github_packages_restore_package_for_user

**描述**: Restore a package for a user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| username | 是 | username |

---

### 23. github_packages_get_all_package_versions_for_package_owned_by_user

**描述**: List package versions for a package owned by a user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| username | 是 | username |

---

### 24. github_packages_get_package_version_for_user

**描述**: Get a package version for a user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| username | 是 | username |

---

### 25. github_packages_delete_package_version_for_user

**描述**: Delete package version for a user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| username | 是 | username |

---

### 26. github_packages_restore_package_version_for_user

**描述**: Restore package version for a user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| username | 是 | username |

---

