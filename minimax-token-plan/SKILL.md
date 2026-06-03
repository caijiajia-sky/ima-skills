---
name: minimax-token-plan
description: MiniMax Token Plan 极速版 API 调用技能。当用户说"帮我搜索XX"、"搜索一下XX"、"联网搜索"、或"帮我分析这张图片"、"识别图片内容"、"分析这张图片"时触发。不适用于非 Token Plan 用户、非极速版套餐用户、或需要使用其他 MiniMax API 功能的场景。
---

# MiniMax Token Plan 极速版工具集

## 概述

MiniMax Token Plan 极速版提供两个核心 AI 能力：

1. **web_search** - 网络搜索，执行网络搜索并获取有机搜索结果及相关搜索查询
2. **understand_image** - 图片理解，基于文本提示使用 AI 分析图像，提取信息并回答关于图像的问题

这两个工具通过 MiniMax API 调用，使用 Token Plan 极速版套餐密钥进行认证。

## 工作方式

### 快速开始

用户触发搜索或图片分析请求时：
1. 调用 `minimax_web_search` 或 `minimax_understand_image` 工具
2. 传入必要的参数（搜索关键词/图片来源+分析提示）
3. 返回结构化结果

### 工具一：网络搜索 (web_search)

**触发场景**：用户说"帮我搜索XX"、"搜索一下XX"、"联网搜索最新XX"、"查一下XX的最新消息"等

**参数**：
- `query` (必填): 搜索查询。建议 3-5 个关键词效果最佳。对于时效性话题，可加入当前日期关键词

**调用方式**：
```javascript
minimax_web_search({
  query: "最新的 AI 技术发展趋势 2025"
})
```

**返回结果**：
- 有机搜索结果列表（标题、链接、摘要）
- 相关搜索查询建议

---

### 工具二：图片理解 (understand_image)

**触发场景**：用户说"帮我分析这张图片"、"识别图片内容"、"这张图里有什么"、"分析一下这个截图"、"图片里写的什么"等

**参数**：
- `prompt` (必填): 分析提示词，描述你想从图片中提取或了解什么
- `image_source` (必填): 图片来源，支持以下格式：
  - HTTP/HTTPS URL: `"https://example.com/image.jpg"`
  - 本地文件路径: `"/sandbox/workspace/uploads/image.png"`
  - 带 @ 前缀的路径: `"@/sandbox/workspace/uploads/image.png"`（@ 会被自动移除）

**调用方式**：
```javascript
minimax_understand_image({
  prompt: "这张图片里有什么？描述一下内容",
  image_source: "https://example.com/sample.jpg"
})
```

或者分析本地图片：
```javascript
minimax_understand_image({
  prompt: "这张图片里有什么？描述一下内容",
  image_source: "/sandbox/workspace/uploads/my_image.png"
})
```

**返回结果**：
- AI 对图片内容的理解和分析
- 图片中提取的文本信息（如有）
- 关于图片问题的直接回答

---

### API 配置

**API 密钥**: `sk-cp-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

**API Host**: `https://api.minimaxi.com`（国内版）

---

## 典型使用示例

### 示例 1：网络搜索

**用户输入**："帮我搜索一下今天有什么 AI 新闻"

**处理**：
```javascript
minimax_web_search({
  query: "AI 人工智能 最新新闻 2025年5月"
})
```

**返回**：搜索结果列表，包含相关新闻标题、链接和摘要

---

### 示例 2：图片分析 - URL

**用户输入**："帮我分析这个图片 https://example.com/photo.jpg ，看看里面有什么"

**处理**：
```javascript
minimax_understand_image({
  prompt: "详细描述这张图片的内容，包括主体、背景、文字等信息",
  image_source: "https://example.com/photo.jpg"
})
```

**返回**：AI 对图片的详细描述和分析

---

### 示例 3：图片分析 - 本地文件

**用户上传图片后输入**："分析一下这张图片"

**处理**：
```javascript
minimax_understand_image({
  prompt: "这张图片的主要内容是什么？有什么重要信息？",
  image_source: "/sandbox/workspace/uploads/user_uploaded_image.png"
})
```

**返回**：图片内容分析结果

---

### 示例 4：截图分析

**用户输入**："帮我看看这个截图里代码有什么问题 https://example.com/screenshot.png"

**处理**：
```javascript
minimax_understand_image({
  prompt: "请分析这张截图中的代码，指出可能的 bug 或问题",
  image_source: "https://example.com/screenshot.png"
})
```

**返回**：代码分析和问题识别

---

## 错误处理

1. **API 密钥错误**：检查 API Host 是否为 `https://api.minimaxi.com`（国内版）
2. **图片无法访问**：确保 URL 可访问，或使用本地文件路径
3. **不支持的图片格式**：仅支持 JPEG、PNG、WebP 格式
4. **查询为空**：搜索关键词必填，确保提供有效的搜索词

---

## 注意事项

- 使用这些工具可能会产生 Token Plan 套餐内的费用
- 图片分析支持 JPEG、PNG 和 WebP 格式
- 网络搜索建议使用 3-5 个关键词，效果最佳
- 对于时效性话题，建议在搜索词中加入当前日期或时间