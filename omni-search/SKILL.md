---
name: omni-search
description: 一体化极致搜索 - 融合系统内置搜索、博查 AI、MiniMax Token Plan、知识库/笔记四大搜索源，每次调用都自动多源并行、跨源去重、关键词扩展、时效性增强，最大限度榨干每个搜索源的价值。当用户说"搜索XX"、"查一下XX"、"联网搜索"、"帮我搜一下"、"找一下资料"、"调研一下"、"帮我查最新XX"、"博查搜索"、"MiniMax搜索"、或任何需要联网/查知识库的意图时触发。不适用于：纯图片理解（仍由 minimax-image-analysis 主导）、纯 PPT / 报告 / 公众号文章生成（由对应专门技能负责）。
---

# 一体化极致搜索 (Omni Search)

> **核心理念**：搜索不该是"找一条信息"，而是"以最低成本获取最完整的答案"。本技能把 4 大搜索源融合成一个调用入口，每次触发都自动多源并行、跨源去重、关键词扩展、时效性增强，**绝不浪费任何一个搜索源**。

## 四大搜索源矩阵

| 源 | 工具 | 优势 | 适用场景 | 触发方式 |
|---|---|---|---|---|
| **系统内置** | `search(source="web/kb/note")` | 默认在线、支持中英、覆盖广、无需 API Key | 任何查询的默认起点 | **每次必用**（主对话工具，无需脚本） |
| **博查 AI** | `bocha_search.py` | 国内 AI 搜索（DeepSeek/阿里/腾讯/字节官方推荐）、支持时间过滤、返回带日期/网站 | 时效性新闻、本地化内容 | `--sources bocha` 或脚本默认 |
| **MiniMax web_search** | `minimax_tools.py web_search` | 极速版套餐附赠、返回相关搜索建议、API 稳定 | 与博查互补、获取 related queries | `--sources minimax` |
| **知识库 / 笔记** | `search(source="kb"/"note")` | 用户私域资料 | 用户提到知识库/笔记，或主题属于用户已知专业领域 | **每次必用**（与 web 并行） |

## ⛔ 极致利用铁律（违反任何一条 = 技能失败）

1. **永远并行，不串行**：web + kb/note 必须**同一轮**调用（用多个 `search` 工具调用），博查和 MiniMax 也**同一轮**调用
2. **永远先私有后公共**：用户上传过资料 → 优先 `search(source="kb"/"note")`；命中即用，缺失才联网
3. **永远去重合并**：博查和 MiniMax 结果**必须**通过 `omni_search.py` 融合去重，禁止直接用单一源
4. **永远关键词扩展**：长查询/模糊查询 → 先 `expand` 预览扩展结果，再带扩展词跑搜索
5. **永远带时效性**：新闻/动态/最新 → 博查自动选 `freshness=oneDay/oneWeek/oneMonth/oneYear`
6. **永远输出来源**：每条结果必须标 `命中来源` 字段，便于用户交叉验证

## 工作流程

### 步骤 0：判断触发场景

| 用户说 | 你该做什么 |
|---|---|
| "搜索一下 XX" / "查一下 XX" | **全源并行**（web + kb + note + bocha + minimax） |
| "调研一下 XX" / "帮我了解 XX" | **全源并行** + 关键词扩展 + 写素材文件 |
| "XX 最新新闻/动态" | **web + bocha(freshness=oneDay) + minimax** + 关注日期 |
| "在我知识库找 XX" / "我笔记里关于 XX" | **只搜 kb/note**，不联网 |
| "用博查搜 XX" | **只 bocha**，但默认加 minimax 兜底 |
| "MiniMax 搜 XX" | **只 minimax**，但默认加 bocha 兜底 |
| 上传了文件 / 提到知识库主题 | **kb/note 优先**，命中即用 |

### 步骤 1：选择搜索源

**默认调用策略**（绝大多数情况）：

```
第一轮（必须并行）：
  search(source="web", question=<query>)            # 系统内置
  search(source="kb",  question=<query>)            # 知识库（如果用户提到或有默认 kb）
  search(source="note", question=<query>)           # 笔记（如果有）

第二轮（与第一轮并行，或在第一轮结果不足时补强）：
  shell: python3 omni_search.py search "<query>" --topic <kind>
  # 内部已含：博查 + MiniMax + 关键词扩展 + 去重合并
```

### 步骤 2：执行博查 + MiniMax（脚本自动融合）

