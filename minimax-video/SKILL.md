---
name: minimax-video
description: 当用户请求生成视频、创建视频、帮我生成一段视频、video generation 等时触发。
---

# MiniMax Video Skill - 视频生成

## 功能

使用 MiniMax mmx CLI 的 video generate 命令生成视频。

## 使用方法

### 基本用法

```bash
# 标准版（文生视频）
mmx --api-key "sk-cp-xxx" video generate --prompt "视频描述" [--download output.mp4]

# Fast版（图生视频，需要首帧图片）
mmx --api-key "sk-cp-xxx" video generate --prompt "描述" --first-frame image.jpg --model "MiniMax-Hailuo-2.3-Fast-6s-768p"
```

### 参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--prompt` | 视频描述文本 | 必需 |
| `--model` | 模型: MiniMax-Hailuo-2.3, Hailuo-2.3-Fast 等 | MiniMax-Hailuo-2.3 |
| `--first-frame` | 起始帧图片（本地路径或 URL） | - |
| `--last-frame` | 结束帧图片（需 --first-frame，启用 SEF 模式） | - |
| `--subject-image` | 主体参考图（用于人物一致性，S2V-01 模型） | - |
| `--callback-url` | 完成通知的 Webhook URL | - |
| `--download` | 完成时保存视频到文件 | - |
| `--no-wait` | 立即返回任务 ID，不等待 | - |
| `--async` | 异步模式，立即返回任务 ID | - |
| `--poll-interval` | 轮询间隔（秒） | 5 |

## 四种视频生成模式

| 模式 | 模型 | 特点 | 是否需要首帧 |
|------|------|------|-------------|
| **标准版** | `MiniMax-Hailuo-2.3` | 高质量视频 | ❌ 不需要 |
| **Fast版** | `MiniMax-Hailuo-2.3-Fast` | 快速生成 | ✅ 需要 `--first-frame` |
| **首尾帧版** | `Hailuo-02` | 首尾帧插值 | ✅ 需要 `--first-frame` + `--last-frame` |
| **主体参考版** | `S2V-01` | 人物一致性 | ✅ 需要 `--subject-image` |

### 用量说明

- **标准版**：每日 3 次额度（768P / 6s）
- **Fast版**：每日 3 次额度（768P / 6s）

> 💡 **提示**：如果标准版额度用完，可使用 Fast 版（需要提供首帧图片）

```bash
# ============================================
# 模式一：标准版（文生视频，不需要首帧）
# ============================================
mmx --api-key "sk-cp-xxx" video generate --prompt "一只猫在草地上玩耍" --download cat.mp4

# ============================================
# 模式二：Fast版（图生视频，必须有首帧）
# ============================================
mmx --api-key "sk-cp-xxx" video generate \
  --prompt "镜头缓缓推进" \
  --first-frame start.jpg \
  --model "MiniMax-Hailuo-2.3-Fast-6s-768p" \
  --download fast_video.mp4

# ============================================
# 模式三：首尾帧插值（Hailuo-02）
# ============================================
mmx --api-key "sk-cp-xxx" video generate \
  --prompt "人物行走" \
  --first-frame start.jpg \
  --last-frame end.jpg \
  --download interp_video.mp4

# ============================================
# 模式四：主体参考（人物一致性，S2V-01）
# ============================================
mmx --api-key "sk-cp-xxx" video generate \
  --prompt "侦探在街头行走" \
  --subject-image character.jpg \
  --download consistent_video.mp4
```

## API Key 配置

当前配置的密钥：`sk-cp-BC0OPAa8Y5HiiKOIHZpC4WRiBF3PEeGXDl2WgAaG7mRI7WHsGXhMdQWXErRKZvrNu6gH_iH-tTMjQsozFC_akhP9VOPJSxh1gMzb-P2KchmzTXBRGjZWBbY`

区域：cn (国内版)