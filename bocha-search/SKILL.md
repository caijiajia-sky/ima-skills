---
name: bocha-search
description: 博查搜索技能 - 使用博查AI搜索引擎进行联网搜索。当用户说"搜索一下XX"、"查一下XX"、"联网搜索"、"博查搜索"、"bocha search"时触发。不适用于非搜索类任务。
---

# 博查搜索 (Bocha Search)

## 概述

使用博查AI搜索引擎进行实时联网搜索，获取高质量的搜索结果。博查是国内领先的AI搜索引擎，为DeepSeek、阿里、腾讯、字节等官方推荐的搜索API。

## 工作流程

### 第一步：执行搜索

使用 `bocha_search.py` 脚本执行搜索：

```bash
python3 /sandbox/workspace/skills/bocha-search/scripts/bocha_search.py "搜索关键词" [结果数量]
```

**参数说明：**
- `搜索关键词`：必填，要搜索的内容
- `结果数量`：可选，1-50，默认10条

**可选参数（通过环境变量或参数）：**
- `freshness`：时间范围过滤，可选值：
  - `noLimit`：不限时间（默认）
  - `oneDay`：最近一天
  - `oneWeek`：最近一周
  - `oneMonth`：最近一月
  - `oneYear`：最近一年
  - `YYYY-MM-DD`：指定日期
  - `YYYY-MM-DD..YYYY-MM-DD`：日期范围

### 第二步：返回结果

脚本会自动调用博查API并返回格式化结果，包含：
- 网页标题
- 网页链接
- 网页摘要
- 发布时间
- 网站名称

## 典型使用场景

### 场景1：快速搜索
```
用户：搜索一下最新的人工智能新闻
执行：python3 /sandbox/workspace/skills/bocha-search/scripts/bocha_search.py "人工智能最新新闻"
```

### 场景2：限定时间范围
```
用户：帮我查一下这周的科技动态
执行：python3 /sandbox/workspace/skills/bocha-search/scripts/bocha_search.py "科技动态" --freshness oneWeek
```

### 场景3：获取多条结果
```
用户：帮我搜索10条关于健康的最新资讯
执行：python3 /sandbox/workspace/skills/bocha-search/scripts/bocha_search.py "健康资讯" 10
```

## API Key 配置

博查API Key需要在环境变量中配置：`BOCHA_API_KEY`

如需配置，请告知用户前往 [博查AI开放平台](https://open.bochaai.com) 注册获取。

## 错误处理

| 错误类型 | 处理方式 |
|---------|---------|
| 缺少API Key | 提示用户配置BOCHA_API_KEY |
| 网络错误 | 重试一次，失败则返回错误信息 |
| API调用失败 | 返回具体错误原因 |