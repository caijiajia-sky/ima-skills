# Contributing Guide

感谢您对 IMA Skills 项目的关注！

## 如何贡献

### 报告问题
- 使用 GitHub Issues 报告bug或建议
- 提供详细的复现步骤和环境信息

### 提交代码
1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 提交 Pull Request

### Skill贡献规范
- 每个Skill必须包含 `SKILL.md`（带YAML frontmatter）
- Python脚本不得硬编码任何密钥
- 遵循 PEP 8 代码风格
- 添加适当的注释和文档字符串

### 安全规范
- ❌ 禁止提交任何API Key、Token、密码
- ✅ 使用环境变量传递敏感信息
- ✅ 在 .gitignore 中排除敏感文件
