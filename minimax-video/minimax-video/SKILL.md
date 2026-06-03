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
mmx --api-key "你的API密钥" video generate --prompt "视频描述" [--download output.mp4]
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

### 示例

```bash
# 文生视频
mmx --api-key "sk-cp-xxx" video generate --prompt "一只猫在草地上玩耍" --download cat.mp4

# 图生视频（需要首帧图片）
mmx --api-key "sk-cp-xxx" video generate --prompt "镜头向前推进" --first-frame start.jpg --download video.mp4

# 首尾帧插值（使用 Hailuo-02 模型）
mmx --api-key "sk-cp-xxx" video generate --prompt "人物行走" --first-frame start.jpg --last-frame end.jpg

# 主体参考（人物一致性，S2V-01 模型）
mmx --api-key "sk-cp-xxx" video generate --prompt "侦探在街头行走" --subject-image character.jpg

# 异步模式（不等待完成）
mmx --api-key "sk-cp-xxx" video generate --prompt "海浪日落" --async --quiet

# 查看任务状态
mmx --api-key "sk-cp-xxx" video task get <task_id>
```

## 视频模型

| 模型 | 说明 | 场景 |
|------|------|------|
| MiniMax-Hailuo-2.3 | 标准文生视频 | 默认 |
| MiniMax-Hailuo-2.3-Fast | 快速模式 | 需要 --first-frame |
| Hailuo-02 | 首尾帧插值 | 需要 --first-frame + --last-frame |
| S2V-01 | 主体一致性 | 需要 --subject-image |

## 输出示例

```json
{
  "task_id": "abc123",
  "status": "pending"
}
```

## 注意事项

- 视频生成需要等待（轮询任务状态）
- 使用 `--no-wait` 或 `--async` 可立即返回任务 ID
- 每日用量限制: 标准版 3 次，Fast 版 3 次
- 截止时间: 2026-05-31 00:00:00

## API Key 配置

当前配置的密钥：`sk-cp-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

区域：cn (国内版)