```bash
# 默认（双源 + 关键词扩展 + 去重 + 来源标记）
python3 /sandbox/workspace/skills/omni-search/scripts/omni_search.py search "深度学习在医疗影像的应用"

# 时效性话题（自动选 freshness）
python3 ... omni_search.py search "AI 最新进展" --topic news

# 指定时间范围
python3 ... omni_search.py search "科技动态" --topic weekly

# 单源模式
python3 ... omni_search.py search "测试" --sources bocha
python3 ... omni_search.py search "测试" --sources minimax

# 拿到 JSON（用于二次处理）
python3 ... omni_search.py search "测试" --json > /tmp/results.json

# 仅看关键词扩展（不实际搜索）
python3 ... omni_search.py expand "模糊查询"
```

**返回内容**（脚本自动输出）：
- 📊 命中统计（博查 X / MiniMax Y / 去重 Z）
- ⚠️ 错误列表
- 📝 合并去重后的结果列表（每条带 `命中来源` 字段）
- 💡 MiniMax 相关搜索建议

### 步骤 3：跨源融合

如果用户需要全面答案，**手动跨源融合**：

```
第一轮结果 = search web/kb/note
第二轮结果 = omni_search.py search (bocha + minimax 融合)
第三轮     = 自己用 LLM 综合两轮，按来源分组、按时效性排序
```

### 步骤 4：交付答案

- 简查询：直接列出 Top 5-10 结果 + 来源 + 摘要
- 调研任务：先写素材文件到 workspace，再交付总结
- 报告任务：交由 `ima-report` 技能接管（不要在 omni-search 内写报告）

## 触发关键词

- "搜索一下" / "查一下" / "联网搜索" / "帮我搜" / "找一下" / "查最新"
- "调研" / "了解一下" / "研究一下"
- "博查" / "bocha" / "MiniMax搜索"
- "知识库找" / "笔记里"
- 任何需要外部信息的查询意图

## 错误处理

| 场景 | 处理 |
|---|---|
| `BOCHA_API_KEY` 未配置 | 脚本自动降级为单 MiniMax 源，错误信息明确提示 |
| MiniMax 限流 | 重试 1 次，失败则降级为博查单源 |
| 所有源都失败 | 返回错误汇总 + 建议用户用浏览器手动搜 |
| 系统内置 search 不可用 | 跳过该源，仅用 bocha + minimax |
| 知识库为空 | 跳过该源，不报错 |

## 典型使用示例

### 示例 1：新闻时效性查询
```
用户：今天 AI 行业有什么大新闻？
步骤：
  1. shell: python3 omni_search.py search "AI 行业 新闻" --topic news
     → 自动选 freshness=oneDay，关键词扩展加当前日期
  2. 整理 Top 5 输出
```

### 示例 2：本地化专业内容
```
用户：搜一下"推拿治疗颈椎病"的最新研究
步骤：
  1. search(source="note", question="推拿治疗颈椎病")  # 用户笔记
  2. search(source="kb",   question="推拿 颈椎病")      # 知识库
  3. shell: omni_search.py search "推拿治疗颈椎病 最新研究" --topic news
  4. 整合私域 + 公网结果
```

### 示例 3：模糊查询自动扩展
```
用户：帮我了解下最近那个很火的开源模型
步骤：
  1. shell: omni_search.py expand "最近那个很火的开源模型"
     → 输出多组候选关键词
  2. shell: omni_search.py search "<主关键词>" --topic news
  3. 必要时用扩展词补搜
```

### 示例 4：纯私域检索
```
用户：在我的知识库里找"针灸禁忌"相关内容
步骤：
  1. search(source="kb", question="针灸禁忌")
  2. search(source="note", question="针灸禁忌")
  3. 整理输出（不联网）
```

## 与其他技能的关系

- **不接管**：`ima-report`（报告生成）、`ima-ppt`（PPT）、`wechat-article-publisher`（公众号）、`minimax-image-analysis`（图片分析）
- **互补**：`ima-knowledge`（管理知识库，不搜索）和 `ima-note`（管理笔记，不搜索）是 omni-search 的私域数据来源
- **可被调用**：本技能只做"信息收集"，不做"信息加工"——拿到素材后交给 `ima-report` 写报告、交给 `huadu-pangu` 提炼观点

## 注意事项

- **多源并行 ≠ 重复劳动**：博查和 MiniMax 索引池不同，重复率 < 30%，去重后净增量显著
- **关键词扩展 ≠ 跑题**：扩展只在主查询太模糊时启用，1 个查询最多扩展 4 组
- **知识库优先 ≠ 忽视网络**：私域命中时仍可补联网验证最新事实
- **博查 freshness**：默认 noLimit；带时间关键词时自动收紧（oneDay/oneWeek/oneMonth/oneYear）
- **MiniMax 推荐 related**：脚本末尾输出，可作为下一轮搜索的关键词灵感
