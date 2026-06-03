---
name: minimax-music
description: 当用户请求生成音乐、创作音乐、帮我写首歌、制作背景音乐、music generation 等时触发。
---

# MiniMax Music Generation Skill

## 触发条件

当用户请求以下内容时触发本 Skill：
- 生成音乐 / 生成歌曲
- 创作音乐 / 写歌
- 音乐生成 / song generation
- 帮我写一首...的歌
- 创建背景音乐
- 制作音乐 / make music

## 功能说明

调用 MiniMax API 生成音乐，支持：
- 文本描述生成音乐（prompt）
- 自定义歌词
- 选择音乐风格
- 支持有歌词歌曲或纯音乐

## API 配置

- **API Host**: `https://api.minimaxi.com`
- **Endpoint**: `POST /v1/music_generation`
- **模型**: music-2.5 / music-2.6

## 输入参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| prompt | string | 是 | 音乐描述/灵感（英文效果更好） |
| model | string | 否 | 模型版本，默认 music-2.6 |
| lyrics | string | 否 | 歌词（JSON 格式或文本） |
| lyrics_type | string | 否 | "user" 或 "ai_generated" |
| instrumental | boolean | 否 | true=纯音乐，false=带歌词，默认 false |
| style | string | 否 | 音乐风格 |
| title | string | 否 | 歌曲标题 |

## 输出

返回任务 ID，需轮询查询任务状态或直接下载音频文件。

## 使用示例

```
用户: 帮我生成一首欢快的流行音乐
Skill: 调用音乐生成 API，返回生成的音频文件
```

## 执行脚本

`scripts/generate_music.py`

## 使用方法

```bash
python scripts/generate_music.py --prompt "描述" --lyrics "歌词" --output "output.mp3"
```

### 参数说明

| 参数 | 缩写 | 说明 |
|------|------|------|
| --prompt | -p | 音乐描述/灵感（必填，英文效果更好） |
| --model | -m | 模型版本，默认 music-2.6 |
| --lyrics | -l | 歌词 |
| --lyrics-type | - | lyrics_type: user/ai_generated |
| --instrumental | - | 生成纯音乐 |
| --style | -s | 音乐风格 |
| --title | -t | 歌曲标题 |
| --output | -o | 输出文件路径，默认 output.mp3 |