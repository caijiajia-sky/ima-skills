# GitHub MCP - Security Advisories

## 概述

本Skill提供GitHub API的 **Security Advisories** 相关操作能力，包含 **10** 个工具。

## 工具列表

### 1. github_security_advisories_list_global_advisories

**描述**: List global security advisories

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| ghsa_id | 否 | If specified, only advisories with this GHSA (GitHub Security Advisory) identifier will be returned. |

---

### 2. github_security_advisories_get_global_advisory

**描述**: Get a global security advisory

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| ghsa_id | 是 | ghsa_id |

---

### 3. github_security_advisories_list_org_repository_advisories

**描述**: List repository security advisories for an organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 4. github_security_advisories_list_repository_advisories

**描述**: List repository security advisories

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 5. github_security_advisories_create_repository_advisory

**描述**: Create a repository security advisory

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 6. github_security_advisories_create_private_vulnerability_report

**描述**: Privately report a security vulnerability

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 7. github_security_advisories_get_repository_advisory

**描述**: Get a repository security advisory

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 8. github_security_advisories_update_repository_advisory

**描述**: Update a repository security advisory

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 9. github_security_advisories_create_repository_advisory_cve_request

**描述**: Request a CVE for a repository security advisory

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 10. github_security_advisories_create_fork

**描述**: Create a temporary private fork

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

