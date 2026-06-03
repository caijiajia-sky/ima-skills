# GitHub MCP - Issues

## 概述

本Skill提供GitHub API的 **Issues** 相关操作能力，包含 **55** 个工具。

## 工具列表

### 1. github_issues_list

**描述**: List issues assigned to the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| filter | 否 | Indicates which sorts of issues to return. `assigned` means issues assigned to you. `created` means issues created by you. `mentioned` means issues mentioning you. `subscribed` means issues you're subscribed to updates for. `all` or `repos` means all issues you can see, regardless of participation or creation. |

---

### 2. github_issues_list_for_org

**描述**: List organization issues assigned to the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 3. github_issues_list_assignees

**描述**: List assignees

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 4. github_issues_check_user_can_be_assigned

**描述**: Check if a user can be assigned

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 5. github_issues_list_for_repo

**描述**: List repository issues

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 6. github_issues_create

**描述**: Create an issue

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 7. github_issues_list_comments_for_repo

**描述**: List issue comments for a repository

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 8. github_issues_get_comment

**描述**: Get an issue comment

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 9. github_issues_update_comment

**描述**: Update an issue comment

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 10. github_issues_delete_comment

**描述**: Delete an issue comment

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 11. github_issues_pin_comment

**描述**: Pin an issue comment

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 12. github_issues_unpin_comment

**描述**: Unpin an issue comment

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 13. github_issues_list_events_for_repo

**描述**: List issue events for a repository

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 14. github_issues_get_event

**描述**: Get an issue event

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 15. github_issues_get

**描述**: Get an issue

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 16. github_issues_update

**描述**: Update an issue

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 17. github_issues_add_assignees

**描述**: Add assignees to an issue

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 18. github_issues_remove_assignees

**描述**: Remove assignees from an issue

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 19. github_issues_check_user_can_be_assigned_to_issue

**描述**: Check if a user can be assigned to a issue

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 20. github_issues_list_comments

**描述**: List issue comments

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 21. github_issues_create_comment

**描述**: Create an issue comment

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 22. github_issues_list_dependencies_blocked_by

**描述**: List dependencies an issue is blocked by

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 23. github_issues_add_blocked_by_dependency

**描述**: Add a dependency an issue is blocked by

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 24. github_issues_remove_dependency_blocked_by

**描述**: Remove dependency an issue is blocked by

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 25. github_issues_list_dependencies_blocking

**描述**: List dependencies an issue is blocking

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 26. github_issues_list_events

**描述**: List issue events

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 27. github_issues_list_issue_field_values_for_issue

**描述**: List issue field values for an issue

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 28. github_issues_list_labels_on_issue

**描述**: List labels for an issue

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 29. github_issues_add_labels

**描述**: Add labels to an issue

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 30. github_issues_set_labels

**描述**: Set labels for an issue

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 31. github_issues_remove_all_labels

**描述**: Remove all labels from an issue

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 32. github_issues_remove_label

**描述**: Remove a label from an issue

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 33. github_issues_lock

**描述**: Lock an issue

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 34. github_issues_unlock

**描述**: Unlock an issue

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 35. github_issues_get_parent

**描述**: Get parent issue

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 36. github_issues_remove_sub_issue

**描述**: Remove sub-issue

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 37. github_issues_list_sub_issues

**描述**: List sub-issues

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 38. github_issues_add_sub_issue

**描述**: Add sub-issue

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 39. github_issues_reprioritize_sub_issue

**描述**: Reprioritize sub-issue

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 40. github_issues_list_events_for_timeline

**描述**: List timeline events for an issue

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 41. github_issues_list_labels_for_repo

**描述**: List labels for a repository

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 42. github_issues_create_label

**描述**: Create a label

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 43. github_issues_get_label

**描述**: Get a label

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 44. github_issues_update_label

**描述**: Update a label

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 45. github_issues_delete_label

**描述**: Delete a label

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 46. github_issues_list_milestones

**描述**: List milestones

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 47. github_issues_create_milestone

**描述**: Create a milestone

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 48. github_issues_get_milestone

**描述**: Get a milestone

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 49. github_issues_update_milestone

**描述**: Update a milestone

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 50. github_issues_delete_milestone

**描述**: Delete a milestone

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 51. github_issues_list_labels_for_milestone

**描述**: List labels for issues in a milestone

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 52. github_issues_add_issue_field_values

**描述**: Add issue field values to an issue

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| repository_id | 是 | repository_id |

---

### 53. github_issues_set_issue_field_values

**描述**: Set issue field values for an issue

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| repository_id | 是 | repository_id |

---

### 54. github_issues_delete_issue_field_value

**描述**: Delete an issue field value from an issue

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| repository_id | 是 | repository_id |

---

### 55. github_issues_list_for_authenticated_user

**描述**: List user account issues assigned to the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| filter | 否 | Indicates which sorts of issues to return. `assigned` means issues assigned to you. `created` means issues created by you. `mentioned` means issues mentioning you. `subscribed` means issues you're subscribed to updates for. `all` or `repos` means all issues you can see, regardless of participation or creation. |

---

