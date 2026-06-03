---
name: minimax-image-analysis
description: 当用户需要理解图像内容、描述图片、从图片中提取文字(OCR)、识别截图或分析视觉元素时说"分析图像"、"理解图片"、"提取图中文字"、"识别图片内容"、"描述这张图片"、"图片里有什么"时触发。
---

# MiniMax Vision Skill - 图片理解

## 功能

使用 MiniMax mmx CLI 的 vision describe 命令分析图片内容。

## 使用方法

### 基本用法

```bash
mmx --api-key "你的API密钥" vision describe --image <图片路径或URL> [--prompt "分析提示词"]
```

### 参数

| 参数 | 说明 |
|------|------|
| `--image` | 图片路径（本地）或 URL（网络） |
| `--file-id` | 预上传的文件 ID（跳过 base64 转换） |
| `--prompt` | 关于图片的问题（默认: "Describe the image."） |
| `--quiet` | 抑制非必要输出 |

### 示例

```bash
# 分析网络图片
mmx --api-key "sk-cp-xxx" vision describe --image "https://example.com/photo.jpg"

# 分析本地图片
mmx --api-key "sk-cp-xxx" vision describe --image "/path/to/photo.jpg"

# 带提示词分析
mmx --api-key "sk-cp-xxx" vision describe --image "https://example.com/dog.jpg" --prompt "这是什么品种的狗？"

# 提取图片中的文字
mmx --api-key "sk-cp-xxx" vision describe --image "screenshot.png" --prompt "提取图片中的所有文字"
```

## 输出格式

```json
{
  "content": "图片内容的详细描述...",
  "base_resp": {
    "status_code": 0,
    "status_msg": "success"
  }
}
```

## 支持的图片格式

- 本地文件: JPEG, PNG, WebP, GIF
- 网络 URL: 支持 HTTP/HTTPS

## API Key 配置

当前配置的密钥：`sk-cp-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

区域：cn (国内版)