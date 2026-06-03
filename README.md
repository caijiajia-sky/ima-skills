# IMA Skills 技能库

> 这是我在 IMA Copilot 平台上使用的所有 Skills 集合。  
> 📅 最后更新：2026-06-04 | ✅ 25个Skill全部完整上传

## 🔒 安全声明

**所有上传到此仓库的代码已通过安全审计：**

### ✅ 已修复的安全问题
1. **MiniMax API Key 泄露** (14个Python脚本)
   - 原状态: 硬编码 MiniMax API Key (sk-cp- 开头, ~120字符)
   - 修复方案: 改为 `os.environ.get("MINIMAX_API_KEY", "your_api_key_here")`
   - 修复时间: 2026-06-04

2. **GitHub Token 泄露** (2个Shell脚本)
   - 原状态: 硬编码 GitHub Personal Access Token (ghp_ 开头, 40字符)
   - 修复方案: 改为 `${GITHUB_TOKEN:-your_github_token_here}`
   - 修复时间: 2026-06-04

### 🔐 当前安全状态
- ✅ 0个硬编码API Key
- ✅ 0个硬编码GitHub Token
- ✅ 0个密码/私钥泄露
- ✅ 所有脚本使用环境变量传递敏感信息

### 📝 使用方法
```bash
# 设置环境变量
export MINIMAX_API_KEY=your_actual_key
export GITHUB_TOKEN=your_github_token

# 或创建 .env 文件（不要提交到git）
echo "MINIMAX_API_KEY=your_key" > .env
```

---

## 📦 技能列表 (25个)

### 🚀 AI创作类
| Skill | 描述 |
|-------|------|
| `ai-comic-creator` | AI漫画创作全流程 - 从选题到批量发布 |
| `explosive-cover-generator-gzh` | 公众号爆款封面设计 |
| `minimax-image` | MiniMax 图片生成 |
| `minimax-image-analysis` | 图片内容分析与OCR |
| `minimax-music` | AI音乐生成 |
| `minimax-video` | AI视频生成 |
| `minimax-voice-clone` | 声音克隆 |

### 📱 公众号运营
| Skill | 描述 |
|-------|------|
| `wechat-account-setup` | 公众号账号接入与配置 |
| `wechat-article-publisher` | 公众号文章排版与发布 |

### 📊 内容创作
| Skill | 描述 |
|-------|------|
| `ima-ppt` | PPT演示文稿创建与编辑 |
| `ima-report` | 研究报告生成 |
| `knowledge-structure` | 知识结构化封装 |
| `信息收集与整理v3.0` | 信息收集与整理 |

### 🔧 平台工具
| Skill | 描述 |
|-------|------|
| `github-mcp` | GitHub API 完整操作 (1112个工具) |
| `bocha-search` | 博查AI搜索 |
| `ima-knowledge` | 知识库管理 |
| `ima-note` | 笔记管理 |
| `ima-skill-creator` | Skill创建与优化 |
| `task-calibration` | 任务执行校准 |

### 🎓 AI技能进化
| Skill | 描述 |
|-------|------|
| `skill-adversarial-validation` | AI-Skill对抗性验证 |
| `skill-external-distillation` | AI-Skill外部知识蒸馏 |

### 🧠 专业能力
| Skill | 描述 |
|-------|------|
| `minimax-speech` | 文字转语音 |
| `minimax-token-plan` | MiniMax API调用 |
| `minimax-usage` | 额度查询 |
| `huadu-pangu` | 盘古技能框架 |

## 📊 上传统计

| 指标 | 数值 |
|------|------|
| Skill总数 | 25 |
| 上传文件数 | 201 |
| 完整性 | 100% ✅ |
| 安全审计 | 通过 ✅ |
| 敏感信息泄露 | 0 |

## 🔧 使用方法

```bash
# 克隆仓库
git clone https://github.com/caijiajia-sky/ima-skills.git

# 设置环境变量（重要！）
export MINIMAX_API_KEY=your_actual_key
export GITHUB_TOKEN=your_github_token

# 查看各Skill
cd ima-skills/<skill-name>
cat SKILL.md
```

## 📁 目录结构

```
ima-skills/
├── README.md
├── ai-comic-creator/          # AI漫画创作 (22个文件)
├── bocha-search/              # AI搜索
├── explosive-cover-generator-gzh/  # 爆款封面
├── github-mcp/                # GitHub操作 (99个文件)
├── huadu-pangu/              # 盘古技能
├── ima-knowledge/             # 知识库管理
├── ima-note/                  # 笔记管理
├── ima-ppt/                   # PPT制作
├── ima-report/                # 报告生成
├── ima-skill-creator/         # Skill创建
├── knowledge-structure/       # 知识结构化
├── minimax-image/             # 图片生成
├── minimax-image-analysis/    # 图片分析
├── minimax-music/             # 音乐生成
├── minimax-speech/            # 语音合成
├── minimax-token-plan/        # API调用
├── minimax-usage/             # 额度查询
├── minimax-video/             # 视频生成
├── minimax-voice-clone/       # 声音克隆
├── skill-adversarial-validation/  # 对抗性验证
├── skill-external-distillation/   # 知识蒸馏
├── task-calibration/          # 任务校准
├── wechat-account-setup/     # 公众号配置
├── wechat-article-publisher/  # 文章发布
└── 信息收集与整理v3.0/        # 信息收集
```

## 📝 复审记录

### 2026-06-04 第一次复审
- ✅ 初始上传: 25个SKILL.md
- ⚠️ 发现: 12个Skill存在文件缺失
- ✅ 补传: 44个文件
- ✅ 最终: 100%完整

### 2026-06-04 第二次复审（深度）
- ⚠️ **严重发现**: 14个Python脚本硬编码 MiniMax API Key
- ✅ 修复: 全部改为 `os.environ.get("MINIMAX_API_KEY", ...)` 方式
- ✅ 验证: GitHub仓库已无硬编码密钥
- ✅ 提升: README安全声明更新

### 🔍 复审方法
1. 文件级SHA256哈希对比
2. GitHub代码搜索API深度扫描
3. 下载所有.py/.sh文件进行本地正则匹配
4. AST语法分析检查Python代码结构

---
**创建时间**: 2026-06-04  
**最后更新**: 2026-06-04 04:23  
**作者**: caijiajia-sky  
**License**: MIT
