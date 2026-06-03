---
name: minimax-usage
description: 当用户询问还剩多少额度、查看用量、检查配额、账户余额，或需要查询 MiniMax API 账户余额和用量配额时触发。
---

# MiniMax Usage Query Skill

## 功能描述

使用 MiniMax Token Plan API 查询账户的用量信息和剩余配额。

## 使用方法

### 基本用法

```bash
# 查询用量（表格格式）
python scripts/query.py

# 查询用量（JSON 格式）
python scripts/query.py --format json
```

### 命令行参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `-f`, `--format` | 输出格式 (table, json) | table |
| `-h`, `--help` | 显示帮助 | - |

### Python API

```python
from scripts.query import query_usage, format_usage_table, format_usage_json

# 查询用量
data = query_usage()

# 表格格式输出
print(format_usage_table(data))

# JSON 格式输出
print(format_usage_json(data))
```

## 输入输出

### 输入
- 无需输入参数（使用预配置的 API Key）

### 输出
- 账户用量信息，包括：
  - 已使用 Token 数量
  - 剩余 Token 数量
  - 总配额
  - 各服务用量详情

## 示例输出

```
================================
    Minimax Account Usage
================================

Model: MiniMax-M2.7
--------------------------------
  Period:         2026-01-01 to 2026-01-31
  Quota:          5000 requests
  Used:           2345 requests (46.9%)
  Remaining:      2655 requests

================================
Query Time: 2026-01-15 14:30:00
================================
```

## 注意事项

- API 请求超时时间为 30 秒
- 表格格式适合快速查看
- JSON 格式适合程序处理
- 数据可能包含多个服务的用量信息