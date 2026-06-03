# GitHub MCP - Gists

## 概述

本Skill提供GitHub API的 **Gists** 相关操作能力，包含 **20** 个工具。

## 工具列表

### 1. github_gists_list

**描述**: List gists for the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| since | 否 | Only show results that were last updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. |

---

### 2. github_gists_create

**描述**: Create a gist

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| body | 否 | Request body (JSON object) |

---

### 3. github_gists_list_public

**描述**: List public gists

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| since | 否 | Only show results that were last updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. |

---

### 4. github_gists_list_starred

**描述**: List starred gists

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| since | 否 | Only show results that were last updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. |

---

### 5. github_gists_get

**描述**: Get a gist

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| gist_id | 是 | gist_id |

---

### 6. github_gists_update

**描述**: Update a gist

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| gist_id | 是 | gist_id |

---

### 7. github_gists_delete

**描述**: Delete a gist

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| gist_id | 是 | gist_id |

---

### 8. github_gists_list_comments

**描述**: List gist comments

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| gist_id | 是 | gist_id |

---

### 9. github_gists_create_comment

**描述**: Create a gist comment

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| gist_id | 是 | gist_id |

---

### 10. github_gists_get_comment

**描述**: Get a gist comment

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| gist_id | 是 | gist_id |

---

### 11. github_gists_update_comment

**描述**: Update a gist comment

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| gist_id | 是 | gist_id |

---

### 12. github_gists_delete_comment

**描述**: Delete a gist comment

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| gist_id | 是 | gist_id |

---

### 13. github_gists_list_commits

**描述**: List gist commits

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| gist_id | 是 | gist_id |

---

### 14. github_gists_list_forks

**描述**: List gist forks

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| gist_id | 是 | gist_id |

---

### 15. github_gists_fork

**描述**: Fork a gist

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| gist_id | 是 | gist_id |

---

### 16. github_gists_check_is_starred

**描述**: Check if a gist is starred

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| gist_id | 是 | gist_id |

---

### 17. github_gists_star

**描述**: Star a gist

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| gist_id | 是 | gist_id |

---

### 18. github_gists_unstar

**描述**: Unstar a gist

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| gist_id | 是 | gist_id |

---

### 19. github_gists_get_revision

**描述**: Get a gist revision

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| gist_id | 是 | gist_id |

---

### 20. github_gists_list_for_user

**描述**: List gists for a user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| username | 是 | username |

---

