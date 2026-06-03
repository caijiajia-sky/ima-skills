---
name: minimax-music
description: 当用户请求生成音乐、创作音乐、帮我写首歌、制作背景音乐、music generation 等时触发。
---

# MiniMax Music Skill - 音乐生成

## 功能

使用 MiniMax mmx CLI 的 music generate 命令创作音乐。

## 使用方法

### 基本用法

```bash
mmx --api-key "你的API密钥" music generate --prompt "音乐风格描述" [--lyrics "歌词"] [--out output.mp3]
```

### 参数

| 参数 | 说明 |
|------|------|
| `--prompt` | 音乐风格描述（最多 2000 字符） |
| `--lyrics` | 带结构标签的歌词 |
| `--lyrics-file` | 从文件读取歌词 |
| `--lyrics-optimizer` | 自动从提示词生成歌词（不能与 --lyrics 或 --instrumental 共用） |
| `--instrumental` | 生成纯音乐（无人声） |
| `--vocals` | 人声风格，如 "warm male baritone" |
| `--genre` | 音乐风格，如 folk, pop, jazz, electronic |
| `--mood` | 情绪，如 warm, melancholic, uplifting |
| `--instruments` | 乐器，如 "acoustic guitar, piano, strings" |
| `--tempo` | 节奏描述，如 fast, slow, moderate |
| `--bpm` | 精确 BPM |
| `--key` | 音调，如 C major, A minor |
| `--model` | 模型: music-2.6, music-2.5+, music-2.5 |
| `--format` | 音频格式: mp3, wav, pcm |
| `--out` | 保存音频到文件 |

### 歌词结构标签

```
[Intro], [Verse], [Pre Chorus], [Chorus], [Interlude], [Bridge], 
[Outro], [Post Chorus], [Transition], [Break], [Hook], [Build Up], 
[Inst], [Solo]
```

注意：标签内不要放描述文字（会被唱出来）

### 示例

```bash
# 纯音乐生成
mmx --api-key "sk-cp-xxx" music generate --prompt "电影配乐，紧张悬疑" --instrumental --out bgm.mp3

# 自动生成歌词
mmx --api-key "sk-cp-xxx" music generate --prompt "欢快的流行音乐，关于夏天" --lyrics-optimizer --out summer.mp3

# 带歌词的歌曲
mmx --api-key "sk-cp-xxx" music generate --prompt "抒情的民谣" \
  --lyrics "[Verse]月光洒在窗台上..." \
  --out song.mp3

# 详细参数
mmx --api-key "sk-cp-xxx" music generate --prompt "温暖爵士" \
  --vocals "female jazz singer, smoky tone" \
  --instruments "piano, double bass, brushes" \
  --bpm 90 \
  --out jazz.mp3

# 从文件读取歌词
mmx --api-key "sk-cp-xxx" music generate --prompt "独立民谣" --lyrics-file song.txt --out indie.mp3

# 指定模型
mmx --api-key "sk-cp-xxx" music generate --prompt "电子舞曲" --model "music-2.5+" --out edm.mp3
```

## 输出示例

```json
{
  "saved": "/path/to/song.mp3"
}
```

## API Key 配置

当前配置的密钥：`sk-cp-BC0OPAa8Y5HiiKOIHZpC4WRiBF3PEeGXDl2WgAaG7mRI7WHsGXhMdQWXErRKZvrNu6gH_iH-tTMjQsozFC_akhP9VOPJSxh1gMzb-P2KchmzTXBRGjZWBbY`

区域：cn (国内版)