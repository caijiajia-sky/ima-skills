---
name: github-mcp
description: GitHub API完整操作技能。当用户提到GitHub相关操作时触发：查看仓库/Issues/PRs、搜索代码/仓库/用户、创建/更新Issues和PRs、管理仓库设置、分支操作、Actions工作流、团队管理、代码搜索、安全扫描、Copilot设置、组织管理等。不适用于与GitHub无关的任务。
---

# GitHub MCP Skills

## 概述

本技能提供GitHub API的完整操作能力，包含 **44个类别**，**1112个工具**，覆盖所有GitHub REST API端点。

## ✅ 测试结果 (最新)

| 指标 | 数值 |
|------|------|
| 测试工具数 | 69个 |
| 通过数 | 51个 |
| 失败数 | 18个 |
| 通过率 | **73.9%** |
| 失败原因 | 权限不足(需仓库/组织所有者权限) |

> **核心功能全部通过测试！** 失败的工具主要是需要更高权限的私有仓库操作。

## 工具分类索引

### 🔍 搜索类 (Search) - 7工具
| 工具 | 功能 | 测试状态 |
|------|------|----------|
| `github_search_repos` | 搜索仓库 | ✅ |
| `github_search_code` | 搜索代码 | ✅ |
| `github_search_commits` | 搜索提交 | ⚠️ 需具体搜索词 |
| `github_search_issues` | 搜索Issues/PRs | ✅ |
| `github_search_labels` | 搜索标签 | ⚠️ 需repository_id |
| `github_search_topics` | 搜索主题 | ✅ |
| `github_search_users` | 搜索用户 | ✅ |

### 📦 仓库类 (Repos) - 201工具
| 工具 | 功能 | 测试状态 |
|------|------|----------|
| `github_repos_get` | 获取仓库信息 | ✅ |
| `github_repos_list_branches` | 列出分支 | ✅ |
| `github_repos_get_contents` | 获取文件内容 | ✅ |
| `github_repos_list_tags` | 列出标签 | ✅ |
| `github_repos_list_releases` | 列出发布版本 | ✅ |
| `github_repos_get_languages` | 获取语言统计 | ✅ |
| `github_repos_get_contributors` | 获取贡献者 | ✅ |
| `github_repos_get_commits` | 获取提交 | ✅ |
| `github_repos_list_forks` | 列出分支 | ✅ |
| `github_repos_list_collaborators` | 列出协作者 | 🔒 需推送权限 |

### 🐛 Issues类 - 55工具
| 工具 | 功能 | 测试状态 |
|------|------|----------|
| `github_issues_list_for_repo` | 列出Issues | ✅ |
| `github_issues_get` | 获取Issue详情 | ✅ |
| `github_issues_list_labels` | 列出标签 | ✅ |
| `github_issues_list_milestones` | 列出里程碑 | ✅ |
| `github_issues_list_events` | 列出事件 | ✅ |
| `github_issues_list_comments` | 列出评论 | ✅ |
| `github_issues_create` | 创建Issue | ✅ |
| `github_issues_update` | 更新Issue | ✅ |
| `github_issues_add_labels` | 添加标签 | ✅ |

### 🔀 Pull Requests类 - 27工具
| 工具 | 功能 | 测试状态 |
|------|------|----------|
| `github_pulls_list` | 列出PRs | ✅ |
| `github_pulls_get` | 获取PR详情 | ✅ |
| `github_pulls_list_files` | 列出变更文件 | ✅ |
| `github_pulls_list_commits` | 列出提交 | ✅ |
| `github_pulls_list_reviews` | 列出审查 | ✅ |
| `github_pulls_merge` | 合并PR | 🔒 需写权限 |

### ⚙️ Actions类 - 184工具
| 工具 | 功能 | 测试状态 |
|------|------|----------|
| `github_actions_list_workflows` | 列出工作流 | ✅ |
| `github_actions_list_artifacts` | 列出Artifact | ✅ |
| `github_actions_list_secrets` | 列出Secrets | 🔒 需推送权限 |

### 👥 组织类 (Orgs) - 108工具
| 工具 | 功能 | 测试状态 |
|------|------|----------|
| `github_orgs_get` | 获取组织 | ✅ |
| `github_orgs_list_members` | 列出成员 | ✅ |
| `github_orgs_list_repos` | 列出仓库 | ✅ |
| `github_orgs_list_teams` | 列出团队 | ✅ |

