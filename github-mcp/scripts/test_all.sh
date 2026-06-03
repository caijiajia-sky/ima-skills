#!/bin/bash
# GitHub MCP 工具测试脚本
# 测试各类别的代表性工具
#
# ⚠️ 安全说明: 本文件已脱敏处理，请通过环境变量传入Token
#   export GITHUB_TOKEN=ghp_your_token_here

TOKEN="${GITHUB_TOKEN:-your_github_token_here}"
BASE_URL="https://api.github.com"

echo "============================================"
echo "GitHub MCP 工具测试"
echo "============================================"

# 1. 用户类测试
echo ""
echo "【1. github_users_get_authenticated】"
echo "→ 获取当前认证用户信息"
curl -s -H "Authorization: token $TOKEN" "$BASE_URL/user" | head -5

# 2. 搜索类测试
echo ""
echo "【2. github_search_repos】"
echo "→ 搜索仓库"
curl -s -H "Authorization: token $TOKEN" "$BASE_URL/search/repositories?q=stars:>1000" | head -5

# 3. 仓库类测试
echo ""
echo "【3. github_repos_get】"
echo "→ 获取仓库信息"
curl -s -H "Authorization: token $TOKEN" "$BASE_URL/repos/octocat/Hello-World" | head -5

# 4. Issues类测试
echo ""
echo "【4. github_issues_list_for_repo】"
echo "→ 列出仓库Issues"
curl -s -H "Authorization: token $TOKEN" "$BASE_URL/repos/octocat/Hello-World/issues" | head -5

# 5. Pull Requests类
echo ""
echo "【5. github_pulls_list】"
echo "→ 列出PRs"
curl -s -H "Authorization: token $TOKEN" "$BASE_URL/repos/octocat/Hello-World/pulls" | head -5

# 6. Actions类
echo ""
echo "【6. github_actions_list_workflows】"
echo "→ 列出工作流"
curl -s -H "Authorization: token $TOKEN" "$BASE_URL/repos/octocat/Hello-World/actions/workflows" | head -5

# 7. 组织类
echo ""
echo "【7. github_orgs_get】"
echo "→ 获取组织信息"
curl -s -H "Authorization: token $TOKEN" "$BASE_URL/orgs/github" | head -5

# 8. Gists类
echo ""
echo "【8. github_gists_list_public】"
echo "→ 列出公开Gists"
curl -s -H "Authorization: token $TOKEN" "$BASE_URL/gists/public" | head -5

echo ""
echo "============================================"
echo "测试完成"
echo "============================================"
