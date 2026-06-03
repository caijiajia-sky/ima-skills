---
name: minimax-image
description: 使用 MiniMax image-01 生图，当用户说"生成图片"、"创建图片"、"画一张图"、"文生图"、"generate an image"、"create a picture"时触发。
---

# MiniMax Image Generation Skill - 文生图

## 功能

使用 MiniMax mmx CLI 的 image generate 命令生成高质量图片。

## 使用方法

### 基本用法

```bash
mmx --api-key "你的API密钥" image generate --prompt "图片描述" [--aspect-ratio 16:9] [--n 2] [--out-dir ./output]
```

### 参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--prompt` | 图片描述文本 | 必需 |
| `--aspect-ratio` | 宽高比 (如 16:9, 1:1) | 1:1 |
| `--n` | 生成数量 (1-9) | 1 |
| `--width` | 自定义宽度 (512-2048, 8的倍数) | - |
| `--height` | 自定义高度 (512-2048, 8的倍数) | - |
| `--prompt-optimizer` | 自动优化提示词 | - |
| `--aigc-watermark` | 添加AI生成水印 | - |
| `--out` | 保存到指定文件路径 | - |
| `--out-dir` | 下载到目录 | - |
| `--out-prefix` | 文件名前缀 | image |
| `--response-format` | 响应格式: url, base64 | url |

### 示例

```bash
# 生成单张图片
mmx --api-key "sk-cp-xxx" image generate --prompt "一只可爱的猫咪在草地上"

# 生成多张图片
mmx --api-key "sk-cp-xxx" image generate --prompt "未来城市天际线" --n 3

# 指定宽高比
mmx --api-key "sk-cp-xxx" image generate --prompt "山水风景" --aspect-ratio 16:9

# 保存到指定目录
mmx --api-key "sk-cp-xxx" image generate --prompt "科技感头像" --out-dir ./images --out-prefix my_avatar

# 自定义尺寸
mmx --api-key "sk-cp-xxx" image generate --prompt "宽幅风景" --width 1920 --height 1080

# 优化提示词 + 水印
mmx --api-key "sk-cp-xxx" image generate --prompt "日落" --prompt-optimizer --aigc-watermark
```

## 支持的宽高比

| 比例 | 适用场景 |
|------|----------|
| 1:1 | 社交媒体头像、正方形 |
| 16:9 | 横版图片、桌面壁纸 |
| 9:16 | 竖版图片、手机壁纸 |
| 4:3 | 经典照片 |
| 3:4 | 竖版人像 |
| 3:2 | 经典摄影 |
| 2:3 | 竖版人像 |
| 21:9 | 超宽屏 |

## 输出示例

```json
{
  "saved": ["/path/to/image_001.jpg"]
}
```

## API Key 配置

当前配置的密钥：`sk-cp-BC0OPAa8Y5HiiKOIHZpC4WRiBF3PEeGXDl2WgAaG7mRI7WHsGXhMdQWXErRKZvrNu6gH_iH-tTMjQsozFC_akhP9VOPJSxh1gMzb-P2KchmzTXBRGjZWBbY`

区域：cn (国内版)