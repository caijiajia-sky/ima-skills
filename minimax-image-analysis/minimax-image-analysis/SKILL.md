---
name: minimax-image-analysis
description: 当用户需要理解图像内容、描述图片、从图片中提取文字(OCR)、识别截图或分析视觉元素时说"分析图像"、"理解图片"、"提取图中文字"、"识别图片内容"、"描述这张图片"、"图片里有什么"时触发。
---

# MiniMax Image Analysis Skill - 图片分析

## 触发条件

当用户请求以下操作时触发此 Skill：

- 分析图片
- 描述这张图片
- 图片内容理解
- 从图片中提取文字
- OCR 识别
- 图片里有什么
- 这张图展示了什么
- analyze image / describe this picture / extract text from image

## 功能描述

使用 MiniMax Token Plan VLM API 对图片进行理解和分析，支持本地文件和 URL 图片输入。

## 使用方法

### 基本用法

```bash
# 分析本地图片
python scripts/analyze.py "photo.jpg" "描述图片内容"

# 分析网络图片
python scripts/analyze.py "https://example.com/image.jpg"

# 分析本地图片（使用默认提示词）
python scripts/analyze.py "screenshot.png"
```

### 命令行参数

| 参数 | 说明 |
|------|------|
| 位置参数1 | 图片路径或 URL |
| 位置参数2 | 分析提示词（可选，默认"描述这张图片的内容"） |
| `-i`, `--image` | 图片路径或 URL |
| `-p`, `--prompt` | 分析提示词 |
| `-h`, `--help` | 显示帮助 |

### Python API

```python
from scripts.analyze import analyze_image

# 分析本地图片
result = analyze_image("photo.jpg", "这张图片有什么特点？")

# 分析网络图片
result = analyze_image("https://example.com/image.jpg", "提取图片中的文字")

print(result)
```

## 输入输出

### 输入
- **图片源**: 本地文件路径或网络 URL
- **提示词**: 分析指令（可选）

### 输出
- **分析结果**: 图片内容的文字描述

## 支持的图片格式

- JPEG (.jpg, .jpeg)
- PNG (.png)
- WebP (.webp)
- GIF (.gif)

### 图片大小限制
- 最大 10MB

## 示例输出

```
📋 分析结果:
--------------------------------------------------
这张图片展示了一只可爱的橘色猫咪正坐在窗台上，
阳光从窗户照进来，猫咪正在悠闲地晒太阳。
图片整体氛围温馨，色调偏暖色系。
```

## 注意事项

- 如果提供的是本地文件，脚本会自动转换为 base64 data URL
- 如果提供的是 URL，脚本会先下载图片再转换
- API 请求超时时间为 120 秒
- 网络图片下载超时时间为 30 秒