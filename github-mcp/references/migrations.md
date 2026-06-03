# GitHub MCP - Migrations

## 概述

本Skill提供GitHub API的 **Migrations** 相关操作能力，包含 **22** 个工具。

## 工具列表

### 1. github_migrations_list_for_org

**描述**: List organization migrations

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 2. github_migrations_start_for_org

**描述**: Start an organization migration

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 3. github_migrations_get_status_for_org

**描述**: Get an organization migration status

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 4. github_migrations_download_archive_for_org

**描述**: Download an organization migration archive

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 5. github_migrations_delete_archive_for_org

**描述**: Delete an organization migration archive

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 6. github_migrations_unlock_repo_for_org

**描述**: Unlock an organization repository

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 7. github_migrations_list_repos_for_org

**描述**: List repositories in an organization migration

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 8. github_migrations_get_import_status

**描述**: Get an import status

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 9. github_migrations_start_import

**描述**: Start an import

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 10. github_migrations_update_import

**描述**: Update an import

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 11. github_migrations_cancel_import

**描述**: Cancel an import

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 12. github_migrations_get_commit_authors

**描述**: Get commit authors

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 13. github_migrations_map_commit_author

**描述**: Map a commit author

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 14. github_migrations_get_large_files

**描述**: Get large files

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 15. github_migrations_set_lfs_preference

**描述**: Update Git LFS preference

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 16. github_migrations_list_for_authenticated_user

**描述**: List user migrations


---

### 17. github_migrations_start_for_authenticated_user

**描述**: Start a user migration

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| body | 否 | Request body (JSON object) |

---

### 18. github_migrations_get_status_for_authenticated_user

**描述**: Get a user migration status

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| migration_id | 是 | migration_id |

---

### 19. github_migrations_get_archive_for_authenticated_user

**描述**: Download a user migration archive

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| migration_id | 是 | migration_id |

---

### 20. github_migrations_delete_archive_for_authenticated_user

**描述**: Delete a user migration archive

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| migration_id | 是 | migration_id |

---

### 21. github_migrations_unlock_repo_for_authenticated_user

**描述**: Unlock a user repository

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| migration_id | 是 | migration_id |

---

### 22. github_migrations_list_repos_for_authenticated_user

**描述**: List repositories for a user migration

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| migration_id | 是 | migration_id |

---

