# GitHub MCP - Users

## 概述

本Skill提供GitHub API的 **Users** 相关操作能力，包含 **44** 个工具。

## 工具列表

### 1. github_users_get_authenticated

**描述**: Update the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| body | 否 | Request body (JSON object) |

---

### 2. github_users_list_blocked_by_authenticated_user

**描述**: List users blocked by the authenticated user


---

### 3. github_users_check_blocked

**描述**: Check if a user is blocked by the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| username | 是 | username |

---

### 4. github_users_block

**描述**: Block a user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| username | 是 | username |

---

### 5. github_users_unblock

**描述**: Unblock a user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| username | 是 | username |

---

### 6. github_users_set_primary_email_visibility_for_authenticated_user

**描述**: Set primary email visibility for the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| body | 否 | Request body (JSON object) |

---

### 7. github_users_list_emails_for_authenticated_user

**描述**: List email addresses for the authenticated user


---

### 8. github_users_add_email_for_authenticated_user

**描述**: Add an email address for the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| body | 否 | Request body (JSON object) |

---

### 9. github_users_delete_email_for_authenticated_user

**描述**: List followers of the authenticated user


---

### 10. github_users_list_followed_by_authenticated_user

**描述**: List the people the authenticated user follows


---

### 11. github_users_check_person_is_followed_by_authenticated

**描述**: Check if a person is followed by the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| username | 是 | username |

---

### 12. github_users_follow

**描述**: Follow a user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| username | 是 | username |

---

### 13. github_users_unfollow

**描述**: Unfollow a user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| username | 是 | username |

---

### 14. github_users_list_gpg_keys_for_authenticated_user

**描述**: List GPG keys for the authenticated user


---

### 15. github_users_create_gpg_key_for_authenticated_user

**描述**: Create a GPG key for the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| body | 否 | Request body (JSON object) |

---

### 16. github_users_get_gpg_key_for_authenticated_user

**描述**: Get a GPG key for the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| gpg_key_id | 是 | gpg_key_id |

---

### 17. github_users_delete_gpg_key_for_authenticated_user

**描述**: Delete a GPG key for the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| gpg_key_id | 是 | gpg_key_id |

---

### 18. github_users_list_public_ssh_keys_for_authenticated_user

**描述**: List public SSH keys for the authenticated user


---

### 19. github_users_create_public_ssh_key_for_authenticated_user

**描述**: Create a public SSH key for the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| body | 否 | Request body (JSON object) |

---

### 20. github_users_get_public_ssh_key_for_authenticated_user

**描述**: Get a public SSH key for the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| key_id | 是 | key_id |

---

### 21. github_users_delete_public_ssh_key_for_authenticated_user

**描述**: Delete a public SSH key for the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| key_id | 是 | key_id |

---

### 22. github_users_list_public_emails_for_authenticated_user

**描述**: List public email addresses for the authenticated user


---

### 23. github_users_list_social_accounts_for_authenticated_user

**描述**: List social accounts for the authenticated user


---

### 24. github_users_add_social_account_for_authenticated_user

**描述**: Add social accounts for the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| body | 否 | Request body (JSON object) |

---

### 25. github_users_delete_social_account_for_authenticated_user

**描述**: List SSH signing keys for the authenticated user


---

### 26. github_users_create_ssh_signing_key_for_authenticated_user

**描述**: Create a SSH signing key for the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| body | 否 | Request body (JSON object) |

---

### 27. github_users_get_ssh_signing_key_for_authenticated_user

**描述**: Get an SSH signing key for the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| ssh_signing_key_id | 是 | ssh_signing_key_id |

---

### 28. github_users_delete_ssh_signing_key_for_authenticated_user

**描述**: Delete an SSH signing key for the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| ssh_signing_key_id | 是 | ssh_signing_key_id |

---

### 29. github_users_get_by_id

**描述**: Get a user using their ID

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| account_id | 是 | account_id |

---

### 30. github_users_list

**描述**: List users

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| since | 否 | A user ID. Only return users with an ID greater than this ID. |

---

### 31. github_users_get_by_username

**描述**: Get a user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| username | 是 | username |

---

### 32. github_users_list_attestations_bulk

**描述**: List attestations by bulk subject digests

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| username | 是 | username |

---

### 33. github_users_delete_attestations_bulk

**描述**: Delete attestations in bulk

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| username | 是 | username |

---

### 34. github_users_delete_attestations_by_subject_digest

**描述**: Delete attestations by subject digest

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| username | 是 | username |

---

### 35. github_users_delete_attestations_by_id

**描述**: Delete attestations by ID

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| username | 是 | username |

---

### 36. github_users_list_attestations

**描述**: List attestations

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| username | 是 | username |

---

### 37. github_users_list_followers_for_user

**描述**: List followers of a user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| username | 是 | username |

---

### 38. github_users_list_following_for_user

**描述**: List the people a user follows

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| username | 是 | username |

---

### 39. github_users_check_following_for_user

**描述**: Check if a user follows another user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| username | 是 | username |

---

### 40. github_users_list_gpg_keys_for_user

**描述**: List GPG keys for a user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| username | 是 | username |

---

### 41. github_users_get_context_for_user

**描述**: Get contextual information for a user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| username | 是 | username |

---

### 42. github_users_list_public_keys_for_user

**描述**: List public keys for a user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| username | 是 | username |

---

### 43. github_users_list_social_accounts_for_user

**描述**: List social accounts for a user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| username | 是 | username |

---

### 44. github_users_list_ssh_signing_keys_for_user

**描述**: List SSH signing keys for a user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| username | 是 | username |

---

