# GitHub MCP - Apps

## 概述

本Skill提供GitHub API的 **Apps** 相关操作能力，包含 **34** 个工具。

## 工具列表

### 1. github_apps_get_authenticated

**描述**: Create a GitHub App from a manifest

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| code | 是 | code |

---

### 2. github_apps_get_webhook_config_for_app

**描述**: Update a webhook configuration for an app

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| body | 否 | Request body (JSON object) |

---

### 3. github_apps_list_webhook_deliveries

**描述**: List deliveries for an app webhook


---

### 4. github_apps_get_webhook_delivery

**描述**: Get a delivery for an app webhook

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| delivery_id | 是 | delivery_id |

---

### 5. github_apps_redeliver_webhook_delivery

**描述**: Redeliver a delivery for an app webhook

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| delivery_id | 是 | delivery_id |

---

### 6. github_apps_list_installation_requests_for_authenticated_app

**描述**: List installation requests for the authenticated app


---

### 7. github_apps_list_installations

**描述**: List installations for the authenticated app


---

### 8. github_apps_get_installation

**描述**: Get an installation for the authenticated app

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| installation_id | 是 | installation_id |

---

### 9. github_apps_delete_installation

**描述**: Delete an installation for the authenticated app

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| installation_id | 是 | installation_id |

---

### 10. github_apps_create_installation_access_token

**描述**: Create an installation access token for an app

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| installation_id | 是 | installation_id |

---

### 11. github_apps_suspend_installation

**描述**: Suspend an app installation

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| installation_id | 是 | installation_id |

---

### 12. github_apps_unsuspend_installation

**描述**: Unsuspend an app installation

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| installation_id | 是 | installation_id |

---

### 13. github_apps_delete_authorization

**描述**: Delete an app authorization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| client_id | 是 | client_id |

---

### 14. github_apps_check_token

**描述**: Check a token

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| client_id | 是 | client_id |

---

### 15. github_apps_reset_token

**描述**: Reset a token

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| client_id | 是 | client_id |

---

### 16. github_apps_delete_token

**描述**: Delete an app token

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| client_id | 是 | client_id |

---

### 17. github_apps_scope_token

**描述**: Create a scoped access token

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| client_id | 是 | client_id |

---

### 18. github_apps_get_by_slug

**描述**: Get an app

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| app_slug | 是 | app_slug |

---

### 19. github_apps_list_repos_accessible_to_installation

**描述**: List repositories accessible to the app installation


---

### 20. github_apps_revoke_installation_access_token

**描述**: Get a subscription plan for an account

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| account_id | 是 | account_id |

---

### 21. github_apps_list_plans

**描述**: List plans


---

### 22. github_apps_list_accounts_for_plan

**描述**: List accounts for a plan

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| plan_id | 是 | plan_id |

---

### 23. github_apps_get_subscription_plan_for_account_stubbed

**描述**: Get a subscription plan for an account (stubbed)

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| account_id | 是 | account_id |

---

### 24. github_apps_list_plans_stubbed

**描述**: List plans (stubbed)


---

### 25. github_apps_list_accounts_for_plan_stubbed

**描述**: List accounts for a plan (stubbed)

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| plan_id | 是 | plan_id |

---

### 26. github_apps_get_org_installation

**描述**: Get an organization installation for the authenticated app

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 27. github_apps_get_repo_installation

**描述**: Get a repository installation for the authenticated app

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| owner | 是 | owner |

---

### 28. github_apps_list_installations_for_authenticated_user

**描述**: List app installations accessible to the user access token


---

### 29. github_apps_list_installation_repos_for_authenticated_user

**描述**: List repositories accessible to the user access token

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| installation_id | 是 | installation_id |

---

### 30. github_apps_add_repo_to_installation_for_authenticated_user

**描述**: Add a repository to an app installation

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| installation_id | 是 | installation_id |

---

### 31. github_apps_remove_repo_from_installation_for_authenticated_user

**描述**: Remove a repository from an app installation

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| installation_id | 是 | installation_id |

---

### 32. github_apps_list_subscriptions_for_authenticated_user

**描述**: List subscriptions for the authenticated user


---

### 33. github_apps_list_subscriptions_for_authenticated_user_stubbed

**描述**: List subscriptions for the authenticated user (stubbed)


---

### 34. github_apps_get_user_installation

**描述**: Get a user installation for the authenticated app

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| username | 是 | username |

---

