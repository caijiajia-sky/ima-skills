---
name: ima-note
description: 管理用户的笔记和笔记本（新建、追加、推送、重命名、移动笔记，按标题定位笔记，按笔记本浏览笔记列表，导出笔记到 workspace，创建/重命名笔记本），当用户提到笔记、备忘录、记事，且涉及以上意图时，使用此 skill。按内容搜索笔记或阅读笔记正文应使用 Search / Fetch 工具，不触发此 skill。
---

# ima-note

通过 IMA OpenAPI 管理用户个人笔记，覆盖完整的读写和笔记本管理场景。

## API 调用模板

所有请求统一为 **HTTP POST + JSON Body**，Base URL 为 `https://ima.qq.com/openapi/note/v1`。

```bash
curl -s -X POST "https://ima.qq.com/openapi/note/v1/{endpoint}" \
  -H "ima-openapi-clientid: $IMA_OPENAPI_CLIENTID" \
  -H "ima-openapi-apikey: $IMA_OPENAPI_APIKEY" \
  -H "Content-Type: application/json" \
  -d '{...}'
```

所有响应的外层结构统一为：
```json
{"code": 0, "msg": "success", "data": { ... }}
```
通过 `code` 字段判断是否成功：`code=0` 为成功，非零为错误码（常见错误码见下方约束速记，完整错误码表见 `references/api.md`）。

## 关键概念

在调用任何接口之前，需要理解三个核心概念——它们贯穿所有接口：

| 概念 | 说明 | 获取方式 |
|------|------|----------|
| `note_id` | 笔记唯一 ID，所有针对单篇笔记的操作都需要它 | `search_note` 或 `list_note` 返回（详见各接口的返回说明） |
| `folder_id` | 笔记本 ID，不传时默认查全部笔记 | `list_notebook` 返回（取 `folder_type=0` 即用户自建的条目） |
| `content_format` | 文本格式枚举 | **写入固定传 `1`**（Markdown，API 写入端只支持这一种） |

> 展示给用户时**只用标题来指代笔记**，不暴露 note_id / folder_id——这些是内部标识，用户不需要看到。

## 规则

1. **操作失败时给出明确原因和建议** —— 如权限不足（210005）提示用户确认是否为笔记作者，内容过大（210009）建议拆分写入
2. **遇到以下情况时查阅 `references/api.md`**（日常调用不需要加载它）：
   - 遇到未知错误码，需要查错误码表
   - 需要解析嵌套返回结构（如 `note_ext_info`、`highlightInfo` 的完整字段定义）
   - 需要确认公共结构体（NoteBookInfo、NoteFolderInfo 等）的完整字段列表
   - 需要了解游标翻页的详细规范
3. **按内容搜索笔记或阅读笔记正文时，不应加载此 skill** —— Search 工具提供关键词+向量+重排序的融合搜索，Fetch 工具可直接读取笔记内容，两者在内容搜索和阅读场景下效果更优。此 skill 的读取能力聚焦于：按标题定位笔记（获取 note_id 及笔记本归属）、按笔记本浏览笔记列表、导出笔记到 workspace。
4. **当前 API 不支持任何删除操作** —— 无法删除笔记、笔记本或任何已写入的内容。如果用户要求删除，直接告知需要在 IMA 客户端中手动操作，**不要尝试寻找或构造删除接口，不要重试**。
5. **所有写入操作不可逆** —— 由于没有删除 API，一旦创建（笔记、笔记本）或写入内容（import_doc、append_doc、push_note），就无法通过 API 撤回。因此：当写入操作不是由用户显式/隐式要求时，必须先向用户确认再执行。

## 接口速查

### 读取类

#### search_note — 按标题定位笔记

`/openapi/note/v1/search_note`

**触发场景**：按标题定位笔记，获取 note_id 及笔记本归属信息。按正文内容搜索应优先使用 Search 工具，此处仅作 fallback。

请求体结构：
```json
{
  "search_type": "int, 必填, 0=标题检索, 1=正文检索",
  "query_info": {
    "title": "string, search_type=0 时必填, 标题关键词",
    "content": "string, search_type=1 时必填, 正文关键词"
  },
  "start": "int, 必填, 翻页起始位置",
  "end": "int, 必填, 翻页结束位置, 与 start 相差不超过 20"
}
```

返回要点：
- `data.search_note_infos[]` —— 结果列表，每条含 `note_book_info`（NoteBookInfo，含 `note_id`、`title`、`summary`、`note_ext_info.folder_id/folder_name`）和 `highlightInfo`（`doc_title` 含 `<em>` 高亮标签）
- `data.is_end` —— bool，是否最后一页
- `data.total_hit_num` —— 命中总数

#### list_note — 浏览笔记列表

`/openapi/note/v1/list_note`

