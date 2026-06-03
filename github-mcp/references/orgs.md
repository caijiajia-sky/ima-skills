# GitHub MCP - Orgs

## 概述

本Skill提供GitHub API的 **Orgs** 相关操作能力，包含 **108** 个工具。

## 工具列表

### 1. github_orgs_list

**描述**: List organizations

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| since | 否 | An organization ID. Only return organizations with an ID greater than this ID. |

---

### 2. github_orgs_get

**描述**: Get an organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 3. github_orgs_update

**描述**: Update an organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 4. github_orgs_delete

**描述**: Delete an organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 5. github_orgs_create_artifact_deployment_record

**描述**: Create an artifact deployment record

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 6. github_orgs_set_cluster_deployment_records

**描述**: Set cluster deployment records

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 7. github_orgs_create_artifact_storage_record

**描述**: Create artifact metadata storage record

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 8. github_orgs_list_artifact_deployment_records

**描述**: List artifact deployment records

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 9. github_orgs_list_artifact_storage_records

**描述**: List artifact storage records

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 10. github_orgs_list_attestations_bulk

**描述**: List attestations by bulk subject digests

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 11. github_orgs_delete_attestations_bulk

**描述**: Delete attestations in bulk

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 12. github_orgs_delete_attestations_by_subject_digest

**描述**: Delete attestations by subject digest

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 13. github_orgs_list_attestation_repositories

**描述**: List attestation repositories

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 14. github_orgs_delete_attestations_by_id

**描述**: Delete attestations by ID

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 15. github_orgs_list_attestations

**描述**: List attestations

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 16. github_orgs_list_blocked_users

**描述**: List users blocked by an organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 17. github_orgs_check_blocked_user

**描述**: Check if a user is blocked by an organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 18. github_orgs_block_user

**描述**: Block a user from an organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 19. github_orgs_unblock_user

**描述**: Unblock a user from an organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 20. github_orgs_list_failed_invitations

**描述**: List failed organization invitations

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 21. github_orgs_list_webhooks

**描述**: List organization webhooks

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 22. github_orgs_create_webhook

**描述**: Create an organization webhook

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 23. github_orgs_get_webhook

**描述**: Get an organization webhook

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 24. github_orgs_update_webhook

**描述**: Update an organization webhook

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 25. github_orgs_delete_webhook

**描述**: Delete an organization webhook

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 26. github_orgs_get_webhook_config_for_org

**描述**: Get a webhook configuration for an organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 27. github_orgs_update_webhook_config_for_org

**描述**: Update a webhook configuration for an organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 28. github_orgs_list_webhook_deliveries

**描述**: List deliveries for an organization webhook

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 29. github_orgs_get_webhook_delivery

**描述**: Get a webhook delivery for an organization webhook

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 30. github_orgs_redeliver_webhook_delivery

**描述**: Redeliver a delivery for an organization webhook

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 31. github_orgs_ping_webhook

**描述**: Ping an organization webhook

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 32. github_api_insights_get_route_stats_by_actor

**描述**: Get route stats by actor

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 33. github_api_insights_get_subject_stats

**描述**: Get subject stats

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 34. github_api_insights_get_summary_stats

**描述**: Get summary stats

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 35. github_api_insights_get_summary_stats_by_user

**描述**: Get summary stats by user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 36. github_api_insights_get_summary_stats_by_actor

**描述**: Get summary stats by actor

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 37. github_api_insights_get_time_stats

**描述**: Get time stats

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 38. github_api_insights_get_time_stats_by_user

**描述**: Get time stats by user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 39. github_api_insights_get_time_stats_by_actor

**描述**: Get time stats by actor

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 40. github_api_insights_get_user_stats

**描述**: Get user stats

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 41. github_orgs_list_app_installations

**描述**: List app installations for an organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 42. github_orgs_list_pending_invitations

**描述**: List pending organization invitations

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 43. github_orgs_create_invitation

**描述**: Create an organization invitation

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 44. github_orgs_cancel_invitation

**描述**: Cancel an organization invitation

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 45. github_orgs_list_invitation_teams

**描述**: List organization invitation teams

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 46. github_orgs_list_issue_fields

**描述**: List issue fields for an organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 47. github_orgs_create_issue_field

**描述**: Create issue field for an organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 48. github_orgs_update_issue_field

**描述**: Update issue field for an organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 49. github_orgs_delete_issue_field

**描述**: Delete issue field for an organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 50. github_orgs_list_issue_types

**描述**: List issue types for an organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 51. github_orgs_create_issue_type

**描述**: Create issue type for an organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 52. github_orgs_update_issue_type

**描述**: Update issue type for an organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 53. github_orgs_delete_issue_type

**描述**: Delete issue type for an organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 54. github_orgs_list_members

**描述**: List organization members

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 55. github_orgs_check_membership_for_user

**描述**: Check organization membership for a user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 56. github_orgs_remove_member

**描述**: Remove an organization member

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 57. github_orgs_get_membership_for_user

**描述**: Get organization membership for a user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 58. github_orgs_set_membership_for_user

**描述**: Set organization membership for a user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 59. github_orgs_remove_membership_for_user

**描述**: Remove organization membership for a user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 60. github_orgs_list_org_roles

