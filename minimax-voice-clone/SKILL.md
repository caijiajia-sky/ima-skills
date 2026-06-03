---
name: minimax-voice-clone
description: 当用户请求克隆声音、上传音频创建自定义音色、voice_clone 等时触发。
---

# MiniMax Voice Clone Skill - 声音克隆

## 功能

通过 MiniMax API 上传音频并克隆声音，创建自定义音色。

## 使用方法

### 基本用法

```bash
python scripts/clone_voice.py --audio-file /path/to/audio.mp3 --voice-id "my_voice"
```

### 参数

| 参数 | 说明 |
|------|------|
| `--audio-file` | 音频文件路径（mp3/m4a/wav） |
| `--voice-id` | 自定义音色 ID |
| `--text` | 测试文本（可选） |
| `--api-key` | API 密钥（可选，默认使用配置） |

### 示例

```bash
# 克隆声音
python scripts/clone_voice.py --audio-file sample.mp3 --voice-id "my_custom_voice"

# 带测试文本
python scripts/clone_voice.py --audio-file sample.mp3 --voice-id "my_voice" --text "测试克隆效果"
```

## 使用限制

- 音频时长：10秒 - 5分钟
- 支持格式：mp3, m4a, wav
- 推荐采样率：16kHz 以上

## 脚本说明

`scripts/clone_voice.py` 完成以下步骤：
1. 上传音频文件到 `/v1/files/upload` 获取 file_id
2. 调用 `/v1/voice_clone` 接口克隆声音
3. 返回克隆后的 voice_id

## 输出示例

```json
{
  "voice_id": "my_custom_voice",
  "status": "success"
}
```

## API Key 配置

当前配置的密钥：`sk-cp-BC0OPAa8Y5HiiKOIHZpC4WRiBF3PEeGXDl2WgAaG7mRI7WHsGXhMdQWXErRKZvrNu6gH_iH-tTMjQsozFC_akhP9VOPJSxh1gMzb-P2KchmzTXBRGjZWBbY`

区域：cn (国内版)