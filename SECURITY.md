# Security Policy

## Supported Versions

| Version | Supported          |
|---------|--------------------|
| Latest  | :white_check_mark: |

## Reporting a Vulnerability

如果您发现安全漏洞，请通过以下方式报告：

1. **不要在公开Issue中披露**
2. 发送邮件到项目维护者
3. 或使用 GitHub Security Advisories 私下报告

我们会在48小时内响应。

## Security Best Practices

### 🔐 API Key管理
所有API Key必须通过环境变量传入：
```bash
export MINIMAX_API_KEY=your_key_here
export GITHUB_TOKEN=ghp_your_token_here
```

### ⚠️ 已修复的安全问题
- 2026-06-04: 14个Python脚本硬编码 MiniMax API Key (已修复)
- 2026-06-04: 2个Shell脚本硬编码 GitHub Token (已修复)
- 2026-06-04: 8个SKILL.md文档中包含完整API Key (已修复)

### 📋 安全审计历史
请查看 [README.md](./README.md) 中的"复审记录"部分。
