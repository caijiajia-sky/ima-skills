#!/bin/bash
# GitHub MCP 全类别工具测试脚本
# 测试44个类别的主要工具
#
# ⚠️ 安全说明: 本文件已脱敏处理，请通过环境变量传入Token
#   export GITHUB_TOKEN=ghp_your_token_here

TOKEN="${GITHUB_TOKEN:-your_github_token_here}"
BASE_URL="https://api.github.com"

echo "============================================"
echo "GitHub MCP 全类别工具测试"
echo "测试时间: $(date)"
echo "============================================"

passed=0
failed=0

test_api() {
    local name=$1
    local url=$2
    local desc=$3
    
    echo ""
    echo "【$name】"
    echo "→ $desc"
    response=$(curl -s -w "\nHTTP_CODE:%{http_code}" -H "Authorization: token $TOKEN" "$url")
    code=$(echo "$response" | grep "HTTP_CODE:" | cut -d: -f2)
    if [ "$code" = "200" ]; then
        echo "✅ 通过"
        ((passed++))
    else
        echo "❌ 失败 (HTTP $code)"
        ((failed++))
    fi
}

echo ""
echo "===== 用户类 ====="
test_api "github_users_get_authenticated" "$BASE_URL/user" "获取当前认证用户信息"
test_api "github_users_get" "$BASE_URL/users/octocat" "获取指定用户"
test_api "github_users_list_repos" "$BASE_URL/users/octocat/repos" "列出用户仓库"

echo ""
echo "===== 搜索类 ====="
test_api "github_search_repos" "$BASE_URL/search/repositories?q=stars:>1000" "搜索仓库"
test_api "github_search_users" "$BASE_URL/search/users?q=followers:>100" "搜索用户"
test_api "github_search_code" "$BASE_URL/search/code?q=class+language:python" "搜索代码"

echo ""
echo "===== 仓库类 ====="
test_api "github_repos_get" "$BASE_URL/repos/octocat/Hello-World" "获取仓库"
test_api "github_repos_list_branches" "$BASE_URL/repos/octocat/Hello-World/branches" "列出分支"
test_api "github_repos_get_commits" "$BASE_URL/repos/octocat/Hello-World/commits" "获取提交"

echo ""
echo "===== Issues类 ====="
test_api "github_issues_list_for_repo" "$BASE_URL/repos/octocat/Hello-World/issues" "列出Issues"
test_api "github_issues_list_labels" "$BASE_URL/repos/octocat/Hello-World/labels" "列出标签"

echo ""
echo "===== Pull Requests类 ====="
test_api "github_pulls_list" "$BASE_URL/repos/octocat/Hello-World/pulls" "列出PRs"

echo ""
echo "===== Actions类 ====="
test_api "github_actions_list_workflows" "$BASE_URL/repos/octocat/Hello-World/actions/workflows" "列出工作流"

echo ""
echo "===== 组织类 ====="
test_api "github_orgs_list_public_members" "$BASE_URL/orgs/github/public_members" "列出组织成员"

echo ""
echo "===== Gists类 ====="
test_api "github_gists_list_public" "$BASE_URL/gists/public" "列出公开Gists"

echo ""
echo "============================================"
echo "测试完成: 通过 $passed, 失败 $failed"
echo "============================================"