**描述**: Get all organization roles for an organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 61. github_orgs_revoke_all_org_roles_team

**描述**: Remove all organization roles for a team

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 62. github_orgs_assign_team_to_org_role

**描述**: Assign an organization role to a team

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 63. github_orgs_revoke_org_role_team

**描述**: Remove an organization role from a team

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 64. github_orgs_revoke_all_org_roles_user

**描述**: Remove all organization roles for a user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 65. github_orgs_assign_user_to_org_role

**描述**: Assign an organization role to a user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 66. github_orgs_revoke_org_role_user

**描述**: Remove an organization role from a user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 67. github_orgs_get_org_role

**描述**: Get an organization role

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 68. github_orgs_list_org_role_teams

**描述**: List teams that are assigned to an organization role

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 69. github_orgs_list_org_role_users

**描述**: List users that are assigned to an organization role

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 70. github_orgs_list_outside_collaborators

**描述**: List outside collaborators for an organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 71. github_orgs_convert_member_to_outside_collaborator

**描述**: Convert an organization member to outside collaborator

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 72. github_orgs_remove_outside_collaborator

**描述**: Remove outside collaborator from an organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 73. github_orgs_list_pat_grant_requests

**描述**: List requests to access organization resources with fine-grained personal access tokens

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 74. github_orgs_review_pat_grant_requests_in_bulk

**描述**: Review requests to access organization resources with fine-grained personal access tokens

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 75. github_orgs_review_pat_grant_request

**描述**: Review a request to access organization resources with a fine-grained personal access token

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 76. github_orgs_list_pat_grant_request_repositories

**描述**: List repositories requested to be accessed by a fine-grained personal access token

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 77. github_orgs_list_pat_grants

**描述**: List fine-grained personal access tokens with access to organization resources

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 78. github_orgs_update_pat_accesses

**描述**: Update the access to organization resources via fine-grained personal access tokens

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 79. github_orgs_update_pat_access

**描述**: Update the access a fine-grained personal access token has to organization resources

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 80. github_orgs_list_pat_grant_repositories

**描述**: List repositories a fine-grained personal access token has access to

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 81. github_orgs_custom_properties_for_repos_get_organization_definitions

**描述**: Get all custom properties for an organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 82. github_orgs_custom_properties_for_repos_create_or_update_organization_definitions

**描述**: Create or update custom properties for an organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 83. github_orgs_custom_properties_for_repos_get_organization_definition

**描述**: Get a custom property for an organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 84. github_orgs_custom_properties_for_repos_create_or_update_organization_definition

**描述**: Create or update a custom property for an organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 85. github_orgs_custom_properties_for_repos_delete_organization_definition

**描述**: Remove a custom property for an organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 86. github_orgs_custom_properties_for_repos_get_organization_values

**描述**: List custom property values for organization repositories

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 87. github_orgs_custom_properties_for_repos_create_or_update_organization_values

**描述**: Create or update custom property values for organization repositories

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 88. github_orgs_list_public_members

**描述**: List public organization members

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 89. github_orgs_check_public_membership_for_user

**描述**: Check public organization membership for a user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 90. github_orgs_set_public_membership_for_authenticated_user

**描述**: Set public organization membership for the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 91. github_orgs_remove_public_membership_for_authenticated_user

**描述**: Remove public organization membership for the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 92. github_orgs_get_org_ruleset_history

**描述**: Get organization ruleset history

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 93. github_orgs_get_org_ruleset_version

**描述**: Get organization ruleset version

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 94. github_orgs_list_security_manager_teams

**描述**: List security manager teams

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 95. github_orgs_add_security_manager_team

**描述**: Add a security manager team

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 96. github_orgs_remove_security_manager_team

**描述**: Remove a security manager team

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 97. github_orgs_get_immutable_releases_settings

**描述**: Get immutable releases settings for an organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 98. github_orgs_set_immutable_releases_settings

**描述**: Set immutable releases settings for an organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 99. github_orgs_get_immutable_releases_settings_repositories

**描述**: List selected repositories for immutable releases enforcement

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 100. github_orgs_set_immutable_releases_settings_repositories

**描述**: Set selected repositories for immutable releases enforcement

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 101. github_orgs_enable_selected_repository_immutable_releases_organization

**描述**: Enable a selected repository for immutable releases in an organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 102. github_orgs_disable_selected_repository_immutable_releases_organization

**描述**: Disable a selected repository for immutable releases in an organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 103. github_orgs_enable_or_disable_security_product_on_all_org_repos

**描述**: Enable or disable a security feature for an organization

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 104. github_orgs_list_memberships_for_authenticated_user

**描述**: List organization memberships for the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| state | 否 | Indicates the state of the memberships to return. If not specified, the API returns both active and pending memberships. |

---

### 105. github_orgs_get_membership_for_authenticated_user

**描述**: Get an organization membership for the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 106. github_orgs_update_membership_for_authenticated_user

**描述**: Update an organization membership for the authenticated user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| org | 是 | org |

---

### 107. github_orgs_list_for_authenticated_user

**描述**: List organizations for the authenticated user


---

### 108. github_orgs_list_for_user

**描述**: List organizations for a user

**参数**:

| 参数名 | 必填 | 描述 |
|--------|------|------|
| username | 是 | username |

---

