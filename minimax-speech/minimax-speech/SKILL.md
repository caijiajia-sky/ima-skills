---
name: minimax-speech
description: 当用户需要将文字转为语音、生成音频文件、语音合成、text to speech、TTS，或说"把这段文字转成语音"、"生成一个音频"、"读一下这段文字"时触发。
---

# MiniMax Text-to-Speech Skill - 语音合成

## 触发条件

当用户请求以下操作时触发此 Skill：

- 文字转语音
- 文本朗读
- 生成音频
- 语音合成
- 将文本转换为语音
- convert to speech / generate audio / read this text

## 功能描述

使用 MiniMax Token Plan API 将文本转换为自然语音，支持多种声音和参数调节。

## 使用方法

### 基本用法

```bash
# 基础语音合成
python scripts/tts.py "欢迎使用 MiniMax 语音合成功能"

# 指定声音和语速
python scripts/tts.py "第一章：故事的開始" --voice female-yujie --speed 1.0

# 完整参数示例
python scripts/tts.py "这是一段测试文本" --voice male-jieshuo --speed 1.2 --vol 8 --pitch 1.0 --output speech.mp3
```

### 命令行参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| 位置参数 | 要转换的文本 | - |
| `-v`, `--voice` | 声音 ID | female-tianmei |
| `-s`, `--speed` | 语速 (0.5-2.0) | 1.0 |
| `--vol` | 音量 (0-10) | 5 |
| `-p`, `--pitch` | 音调 (0.5-2.0) | 1.0 |
| `-o`, `--output` | 输出文件路径 | speech_{timestamp}.mp3 |
| `-h`, `--help` | 显示帮助 | - |

### Python API

```python
from scripts.tts import text_to_speech_sync, text_to_speech_async, wait_for_async_task

# 短文本（≤500字符）使用同步接口
audio = text_to_speech_sync("欢迎使用语音合成", voice_id="female-tianmei", speed=1.0)

# 长文本使用异步接口
task_id = text_to_speech_async("这是一段很长的文本..." * 100, voice_id="male-jieshuo")
audio = wait_for_async_task(task_id)

# 保存文件
with open("output.mp3", "wb") as f:
    f.write(audio)
```

## 接口选择

| 接口类型 | 适用场景 | 字符限制 |
|----------|----------|----------|
| 同步接口 | 短文本 | ≤500 字符 |
| 异步接口 | 长文本 | ≤100,000 字符 |

系统会自动选择合适的接口，也支持手动指定。

## 常用声音

| 声音 ID | 说明 | 适用场景 |
|---------|------|----------|
| female-tianmei | 甜美女声 | 日常对话、提示音 |
| female-yujie | 成熟女声 | 讲故事、朗读 |
| female-shaonv | 少女声 | 年轻角色、活泼场景 |
| male-qn-qingse | 青年男声 | 男性角色 |
| male-jieshuo | 主持人男声 | 旁白、播报 |

## 参数说明

### 语速 (speed)
- 范围: 0.5 - 2.0
- 1.0 为正常语速
- 小于 1.0 减慢，大于 1.0 加快

### 音调 (pitch)
- 范围: 0.5 - 2.0
- 1.0 为正常音调
- 小于 1.0 降低，大于 1.0 升高

### 音量 (vol)
- 范围: 0 - 10
- 5 为正常音量

## 示例输出

```
🔊 正在生成语音...
   文本: 欢迎使用 MiniMax 语音合成功能
   声音: female-tianmei
   语速: 1.0

📡 使用同步接口...

✅ 语音已保存: speech_1710000000.mp3
   文件大小: 45.2 KB
```

## 注意事项

- 默认输出格式为 MP3
- 异步任务最长等待 300 秒
- 异步任务每 5 秒查询一次状态
- 详见 `voices.md` 获取完整声音列表