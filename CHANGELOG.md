# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

## [2026-06-04] - 第三轮复审

### 🔒 Security
- 修复8个SKILL.md文档中硬编码的MiniMax API Key
- 完善所有占位符为标准脱敏格式
- 重新生成完整的仓库安全审计

### ✨ Added
- 添加 LICENSE (MIT)
- 添加 .gitignore
- 添加 SECURITY.md
- 添加 CONTRIBUTING.md

## [2026-06-04] - 第二轮复审

### 🔒 Security
- 修复14个Python脚本硬编码的MiniMax API Key
- 修复2个Shell脚本硬编码的GitHub Token
- 修复多个文件的重复docstring和重复shebang
- 修复 README.md 中的敏感信息泄露

## [2026-06-04] - 第一轮复审

### ✨ Added
- 初始上传25个Skills
- 补传44个缺失文件
- 添加基础README

### 🐛 Fixed
- 修复 GitHub-mcp 脚本中的Token泄露