**触发场景**：用户说「最近的笔记」「看看xx笔记本里有什么」。没有指明笔记本时，`folder_id` 留空查全部。

请求体结构：
```json
{
  "folder_id": "string, 可选, 空字符串=全部笔记, 指定则只查该笔记本",
  "sort_type": "int, 可选, 0=修改时间(默认), 1=创建时间, 2=标题, 3=大小",
  "cursor": "string, 必填, 首次传空字符串, 翻页传已获取的条目总数(如首页 limit=20 则第二页传 '20')",
  "limit": "int, 必填, 每页数量, 最大 20"
}
```

返回要点：
- `data.note_book_list[]` —— 笔记列表（NoteBookInfo，含 `note_id`、`title`、`summary`、`create_time`、`modify_time`、`note_ext_info.folder_id/folder_name`）
- `data.is_end` —— bool，是否最后一页

#### export_note — 导出笔记到 workspace

`/openapi/note/v1/export_note`

**触发场景**：导出笔记原文, 获取笔记的markdown格式, 获取笔记的json格式, 获取笔记的纯文本。也用于 Fetch 工具返回生成内容而非原文时的 fallback：先 export 获取原文再做后续处理。

请求体结构：
```json
{
  "note_id": "string, 必填, 目标笔记 ID",
  "target_content_format": "int, 必填, 推荐传 1 (Markdown)"
}
```

- 返回 `data.content_url`，为带签名的 COS 下载链接（非内容本身），需二次 `curl` 请求该链接获取实际笔记内容。签名有时效（约3小时）
- 下载内容的格式取决于 `target_content_format`：`0` → 纯文本（.txt），`1` → Markdown（.md），`2` → JSON（Slate 编辑器 AST 结构，.json）
- 需要作者权限

### 写入类

#### import_doc — 新建笔记

`/openapi/note/v1/import_doc`

**触发场景**：用户说「新建笔记」「把这段内容保存为笔记」。

请求体结构：
```json
{
  "content_format": "int, 必填, 固定传 1 (Markdown)",
  "content": "string, 必填, Markdown 格式笔记内容。第一行文本会被自动提取为笔记标题",
  "folder_id": "string, 可选, 目标笔记本 ID, 不传则新建到默认位置",
  "folder_name": "string, 可选, 目标笔记本名称"
}
```

- 返回 `data.note_id`，后续可用于 append_doc

#### append_doc — 追加内容到已有笔记

`/openapi/note/v1/append_doc`

**触发场景**：用户说「在这篇笔记末尾加点内容」「把XX添加到笔记里」。适合短内容直接追加；长内容应走 COS 上传 + `push_note`（传 note_id）路径。

请求体结构：
```json
{
  "note_id": "string, 必填, 目标笔记 ID",
  "content_format": "int, 必填, 固定传 1 (Markdown)",
  "content": "string, 必填, 追加的内容"
}
```

- 需要作者权限
- 返回 `data.note_id`

#### push_note — 智能推送（新建或追加）

`/openapi/note/v1/push_note`

**触发场景**：用户说「帮我记一下」「保存这段内容」。当不确定笔记是否已存在时用 —— note_id 为空则新建，不为空则追加。支持通过 `ima_cos_util -f <文件路径>` 上传获取 cosKey，再传 `content_cos_key` 代替 `content`，长内容场景推荐此方式（见「长内容写入策略」章节）。

请求体结构：
```json
{
  "note_id": "string, 可选, 为空则新建笔记, 不为空则追加到该笔记",
  "content": "string, 可选, Markdown 格式笔记内容, 与 content_cos_key 不能同时为空",
  "content_cos_key": "string, 可选, 内容的 COS 对象路径, 当 content 为空时生效"
}
```

- note_id 不为空时需要作者权限
- 返回 `data.note_id`（新建或追加的笔记 ID）

#### rename_note — 重命名笔记

`/openapi/note/v1/rename_note`

请求体结构：
```json
{
  "note_id": "string, 必填, 目标笔记 ID",
  "title": "string, 必填, 新标题"
}
```

- 需要作者权限
- 返回空消息体，成功即可

#### move_notes — 批量移动笔记

`/openapi/note/v1/move_notes`

**触发场景**：用户说「把笔记移到xx笔记本」「整理一下笔记」。

请求体结构：
```json
{
  "note_ids": ["string, 必填, 笔记 ID 数组, 最多 100 条"],
  "target_folder_id": "string, 必填, 目标笔记本 ID",
  "target_folder_name": "string, 可选, 目标笔记本名称"
}
```

- 返回 `data.result` map：key 为 note_id，value 为 true/false —— 可能部分成功，需逐条检查

### 笔记本管理类

#### list_notebook — 查看笔记本列表

`/openapi/note/v1/list_notebook`

请求体结构：
```json
{
  "cursor": "string, 必填, 首页传 '0' (注意和 list_note 不同), 翻页传返回的 next_cursor",
  "limit": "int, 必填, 数量限制, 最大 20"
}
```

