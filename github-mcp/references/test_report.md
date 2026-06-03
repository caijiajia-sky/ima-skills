# GitHub MCP 测试报告

## 测试时间
2026-05-30

## 测试环境
- Token: 已配置 (caijiajia-sky)
- API版本: GitHub REST API v3
- 测试工具: github-rest-mcp

---

## ✅ 测试结果汇总

| # | 工具类别 | 工具名称 | 状态 | 备注 |
|---|---------|----------|------|------|
| 1 | 用户类 | `github_users_get_authenticated` | ✅ 通过 | 获取当前用户 |
| 2 | 搜索类 | `github_search_repos` | ✅ 通过 | 搜索仓库 |
| 3 | 仓库类 | `github_repos_get` | ✅ 通过 | 获取仓库信息 |
| 4 | 仓库类 | `github_repos_list_branches` | ✅ 通过 | 列出分支 |
| 5 | Issues类 | `github_issues_list_for_repo` | ✅ 通过 | 列出Issues |
| 6 | Pull Requests类 | `github_pulls_list_for_repo` | ✅ 通过 | 列出PRs |
| 7 | 组织类 | `github_orgs_get` | ✅ 通过 | 获取组织信息 |
| 8 | 团队类 | `github_teams_list` | ✅ 通过 | 用户未加入团队 |
| 9 | Gists类 | `github_gists_list_for_user` | ✅ 通过 | 列出gists |
| 10 | 速率限制类 | `github_rate_limit_get` | ✅ 通过 | 检查限速 |
| 11 | 搜索类 | `github_search_users` | ✅ 通过 | 搜索用户 |
| 12 | 搜索类 | `github_search_code` | ✅ 通过 | 搜索代码 |

---

## 详细测试记录

### 1. github_users_get_authenticated
```
请求: GET /user
响应: {
  "login": "caijiajia-sky",
  "id": 264462328,
  "node_id": "U_kgDOD8Nf-A",
  "avatar_url": "https://avatars.githubusercontent.com/u/264462328?v=4",
  ...
}
```

### 2. github_search_repos
```
请求: GET /search/repositories?q=javascript&per_page=2
响应: {
  "total_count": 3003509,
  "incomplete_results": false,
  "items": [
    { "name": "javascript", "full_name": "airbnb/javascript", ... },
    ...
  ]
}
```

### 3. github_repos_get
```
请求: GET /repos/facebook/react
响应: {
  "id": 10270250,
  "name": "react",
  "full_name": "facebook/react",
  "private": false,
  "owner": { "login": "facebook", ... },
  ...
}
```

### 4. github_repos_list_branches
```
请求: GET /repos/facebook/react/branches?per_page=3
响应: [
  { "name": "0.3-stable", "commit": {...}, "protected": false },
  { "name": "0.4-stable", "commit": {...}, "protected": false },
  { "name": "0.5-stable", "commit": {...}, "protected": false }
]
```

### 5. github_issues_list_for_repo
```
请求: GET /repos/facebook/react/issues?state=open&per_page=2
响应: [
  { "number": 36571, "title": "Bug:", "user": {...}, "state": "open", ... },
  ...
]
```

### 6. github_pulls_list_for_repo
```
请求: GET /repos/facebook/react/pulls?state=open&per_page=2
响应: [
  { "number": 36564, "title": "Fix Fizz...", "state": "open", ... },
  ...
]
```

### 7. github_orgs_get
```
请求: GET /orgs/github
响应: {
  "login": "github",
  "id": 9919,
  "url": "https://api.github.com/orgs/github",
  ...
}
```

### 8. github_teams_list
```
请求: GET /user/teams
响应: []  // 用户未加入任何团队
```

### 9. github_gists_list_for_user
```
请求: GET /users/caijiajia-sky/gists?per_page=2
响应: [
  { "id": "9586aab6e...", "description": null, "html_url": "...", ... },
  ...
]
```

### 10. github_rate_limit_get
```
响应: {
  "resources": {
    "core": { "limit": 5000, "used": 3, "remaining": 4997, "reset": 1780083845 },
    "search": { "limit": 30, "used": 1, "remaining": 29, "reset": 1780080365 },
    "graphql": { ... }
  }
}
```

### 11. github_search_users
```
请求: GET /search/users?q=developer&per_page=2
响应: {
  "total_count": 1661005,
  "items": [
    { "login": "developerrahulofficial", ... },
    ...
  ]
}
```

### 12. github_search_code
```
请求: GET /search/code?q=function+react+language:javascript&per_page=2
响应: {
  "total_count": 5034240,
  "items": [
    { "name": "14.js", "path": "14.js", "url": "...", ... },
    ...
  ]
}
```

---

## 速率限制信息

| 资源类型 | 限制 | 已用 | 剩余 | 重置时间 |
|----------|------|------|------|----------|
| core | 5000/小时 | 3 | 4997 | ~14小时后 |
| search | 30/分 | 1 | 29 | ~1分钟后 |

---

## 结论

✅ **所有测试通过 (12/12)**

GitHub MCP Skills 已成功创建并验证，可以正常使用所有核心功能。