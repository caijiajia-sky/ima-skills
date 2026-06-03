# GitHub MCP - Codespaces

## 概述

本Skill提供GitHub API的 **Codespaces** 相关操作能力，包含 **47** 个工具。

## 工具列表

### 1. github_codespaces_list_in_organization

**描述**: List codespaces for the organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 2. github_codespaces_set_codespaces_access

**描述**: Manage access control for organization codespaces

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 3. github_codespaces_set_codespaces_access_users

**描述**: Add users to Codespaces access for an organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 4. github_codespaces_delete_codespaces_access_users

**描述**: Remove users from Codespaces access for an organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 5. github_codespaces_list_org_secrets

**描述**: List organization secrets

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 6. github_codespaces_get_org_public_key

**描述**: Get an organization public key

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 7. github_codespaces_get_org_secret

**描述**: Get an organization secret

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 8. github_codespaces_create_or_update_org_secret

**描述**: Create or update an organization secret

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 9. github_codespaces_delete_org_secret

**描述**: Delete an organization secret

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 10. github_codespaces_list_selected_repos_for_org_secret

**描述**: List selected repositories for an organization secret

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 11. github_codespaces_set_selected_repos_for_org_secret

**描述**: Set selected repositories for an organization secret

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 12. github_codespaces_add_selected_repo_to_org_secret

**描述**: Add selected repository to an organization secret

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 13. github_codespaces_remove_selected_repo_from_org_secret

**描述**: Remove selected repository from an organization secret

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 14. github_codespaces_get_codespaces_for_user_in_org

**描述**: List codespaces for a user in organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 15. github_codespaces_delete_from_organization

**描述**: Delete a codespace from the organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 16. github_codespaces_stop_in_organization

**描述**: Stop a codespace for an organization user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 17. github_codespaces_list_in_repository_for_authenticated_user

**描述**: List codespaces in a repository for the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 18. github_codespaces_create_with_repo_for_authenticated_user

**描述**: Create a codespace in a repository

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 19. github_codespaces_list_devcontainers_in_repository_for_authenticated_user

**描述**: List devcontainer configurations in a repository for the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 20. github_codespaces_repo_machines_for_authenticated_user

**描述**: List available machine types for a repository

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 21. github_codespaces_pre_flight_with_repo_for_authenticated_user

**描述**: Get default attributes for a codespace

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 22. github_codespaces_check_permissions_for_devcontainer

**描述**: Check if permissions defined by a devcontainer have been accepted by the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 23. github_codespaces_list_repo_secrets

**描述**: List repository secrets

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 24. github_codespaces_get_repo_public_key

**描述**: Get a repository public key

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 25. github_codespaces_get_repo_secret

**描述**: Get a repository secret

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 26. github_codespaces_create_or_update_repo_secret

**描述**: Create or update a repository secret

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 27. github_codespaces_delete_repo_secret

**描述**: Delete a repository secret

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 28. github_codespaces_create_with_pr_for_authenticated_user

**描述**: Create a codespace from a pull request

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 29. github_codespaces_list_for_authenticated_user

**描述**: List codespaces for the authenticated user


---

### 30. github_codespaces_create_for_authenticated_user

**描述**: Create a codespace for the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| body | 否 | Request body (JSON object) |

---

### 31. github_codespaces_list_secrets_for_authenticated_user

**描述**: List secrets for the authenticated user


---

### 32. github_codespaces_get_public_key_for_authenticated_user

**描述**: Get a secret for the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| secret_name | 是 | secret_name |

---

### 33. github_codespaces_create_or_update_secret_for_authenticated_user

**描述**: Create or update a secret for the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| secret_name | 是 | secret_name |

---

### 34. github_codespaces_delete_secret_for_authenticated_user

**描述**: Delete a secret for the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| secret_name | 是 | secret_name |

---

### 35. github_codespaces_list_repositories_for_secret_for_authenticated_user

**描述**: List selected repositories for a user secret

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| secret_name | 是 | secret_name |

---

### 36. github_codespaces_set_repositories_for_secret_for_authenticated_user

**描述**: Set selected repositories for a user secret

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| secret_name | 是 | secret_name |

---

### 37. github_codespaces_add_repository_for_secret_for_authenticated_user

**描述**: Add a selected repository to a user secret

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| secret_name | 是 | secret_name |

---

### 38. github_codespaces_remove_repository_for_secret_for_authenticated_user

**描述**: Remove a selected repository from a user secret

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| secret_name | 是 | secret_name |

---

### 39. github_codespaces_get_for_authenticated_user

**描述**: Get a codespace for the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| codespace_name | 是 | codespace_name |

---

### 40. github_codespaces_update_for_authenticated_user

**描述**: Update a codespace for the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| codespace_name | 是 | codespace_name |

---

### 41. github_codespaces_delete_for_authenticated_user

**描述**: Delete a codespace for the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| codespace_name | 是 | codespace_name |

---

### 42. github_codespaces_export_for_authenticated_user

**描述**: Export a codespace for the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| codespace_name | 是 | codespace_name |

---

### 43. github_codespaces_get_export_details_for_authenticated_user

**描述**: Get details about a codespace export

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| codespace_name | 是 | codespace_name |

---

### 44. github_codespaces_codespace_machines_for_authenticated_user

**描述**: List machine types for a codespace

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| codespace_name | 是 | codespace_name |

---

### 45. github_codespaces_publish_for_authenticated_user

**描述**: Create a repository from an unpublished codespace

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| codespace_name | 是 | codespace_name |

---

### 46. github_codespaces_start_for_authenticated_user

**描述**: Start a codespace for the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| codespace_name | 是 | codespace_name |

---

### 47. github_codespaces_stop_for_authenticated_user

**描述**: Stop a codespace for the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| codespace_name | 是 | codespace_name |

---

