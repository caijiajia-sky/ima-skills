# GitHub MCP 常用工作流（实测版）

## 已验证工作流

以下工作流已通过实际API测试验证：

### 1. 获取当前用户信息 ✅
```javascript
// github_users_get_authenticated
GET /user
// 返回: {login: "caijiajia-sky", id: 264462328, ...}
```

### 2. 搜索仓库 ✅
```javascript
// github_search_repos
GET /search/repositories?q={keyword}&sort=stars&per_page=10
// 返回: {total_count: 3003509, items: [...]}
```

### 3. 获取仓库信息 ✅
```javascript
// github_repos_get
GET /repos/{owner}/{repo}
// 示例: facebook/react → {id: 10270250, name: "react", ...}
```

### 4. 列出仓库分支 ✅
```javascript
// github_repos_list_branches
GET /repos/{owner}/{repo}/branches?per_page=5
// 返回: [{name: "main", commit: {...}, protected: false}, ...]
```

### 5. 列出Issues ✅
```javascript
// github_issues_list_for_repo
GET /repos/{owner}/{repo}/issues?state=open&per_page=10
// 返回: [{url, number, title, user, state, labels, ...}, ...]
```

### 6. 列出Pull Requests ✅
```javascript
// github_pulls_list_for_repo
GET /repos/{owner}/{repo}/pulls?state=open&per_page=10
// 返回: [{url, number, title, state, user, draft, ...}, ...]
```

### 7. 获取组织信息 ✅
```javascript
// github_orgs_get
GET /orgs/{org}
// 示例: github → {login: "github", id: 9919, ...}
```

### 8. 列出用户Gists ✅
```javascript
// github_gists_list_for_user
GET /users/{username}/gists?per_page=10
// 返回: [{url, id, description, html_url, ...}, ...]
```

### 9. 检查速率限制 ✅
```javascript
// github_rate_limit_get
GET /rate_limit
// 返回: {resources: {core: {limit: 5000, used: 3, remaining: 4997}, ...}}
```

### 10. 搜索用户 ✅
```javascript
// github_search_users
GET /search/users?q={keyword}&per_page=10
// 返回: {total_count: 1661005, items: [{login, avatar_url, ...}, ...]}
```

### 11. 搜索代码 ✅
```javascript
// github_search_code
GET /search/code?q={keyword}&per_page=10
// 返回: {total_count: 5034240, items: [{name, path, url, ...}, ...]}
```

## 创建类工作流

### 创建Issue
```
1. 确认仓库信息 (owner, repo)
2. POST /repos/{owner}/{repo}/issues
   {
     "title": "Bug: xxx",
     "body": "详细描述",
     "labels": ["bug", "help wanted"],
     "assignees": ["username"]
   }
3. 返回: {url, number, id, ...}
```

### 创建Pull Request
```
1. POST /repos/{owner}/{repo}/pulls
   {
     "title": "feat: 新功能",
     "head": "feature-branch",
     "base": "main",
     "body": "PR描述"
   }
2. 返回: {url, number, state, ...}
```

### 创建Release
```
1. POST /repos/{owner}/{repo}/releases
   {
     "tag_name": "v1.0.0",
     "name": "Version 1.0.0",
     "body": "Release notes",
     "draft": false,
     "prerelease": false
   }
```

## 修改类工作流

### 更新Issue
```
1. PATCH /repos/{owner}/{repo}/issues/{issue_number}
   {
     "title": "新标题",
     "body": "新内容",
     "state": "closed",
     "labels": ["enhancement"]
   }
```

### 更新仓库设置
```
1. PATCH /repos/{owner}/{repo}
   {
     "name": "new-repo-name",
     "description": "新描述",
     "default_branch": "main",
     "private": true
   }
```

## 批量操作工作流

### 获取多个仓库信息
```javascript
const repos = [
  {owner: "facebook", repo: "react"},
  {owner: "facebook", repo: "react-native"},
  {owner: "facebook", repo: "jest"}
];

for (const {owner, repo} of repos) {
  const data = await github_repos_get({owner, repo});
  console.log(`${data.full_name}: ${data.stargazers_count} stars`);
}
```

### 搜索并筛选仓库
```javascript
// 搜索Star数>1000的JavaScript项目
github_search_repos({
  q: "language:javascript stars:>1000",
  sort: "stars",
  order: "desc",
  per_page: 20
})
```

### 列出仓库所有开放Issues和PRs
```javascript
const issues = await github_issues_list_for_repo({
  owner, repo, 
  state: "open", 
  per_page: 100
});

const pulls = await github_pulls_list_for_repo({
  owner, repo,
  state: "open",
  per_page: 100
});

console.log(`开放Issues: ${issues.length}`);
console.log(`开放PRs: ${pulls.length}`);
```

## 条件分支工作流

### 根据仓库大小处理
```
IF repo.size < 1000:
  → 获取完整信息
ELIF repo.size < 10000:
  → 仅获取基本信息
ELSE:
  → 提示仓库太大，建议使用分页
```

### 根据PR状态处理
```
IF pr.state === "open":
  → 检查是否有冲突
  → 列出待审查文件
ELIF pr.state === "closed":
  → 检查是否已合并
  → 列出合并信息
```

## 速率限制处理
```javascript
const limit = await github_rate_limit_get();
const remaining = limit.resources.core.remaining;
const reset = new Date(limit.resources.core.reset * 1000);

if (remaining < 100) {
  console.log(`速率限制警告: 剩余${remaining}次请求`);
  console.log(`限制重置时间: ${reset.toLocaleString()}`);
  // 等待或减少请求
}
```

## 错误处理模式
```javascript
try {
  const result = await github_repos_get({owner, repo});
  return result;
} catch (error) {
  switch(error.status) {
    case 404:
      return {error: "仓库不存在"};
    case 403:
      return {error: "权限不足"};
    case 422:
      return {error: "参数错误"};
    default:
      return {error: "未知错误"};
  }
}
```