返回要点：
- `data.note_folder_infos[]` —— 笔记本列表（含 `folder_id`、`name`、`note_number`、`folder_type`），取 `folder_type=0`（用户自建）的条目获取 `folder_id`
- `data.next_cursor` —— 翻页游标，传入下次请求的 `cursor`
- `data.is_end` —— bool，是否最后一页

#### add_notebook — 创建笔记本

`/openapi/note/v1/add_notebook`

请求体结构：
```json
{
  "folder_name": "string, 必填, 笔记本名称"
}
```

- 返回 `data.folder_id` 和 `data.folder_name`

#### rename_notebook — 重命名笔记本

`/openapi/note/v1/rename_notebook`

请求体结构：
```json
{
  "folder_id": "string, 必填, 目标笔记本 ID",
  "new_folder_name": "string, 必填, 新名称"
}
```

- 返回空消息体，成功即可

## 长内容写入策略

根据内容规模选择写入方式：

| 内容规模 | 推荐方式 |
|---------|---------|
| **短内容**（几句话，无特殊字符） | 直接 `-d '{...}'` 内联 |
| **中等内容**（几百字以内，结构简单） | `file_write` 写 JSON 请求体到临时文件 → `curl -d @文件路径` |
| **长内容**（几百字以上，或含表格/emoji/引号/反斜杠等特殊字符） | 写 `.md` 文件 → `ima_cos_util` 上传 → `push_note` 的 `content_cos_key` |

> 不要把长内容直接嵌入 curl `-d '{...}'` 的内联 JSON 中——特殊字符会导致失败。中等内容可通过 `file_write` 写 JSON 请求体再 `curl -d @文件路径` 发送；长内容推荐 COS 上传路径，可以绕过 JSON 序列化，最为可靠。具体操作示例见下方「多步工作流」。

## 多步工作流

以下场景需要串联多个接口。所有 curl 命令均省略公共 header（见「API 调用模板」）。

### 新建笔记到指定笔记本（长内容）

1. `add_notebook`（或 `list_notebook` 查找已有笔记本）→ 获取 `folder_id`
2. `file_write` 将内容写为 `.md` 文件
3. `ima_cos_util -f <文件路径>` → 获取 cosKey
4. `push_note` → `-d '{"content_cos_key":"<cosKey>"}'` → 获取 `note_id`
5. `move_notes` → `-d '{"note_ids":["<note_id>"],"target_folder_id":"<folder_id>"}'`

### 按标题定位 → 追加内容

1. `search_note` → `-d '{"search_type":0,"query_info":{"title":"关键词"},"start":0,"end":20}'`
2. 从 `data.search_note_infos[].note_book_info.note_id` 取目标笔记 ID
3. 写入追加内容（按内容规模选择，见「长内容写入策略」）：
   - **短内容**：直接 `append_doc` + `-d '{...}'` 内联
   - **中等内容**：`file_write` 写 JSON 请求体 → `append_doc` + `curl -d @文件路径`
   - **长内容**：`file_write` 写 `.md` 文件 → `ima_cos_util` 上传获取 cosKey → `push_note` + `-d '{"note_id":"<note_id>","content_cos_key":"<cosKey>"}'`

### 指定笔记本 → 浏览笔记

1. `list_notebook` → `-d '{"cursor":"0","limit":20}'`
2. 从 `data.note_folder_infos` 中找 `folder_type=0` 的条目，取 `folder_id`
3. `list_note` → `-d '{"folder_id":"<folder_id>","cursor":"","limit":20}'`

## 关键约束速记

- **`folder_id` 不可传 `"0"`** —— "0" 不是有效的根目录 ID，根目录的真实 ID 需从 `list_notebook` 返回中 `folder_type=1` 的条目获取
- **写入固定 Markdown** —— 写入接口的 `content_format` 固定传 `1`
- **需要作者权限的接口** —— `append_doc`、`rename_note`、`export_note`、`push_note`（仅 note_id 非空时），否则返回 `210005`
- **时间字段是 Unix 毫秒时间戳** —— 展示时转为用户可读的日期格式
- **翻页策略不统一** —— `list_notebook` 首页 cursor 传 `"0"`，`list_note` 首页 cursor 传空字符串 `""`，`search_note` 用 `start`/`end` 偏移量。三者不可混用
- **常见错误码速查** —— `210001` 参数错误、`210005` 非笔记作者、`210009` 内容过大需拆分、`210030` 笔记本名称重复、`210035` 笔记本不存在

> 完整的公共结构体字段定义、枚举值、游标翻页规范、全部错误码表见 `references/api.md`。日常调用不需要加载它——只在遇到未知错误码、需要解析嵌套返回结构、或确认完整字段定义时再查阅。
