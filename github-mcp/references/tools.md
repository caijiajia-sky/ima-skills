# GitHub MCP 工具完整列表

## 工具命名规范

所有工具遵循 `github_{category}_{action}` 命名模式。

## 搜索类 (Search) - 7工具

### github_search_code
- **描述**: Search code
- **参数**: q, sort, order, per_page, page

### github_search_commits  
- **描述**: Search commits
- **参数**: q, sort, order, per_page, page

### github_search_issues_and_pull_requests
- **描述**: Search issues and pull requests
- **参数**: q, sort, order, per_page, page, type

### github_search_labels
- **描述**: Search labels
- **参数**: repository_id, q, per_page, page

### github_search_repos
- **描述**: Search repositories
- **参数**: q, sort, order, per_page, page

### github_search_topics
- **描述**: Search topics
- **参数**: q, per_page, page

### github_search_users
- **描述**: Search users
- **参数**: q, sort, order, per_page, page

## Issues类 (55工具)

### 列表查询
- github_issues_list
- github_issues_list_for_org
- github_issues_list_assignees
- github_issues_list_for_repo
- github_issues_list_comments_for_repo
- github_issues_list_events_for_repo
- github_issues_list_events
- github_issues_list_events_for_timeline
- github_issues_list_dependencies_blocked_by
- github_issues_list_dependencies_blocking
- github_issues_list_sub_issues
- github_issues_list_labels_for_repo
- github_issues_list_labels_for_milestone
- github_issues_list_milestones
- github_issues_list_comments
- github_issues_list_issue_field_values_for_issue

### 增删改查
- github_issues_create
- github_issues_get
- github_issues_update
- github_issues_delete
- github_issues_get_comment
- github_issues_update_comment
- github_issues_delete_comment
- github_issues_add_assignees
- github_issues_remove_assignees
- github_issues_create_comment
- github_issues_add_labels
- github_issues_set_labels
- github_issues_remove_all_labels
- github_issues_remove_label
- github_issues_create_label
- github_issues_get_label
- github_issues_update_label
- github_issues_delete_label
- github_issues_create_milestone
- github_issues_get_milestone
- github_issues_update_milestone
- github_issues_delete_milestone

### 特殊操作
- github_issues_check_user_can_be_assigned
- github_issues_check_user_can_be_assigned_to_issue
- github_issues_pin_comment
- github_issues_unpin_comment
- github_issues_get_event
- github_issues_lock
- github_issues_unlock
- github_issues_get_parent
- github_issues_remove_sub_issue
- github_issues_add_sub_issue
- github_issues_reprioritize_sub_issue
- github_issues_add_blocked_by_dependency
- github_issues_remove_dependency_blocked_by
- github_issues_add_issue_field_values
- github_issues_set_issue_field_values
- github_issues_delete_issue_field_value

## Pull Requests类 (27工具)

### github_pulls_list
### github_pulls_list_for_repo
### github_pulls_get
### github_pulls_create
### github_pulls_update
### github_pulls_list_commits
### github_pulls_list_files
### github_pulls_get_by_number
### github_pulls_create_review
### github_pulls_update_review
### github_pulls_delete_pending_review
### github_pulls_list_reviews
### github_pulls_get_review
### github_pulls_list_comments_for_review
### github_pulls_create_review_comment
### github_pulls_update_review_comment
### github_pulls_delete_review_comment
### github_pulls_merge
### github_pulls_is_merged
### github_pulls_list_review_comments
### github_pulls_list_review_comments_for_repo

## Repos类 (201工具) - 最大类别

### 仓库操作
- github_repos_get
- github_repos_list_for_authenticated_user
- github_repos_list_for_user
- github_repos_list_public
- github_repos_create_for_authenticated_user
- github_repos_create_in_org
- github_repos_create_using_template
- github_repos_update
- github_repos_delete
- github_repos_get_clones
- github_repos_get_top_referrers
- github_repos_get_views
- github_repos_list_invitations_for_authenticated_user
- github_repos_accept_invitation
- github_repos_decline_invitation

### 分支操作
- github_repos_list_branches
- github_repos_get_branch
- github_repos_list_protected_branches
- github_repos_get_branch_protection
- github_repos_update_branch_protection
- github_repos_delete_branch_protection
- github_repos_list_collaborators
- github_repos_check_collaborator
- github_repos_add_collaborator
- github_repos_remove_collaborator

### 文件操作
- github_repos_get_contents
- github_repos_get_content
- github_repos_create_or_update_file_contents
- github_repos_delete_file

### 发布管理
- github_repos_list_releases
- github_repos_get_release
- github_repos_create_release
- github_repos_update_release
- github_repos_delete_release
- github_repos_get_latest_release
- github_repos_list_tags

### 环境变量
- github_repos_get_environment
- github_repos_list_environment_secrets
- github_repos_get_environment_secret
- github_repos_create_or_update_environment_secret
- github_repos_delete_environment_secret

### 其他操作
... (更多工具，请查看 /sandbox/workspace/github-mcp-skills/repos.md)

## Actions类 (184工具)

### 工作流运行
- github_actions_list_repo_workflows
- github_actions_get_workflow
- github_actions_disable_workflow
- github_actions_enable_workflow
- github_actions_list_workflow_runs
- github_actions_get_workflow_run
- github_actions_cancel_workflow_run
- github_actions_list_jobs_for_workflow_run
- github_actions_download_workflow_run_logs
- github_actions_delete_workflow_run_logs
- github_actions_re_run_workflow

### Artifacts
- github_actions_list_artifacts_for_repo
- github_actions_get_artifact
- github_actions_delete_artifact
- github_actions_download_artifact

### 秘钥管理
- github_actions_list_repo_secrets
- github_actions_get_repo_public_key
- github_actions_get_repo_secret
- github_actions_create_or_update_repo_secret
- github_actions_delete_repo_secret

### 运行器
- github_actions_list_self_hosted_runners_for_repo
- github_actions_list_labels_for_repo_runner
- github_actions_add_labels_to_repo_runner
- github_actions_remove_all_labels_from_repo_runner
- github_actions_remove_label_from_repo_runner
- github_actions_create_registration_token_for_repo
- github_actions_create_remove_token_for_repo
- github_actions_delete_self_hosted_runner_from_repo

### 组织级别
- github_actions_list_selected_repositories_enabled_github_actions_organization
- github_actions_set_selected_repositories_enabled_github_actions_organization
- github_actions_list_self_hosted_runner_groups_for_org
- github_actions_create_self_hosted_runner_group_for_org
... (更多工具，请查看 /sandbox/workspace/github-mcp-skills/actions.md)