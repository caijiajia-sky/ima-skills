# GitHub MCP - Activity

## 概述

本Skill提供GitHub API的 **Activity** 相关操作能力，包含 **31** 个工具。

## 工具列表

### 1. github_activity_list_public_events

**描述**: List public events


---

### 2. github_activity_get_feeds

**描述**: List public events for a network of repositories

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 3. github_activity_list_notifications_for_authenticated_user

**描述**: List notifications for the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| all | 否 | If `true`, show notifications marked as read. |

---

### 4. github_activity_mark_notifications_as_read

**描述**: Mark notifications as read

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| body | 否 | Request body (JSON object) |

---

### 5. github_activity_get_thread

**描述**: Get a thread

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| thread_id | 是 | thread_id |

---

### 6. github_activity_mark_thread_as_read

**描述**: Mark a thread as read

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| thread_id | 是 | thread_id |

---

### 7. github_activity_mark_thread_as_done

**描述**: Mark a thread as done

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| thread_id | 是 | thread_id |

---

### 8. github_activity_get_thread_subscription_for_authenticated_user

**描述**: Get a thread subscription for the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| thread_id | 是 | thread_id |

---

### 9. github_activity_set_thread_subscription

**描述**: Set a thread subscription

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| thread_id | 是 | thread_id |

---

### 10. github_activity_delete_thread_subscription

**描述**: Delete a thread subscription

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| thread_id | 是 | thread_id |

---

### 11. github_activity_list_public_org_events

**描述**: List public organization events

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 12. github_activity_list_repo_events

**描述**: List repository events

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 13. github_activity_list_repo_notifications_for_authenticated_user

**描述**: List repository notifications for the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 14. github_activity_mark_repo_notifications_as_read

**描述**: Mark repository notifications as read

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 15. github_activity_list_stargazers_for_repo

**描述**: List stargazers

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 16. github_activity_list_watchers_for_repo

**描述**: List watchers

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 17. github_activity_get_repo_subscription

**描述**: Get a repository subscription

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 18. github_activity_set_repo_subscription

**描述**: Set a repository subscription

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 19. github_activity_delete_repo_subscription

**描述**: Delete a repository subscription

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 20. github_activity_list_repos_starred_by_authenticated_user

**描述**: List repositories starred by the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| sort | 否 | The property to sort the results by. `created` means when the repository was starred. `updated` means when the repository was last pushed to. |

---

### 21. github_activity_check_repo_is_starred_by_authenticated_user

**描述**: Check if a repository is starred by the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 22. github_activity_star_repo_for_authenticated_user

**描述**: Star a repository for the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 23. github_activity_unstar_repo_for_authenticated_user

**描述**: Unstar a repository for the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 24. github_activity_list_watched_repos_for_authenticated_user

**描述**: List repositories watched by the authenticated user


---

### 25. github_activity_list_events_for_authenticated_user

**描述**: List events for the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| username | 是 | username |

---

### 26. github_activity_list_org_events_for_authenticated_user

**描述**: List organization events for the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| username | 是 | username |

---

### 27. github_activity_list_public_events_for_user

**描述**: List public events for a user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| username | 是 | username |

---

### 28. github_activity_list_received_events_for_user

**描述**: List events received by the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| username | 是 | username |

---

### 29. github_activity_list_received_public_events_for_user

**描述**: List public events received by a user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| username | 是 | username |

---

### 30. github_activity_list_repos_starred_by_user

**描述**: List repositories starred by a user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| username | 是 | username |

---

### 31. github_activity_list_repos_watched_by_user

**描述**: List repositories watched by a user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| username | 是 | username |

---