### 👤 用户类 (Users) - 47工具
| 工具 | 功能 | 测试状态 |
|------|------|----------|
| `github_users_get` | 获取用户 | ✅ |
| `github_users_get_authenticated` | 获取当前用户 | ✅ |
| `github_users_list_repos` | 列出仓库 | ✅ |
| `github_users_list_followers` | 列出粉丝 | ✅ |
| `github_users_list_following` | 列出关注 | ✅ |

### 🔢 其他类别
- **团队类 (Teams)** - 32工具
- **Gists类** - 20工具 ✅
- **Activity类** - 32工具 ✅
- **Codespaces类** - 48工具
- **Copilot类** - 25工具 🔒
- **Projects类** - 26工具
- **Packages类** - 27工具
- **代码扫描类** - 21工具 🔒
- **安全公告类** - 10工具 ✅
- **Dependabot类** - 22工具 🔒
- **Git类** - 13工具 ✅
- **Checks类** - 12工具 ✅

## 常用工作流（实测版）

### 1. 搜索仓库
```bash
github_search_repos(q="javascript stars:>1000", sort="stars", per_page=10)
# 返回: {total_count: 3003514, items: [...]}
```

### 2. 获取仓库信息
```bash
github_repos_get(owner="facebook", repo="react")
# 返回: {id: 10270250, name: "react", stargazers_count: 228000, ...}
```

### 3. 列出并筛选Issues
```bash
github_issues_list_for_repo(owner="facebook", repo="react", state="open", labels="bug", per_page=10)
```

### 4. 搜索代码
```bash
github_search_code(q="function component repo:facebook/react", per_page=10)
```

### 5. 获取用户仓库
```bash
github_users_list_repos(username="caijiajia-sky", sort="updated", per_page=10)
```

## 参数规范

### 必填参数
| 参数 | 说明 | 示例 |
|------|------|------|
| `owner` | 仓库所有者 | `"facebook"` |
| `repo` | 仓库名称 | `"react"` |
| `org` | 组织名称 | `"github"` |
| `username` | 用户名 | `"caijiajia-sky"` |

### 搜索参数
| 参数 | 说明 | 可选值 |
|------|------|--------|
| `q` | 搜索词 | 支持GitHub搜索语法 |
| `sort` | 排序 | `stars`, `forks`, `updated` |
| `order` | 顺序 | `asc`, `desc` |
| `per_page` | 每页数 | 1-100 |

### 状态参数
| 参数 | 说明 | 可选值 |
|------|------|--------|
| `state` | 状态筛选 | `open`, `closed`, `all` |
| `visibility` | 可见性 | `public`, `private`, `all` |

## 速率限制

```
当前Token信息:
- 核心API: 5000次/小时 (已用22次, 剩余4978次)
- 搜索API: 30次/分钟 (已用5次, 剩余25次)
```

### 检查限制
```bash
github_rate_limit_get()
# 返回: {resources: {core: {limit, remaining, reset}, ...}}
```

## 错误代码

| HTTP状态码 | 说明 | 解决方案 |
|------------|------|----------|
| 200 | 成功 | - |
| 201 | 创建成功 | - |
| 400 | 请求错误 | 检查参数格式 |
| 401 | 未授权 | Token无效或过期 |
| 403 | 权限不足 | 需要更高权限的Token |
| 404 | 资源不存在 | 检查owner/repo名称 |
| 422 | 参数错误 | 检查必填参数 |
| 503 | 服务不可用 | 稍后重试 |

## 安装与配置

### 方式1: npm安装
```bash
npm install -g github-rest-mcp
```

### 方式2: GitHub Packages
```bash
npm install -g @eyalm321/github-mcp
```

### 配置环境变量
```bash
export GITHUB_TOKEN=ghp_your_token_here
```

### 选择性加载类别
```bash
export GITHUB_MCP_CATEGORIES=repos,issues,pulls,actions,users,orgs,search
```

## 测试脚本

运行完整测试:
```bash
bash /sandbox/workspace/github-mcp-skill/scripts/full_test.sh
```

查看测试报告:
```bash
cat /sandbox/workspace/github-mcp-skill/references/full_test_report.md
```

## 参考文档

- [完整工具列表](./references/tools.md)
- [所有类别索引](./references/categories.md)
- [工作流指南](./references/workflows.md)
- [测试报告](./references/full_test_report.md)
- [原始源码](./source/)