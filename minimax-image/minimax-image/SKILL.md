---
name: minimax-image
description: 使用 MiniMax image-01 生图，当用户说"生成图片"、"创建图片"、"画一张图"、"文生图"、"generate an image"、"create a picture"时触发。
---

# MiniMax Image Generation Skill - 文生图

## 触发条件

当用户请求以下操作时触发此 Skill：

- 生成图片
- 创建图片
- 画一张图
- 根据描述生成图片
- 文本生成图片
- generate an image / create a picture / draw

## 功能描述

使用 MiniMax Token Plan API 根据文本描述生成高质量图片。

## 使用方法

### 基本用法

```bash
# 生成单张图片
python scripts/generate.py "一只飞翔的猫，太空风格"

# 生成多张图片
python scripts/generate.py "未来城市赛博朋克风格" --n 4

# 指定宽高比
python scripts/generate.py "山水风景画" --aspect-ratio 16:9

# 指定输出目录
python scripts/generate.py "可爱的小狗" --output-dir ./images --prefix my_pet
```

### 命令行参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| 位置参数 | 图片描述提示词 | - |
| `-r`, `--aspect-ratio` | 宽高比 | 1:1 |
| `-n`, `--num` | 生成数量 (1-9) | 1 |
| `-o`, `--output-dir` | 输出目录 | . |
| `-p`, `--prefix` | 文件名前缀 | generated |
| `-h`, `--help` | 显示帮助 | - |

### Python API

```python
from scripts.generate import generate_image, save_images

# 生成图片
images = generate_image(
    prompt="未来城市天际线，赛博朋克风格",
    aspect_ratio="16:9",
    n=2
)

# 保存到文件
save_images(images, "./output", "cyberpunk_city")
```

## 支持的宽高比

| 比例 | 适用场景 |
|------|----------|
| 1:1 | 社交媒体头像、正方形图片 |
| 16:9 | 横版图片、桌面壁纸 |
| 9:16 | 竖版图片、手机壁纸 |
| 4:3 | 经典照片比例 |
| 3:4 | 竖版照片、人像 |
| 3:2 | 经典摄影比例 |
| 2:3 | 竖版人像 |
| 21:9 | 超宽屏壁纸 |

## 示例输出

```
🎨 正在生成图片...
   提示词: 一只飞翔的猫，太空风格
   宽高比: 1:1
   数量: 2

✅ 已保存: ./generated_1710000000_1.png
✅ 已保存: ./generated_1710000000_2.png

✨ 成功生成 2 张图片!
```

## 示例图片提示词

- "a cat flying through space, comic style" (太空猫，漫画风格)
- "cute cat poses, multiple angles" (可爱的猫咪多角度)
- "herdsman pointing to Xinghua village, traditional Chinese ink wash painting style" (传统水墨画风格)
- "cyberpunk city at night with neon lights" (霓虹灯赛博朋克城市)

## 注意事项

- 图片格式为 PNG
- 文件名格式: `{prefix}_{timestamp}_{index}.png`
- 请求超时时间为 180 秒
- 生成多张图片会增加处理时间