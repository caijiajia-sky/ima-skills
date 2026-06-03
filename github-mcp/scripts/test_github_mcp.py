#!/usr/bin/env python3
"""
GitHub MCP 工具测试脚本
用于测试GitHub MCP的各个工具
"""

import json
import subprocess

def test_tool(tool_name, params):
    """测试一个GitHub MCP工具"""
    print(f"\n{'='*60}")
    print(f"测试工具: {tool_name}")
    print(f"参数: {json.dumps(params, indent=2)}")
    print('='*60)
    
    # 构建命令
    cmd = [
        "npx", "-y", "github-rest-mcp",
        tool_name,
        json.dumps(params)
    ]
    
    print(f"\n命令: {' '.join(cmd)}")
    print("\n结果:")
    
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=30
        )
        print(result.stdout)
        if result.stderr:
            print(f"错误: {result.stderr}")
    except Exception as e:
        print(f"执行失败: {e}")

def list_all_tools():
    """列出所有可用工具"""
    print("""
GitHub MCP 工具列表 (1112个工具, 44个类别)

=== 搜索类 (7工具) ===
github_search_code, github_search_commits, github_search_issues_and_pull_requests,
github_search_labels, github_search_repos, github_search_topics, github_search_users

=== 仓库类 (201工具) ===
github_repos_get, github_repos_list_for_user, github_repos_list_for_authenticated_user,
github_repos_create_for_authenticated_user, github_repos_update, github_repos_delete,
github_repos_list_branches, github_repos_get_branch, github_repos_create_or_update_file_contents,
... (更多请查看 /sandbox/workspace/github-mcp-skill/references/tools.md)

=== Issues类 (55工具) ===
github_issues_list, github_issues_list_for_repo, github_issues_get,
github_issues_create, github_issues_update, github_issues_add_labels,
github_issues_list_comments, github_issues_create_comment, ...

=== Pull Requests类 (27工具) ===
github_pulls_list, github_pulls_list_for_repo, github_pulls_get,
github_pulls_create, github_pulls_update, github_pulls_merge, ...

=== Actions类 (184工具) ===
github_actions_list_repo_workflows, github_actions_get_workflow_run,
github_actions_list_artifacts_for_repo, github_actions_list_repo_secrets, ...

=== 组织类 (108工具) ===
github_orgs_get, github_orgs_list_for_authenticated_user, github_orgs_update, ...

=== 用户类 (47工具) ===
github_users_get_authenticated, github_users_update_authenticated,
github_users_list_followers_for_authenticated_user, ...

=== 团队类 (32工具) ===
github_teams_list, github_teams_create, github_teams_get_by_name, ...

=== 代码空间类 (48工具) ===
github_codespaces_list_for_authenticated_user, github_codespaces_create, ...

=== Copilot类 (25工具) ===
github_copilot_list_seats, github_copilot_add_billing_manager, ...

... (更多类别请查看 /sandbox/workspace/github-mcp-skill/references/categories.md)
""")

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == '--list':
            list_all_tools()
        elif sys.argv[1] == '--test' and len(sys.argv) > 2:
            tool_name = sys.argv[2]
            params = json.loads(sys.argv[3]) if len(sys.argv) > 3 else {}
            test_tool(tool_name, params)
        else:
            print("用法:")
            print("  python3 test_github_mcp.py --list           # 列出所有工具")
            print("  python3 test_github_mcp.py --test <tool> [params]  # 测试工具")
    else:
        list_all_tools()