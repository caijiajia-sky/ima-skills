---
name: minimax-voice-clone
description: 当用户请求克隆声音、上传音频创建自定义音色、voice_clone 等时触发。
---

# MiniMax Voice Clone Skill

## 触发条件

当用户请求以下操作时触发此 Skill：

- 克隆声音 / 上传音频克隆声音
- 创建自定义音色 / 上传音色样本
- voice_clone / 声音克隆 / 克隆音色
- 制作声音复刻 / 声音复刻模型

## 功能说明

此 Skill 用于调用 MiniMax API 实现声音克隆功能。用户上传音频文件（时长 10秒-5分钟，支持 mp3/m4a/wav 格式），系统将上传音频并克隆声音，返回自定义的 voice_id。

## 使用限制

- MiniMax Token Plan 用户可用
- 音频时长：10秒 - 5分钟
- 支持格式：mp3, m4a, wav
- 推荐采样率：16kHz 以上

## 输入要求

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| audio_file | string | 是 | 音频文件路径 |
| voice_id | string | 是 | 自定义音色ID（用于标识克隆的声音） |
| text | string | 否 | 测试文本（默认使用示例文本） |

## 输出结果

| 字段 | 类型 | 说明 |
|------|------|------|
| voice_id | string | 克隆后的音色ID |
| status | string | 操作状态 |

## API 配置

- API Host: `https://api.minimaxi.com`
- API Key: 已配置在环境变量中

## 调用流程

1. 上传音频文件到 `/v1/files/upload` 获取 file_id
2. 调用 `/v1/voice_clone` 接口克隆声音
3. 返回克隆后的 voice_id

## 示例

### 用户输入
```
上传音频 /Users/test/voice_sample.mp3，克隆声音，voice_id 为 my_voice_001
```

### 参数提取
- audio_file: `/Users/test/voice_sample.mp3`
- voice_id: `my_voice_001`
- text: （使用默认测试文本）

### 执行结果
```json
{
  "voice_id": "my_voice_001",
  "status": "success"
}
```

## 错误处理

| 错误码 | 说明 | 处理方式 |
|--------|------|----------|
| 400 | 音频格式不支持 | 提示用户使用 mp3/m4a/wav 格式 |
| 400 | 音频时长不符 | 提示用户控制音频时长在 10秒-5分钟 |
| 401 | API Key 无效 | 检查 API 配置 |
| 413 | 文件过大 | 压缩音频或分段处理 |
| 500 | 服务器错误 | 重试或联系技术支持 |