# GitHub MCP - Code Scanning

## 概述

本Skill提供GitHub API的 **Code Scanning** 相关操作能力，包含 **21** 个工具。

## 工具列表

### 1. github_code_scanning_list_alerts_for_org

**描述**: List code scanning alerts for an organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 2. github_code_scanning_list_alerts_for_repo

**描述**: List code scanning alerts for a repository

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 3. github_code_scanning_get_alert

**描述**: Get a code scanning alert

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 4. github_code_scanning_update_alert

**描述**: Update a code scanning alert

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 5. github_code_scanning_get_autofix

**描述**: Get the status of an autofix for a code scanning alert

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 6. github_code_scanning_create_autofix

**描述**: Create an autofix for a code scanning alert

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 7. github_code_scanning_commit_autofix

**描述**: Commit an autofix for a code scanning alert

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 8. github_code_scanning_list_alert_instances

**描述**: List instances of a code scanning alert

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 9. github_code_scanning_list_recent_analyses

**描述**: List code scanning analyses for a repository

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 10. github_code_scanning_get_analysis

**描述**: Get a code scanning analysis for a repository

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 11. github_code_scanning_delete_analysis

**描述**: Delete a code scanning analysis from a repository

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 12. github_code_scanning_list_codeql_databases

**描述**: List CodeQL databases for a repository

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 13. github_code_scanning_get_codeql_database

**描述**: Get a CodeQL database for a repository

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 14. github_code_scanning_delete_codeql_database

**描述**: Delete a CodeQL database

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 15. github_code_scanning_create_variant_analysis

**描述**: Create a CodeQL variant analysis

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 16. github_code_scanning_get_variant_analysis

**描述**: Get the summary of a CodeQL variant analysis

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 17. github_code_scanning_get_variant_analysis_repo_task

**描述**: Get the analysis status of a repository in a CodeQL variant analysis

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 18. github_code_scanning_get_default_setup

**描述**: Get a code scanning default setup configuration

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 19. github_code_scanning_update_default_setup

**描述**: Update a code scanning default setup configuration

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 20. github_code_scanning_upload_sarif

**描述**: Upload an analysis as SARIF data

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 21. github_code_scanning_get_sarif

**描述**: Get information about a SARIF upload

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

