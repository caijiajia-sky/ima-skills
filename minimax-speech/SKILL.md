---
name: minimax-speech
description: 当用户需要将文字转为语音、生成音频文件、语音合成、text to speech、TTS，或说"把这段文字转成语音"、"生成一个音频"、"读一下这段文字"时触发。
---

# MiniMax Speech Skill - 语音合成

## 功能

使用 MiniMax mmx CLI 的 speech synthesize 命令将文字转为语音。

## 使用方法

### 基本用法

```bash
mmx --api-key "你的API密钥" speech synthesize --text "要转换的文字" [--out output.mp3]
```

### 参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--text` | 要合成的文本 | 必需 |
| `--text-file` | 从文件读取文本（用 - 表示 stdin） | - |
| `--model` | 模型: speech-2.8-hd, speech-2.6, speech-02 | speech-2.8-hd |
| `--voice` | 音色 ID | English_expressive_narrator |
| `--speed` | 语速倍数 | 1.0 |
| `--volume` | 音量 | 1.0 |
| `--pitch` | 音调调整 | 0 |
| `--format` | 音频格式: mp3, pcm, flac, wav | mp3 |
| `--sample-rate` | 采样率 | 32000 |
| `--bitrate` | 比特率 | 128000 |
| `--channels` | 声道数 | 1 |
| `--language` | 语言代码 | - |
| `--subtitles` | 包含字幕时间数据 | - |
| `--pronunciation` | 自定义发音 (repeatable) | - |
| `--out` | 保存音频到文件 | - |
| `--stream` | 流式输出到 stdout | - |

### 示例

```bash
# 基础语音合成
mmx --api-key "sk-cp-xxx" speech synthesize --text "你好，欢迎使用 MiniMax"

# 保存到文件
mmx --api-key "sk-cp-xxx" speech synthesize --text "你好" --out hello.mp3

# 指定音色
mmx --api-key "sk-cp-xxx" speech synthesize --text "新闻播报" --voice "news_anchor" --out news.mp3

# 调整语速
mmx --api-key "sk-cp-xxx" speech synthesize --text "快速播报" --speed 1.5 --out fast.mp3

# 生成字幕
mmx --api-key "sk-cp-xxx" speech synthesize --text "Hello world" --subtitles --out hello.mp3

# 从文件读取
mmx --api-key "sk-cp-xxx" speech synthesize --text-file script.txt --out audio.mp3

# 管道输入
echo "Reading from stdin" | mmx --api-key "sk-cp-xxx" speech synthesize --text-file - --out stdin.mp3

# 流式输出
mmx --api-key "sk-cp-xxx" speech synthesize --text "Stream audio" --stream | mpv --no-terminal -
```

## 可用音色

```bash
# 查看所有可用音色
mmx --api-key "sk-cp-xxx" speech voices
```

## 输出示例

```json
{
  "saved": "/path/to/output.mp3",
  "duration_ms": 3456,
  "size_bytes": 57012,
  "sample_rate": 32000
}
```

## API Key 配置

当前配置的密钥：`sk-cp-BC0OPAa8Y5HiiKOIHZpC4WRiBF3PEeGXDl2WgAaG7mRI7WHsGXhMdQWXErRKZvrNu6gH_iH-tTMjQsozFC_akhP9VOPJSxh1gMzb-P2KchmzTXBRGjZWBbY`

区域：cn (国内版)