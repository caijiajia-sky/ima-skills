---
name: skill-version-control
description: 技能版本控制与防丢失管理。任何创建/更新技能的流程都必须经过本技能的强制 3 处同步（本地 + GitHub 仓库 + ima 知识库"腾讯ima软件Skills备份"），并在 memory_md 登记同步指纹，杜绝因沙箱重置导致技能变幽灵。当用户说"创建技能""新建 Skill""更新技能""同步技能""技能版本""防丢失""3处同步""强制同步"时触发。**此技能为强制性门禁——任何技能创建/更新操作都必须以本技能收尾才算完成。**
---

# skill-version-control (svc)

> **核心目标：杜绝幽灵技能。** 任何技能在沙箱丢失后都能从至少一处外部副本恢复。

## 为什么需要这个技能

**残酷现实**：沙箱环境是非持久的，`/root/.skills/` 下的文件随时可能被重置，但记忆（memory）里仍保留着该技能存在过的痕迹——这就是"幽灵技能"。2026-06-06 一次盘点发现 13 个技能变幽灵，核心业务流（`ai-comic-creator`、`medical-science-popularizer`、`skill-adversarial-validation`）全部失踪。

**唯一可靠的防御** = 强制把每个技能的副本写到你控制下的多处持久存储。

## 强制 3 处同步（缺一不可）

```
技能创建/更新
  ↓
┌─────────────────────────────────────────┐
│ 1. 本地（/root/.skills/{name}）         │ ← 默认落点，但沙箱可能丢
│ 2. GitHub caijiajia-sky/ima-skills      │ ← 你控制的代码仓库
│ 3. ima 知识库 kb_id=MisO3d_...          │ ← 平台级持久存储
│ 4. memory_md 登记同步指纹               │ ← 防止未来找不到同步记录
└─────────────────────────────────────────┘
  ↓
✅ 完成
```

**任意一处失守**，其他两处可恢复——这就是这套机制的核心保险逻辑。

## ⛔ 硬门禁规则

> **违反任何一条 = 流程未完成，禁止宣告"技能已创建/更新"**

1. **创建技能时**必须调用 `svc.py create <name> "<description>"`，生成骨架后填内容，最后再调一次 `svc.py update <name>` 走完 3 处同步
2. **更新技能时**必须调用 `svc.py update <name>`，不允许只改本地文件就声称更新
3. **任何时候**发现本地有未登记的技能，必须立即 `svc.py update <name>` 补同步
4. **每次同步后**必须在 memory_md 追加一行记录：`sync: <name> -> github=<hash> kb=<file_count>`
5. **不写明文密钥**到任何一处的源文件——这是 ima-skill-creator 流程的硬性要求，本技能继承

## 工作流程

### 创建新技能

```bash
# Step 1: 用 svc 创建骨架 + 同步
python3 /root/.skills/skill-version-control/scripts/svc.py create <skill-name> "<description>"

# Step 2: 编辑 SKILL.md 和 scripts/
# (使用 ima-skill-creator 的设计原则)

# Step 3: 完成后再次同步
python3 /root/.skills/skill-version-control/scripts/svc.py update <skill-name>

# Step 4: 手动在 memory_md 追加:
# sync: <skill-name> -> github=<commit_hash> kb=<file_count>
```

### 更新已存在技能

```bash
# 编辑文件后
python3 /root/.skills/skill-version-control/scripts/svc.py update <skill-name>
# 然后在 memory_md 追加同步记录
```

### 审计单个技能

```bash
python3 /root/.skills/skill-version-control/scripts/svc.py audit <skill-name>
# 输出：本地哈希 vs 上次同步哈希、平台状态、GitHub 状态、KB 状态
```

### 全量审计（盘查幽灵技能）

```bash
python3 /root/.skills/skill-version-control/scripts/svc.py audit-all
# 输出三类清单：
# 🔴 幽灵（登记了但本地没了）→ 建议从 GitHub/KB 恢复或删除登记
# 🟡 未登记（本地有但没走 3 处同步）→ 立即补同步
# 🟢 完整同步
# 🟢 仅远端（本地缺失但 GitHub 远端有）→ 可一键 restore
```

### 🆕 从 GitHub 远端恢复（兜底机制）

**这是防丢失的最终防线**——当沙箱丢失技能、平台卸载技能时，从 GitHub 远端拉回。

```bash
# 恢复单个技能
python3 /root/.skills/skill-version-control/scripts/svc.py restore <skill-name>
# 强制覆盖（覆盖本地现有版本）
python3 /root/.skills/skill-version-control/scripts/svc.py restore <skill-name> --force
# 只恢复到某个位置
python3 /root/.skills/skill-version-control/scripts/svc.py restore <skill-name> --target local
python3 /root/.skills/skill-version-control/scripts/svc.py restore <skill-name> --target workspace

# 全量对比 + 一键恢复
python3 /root/.skills/skill-version-control/scripts/svc.py restore-all --dry-run  # 只看差异
python3 /root/.skills/skill-version-control/scripts/svc.py restore-all              # 实际恢复
```

**前置条件**：环境变量 `GITHUB_TOKEN` 已设置（否则会因权限不足无法访问远端）。

**实测案例**：2026-06-06 一次沙箱清空，13 个技能变"幽灵"。用 `restore-all` + `restore <name>` 一次性把 12 个从远端拉回（剩下的 1 个在远端也丢失，需重建）。

### 🆕 完整命令清单

```
svc.py create <name> <desc>   # 创建技能
svc.py update <name>          # 更新已存在技能
svc.py audit <name>           # 审计单个技能
svc.py audit-all              # 全量审计（含远端对比）
svc.py restore <name>         # 从 GitHub 恢复单个技能 [新]
svc.py restore-all            # 全量对比 + 一键恢复 [新]
```

## 关键配置（硬编码在 svc.py）

| 配置项 | 值 | 说明 |
|---|---|---|
| `GITHUB_REPO` | `caijiajia-sky/ima-skills` | 你的公开 GitHub 仓库 |
| `GITHUB_LOCAL_PATH` | `/sandbox/workspace/github-mirror/ima-skills` | 本地镜像（首次自动 clone） |
| `KB_NAME` | `腾讯ima软件Skills备份` | 知识库名称 |
| `KB_ID` | `MisO3d_JF3Tk2l1fKGYmAVNj4ropntstRXCvOiWzlqU=` | 知识库 ID |
| `LOCAL_SKILLS_DIR` | `/root/.skills` | 平台注册位置 |
| `WORKSPACE_SKILLS_DIR` | `/sandbox/workspace/skills` | workspace 副本位置 |
| `REGISTRY_FILE` | `/root/.skills/.sync-registry.json` | 同步指纹登记 |

## 与其他技能的关系

- **被 ima-skill-creator 调用**：创建/修改技能后，必须用本技能收尾
- **联动 github-mcp**：通过 git CLI 推送（如 github-mcp MCP 不可达，自动降级为本地 git 记录）
- **联动 ima-knowledge**：知识库上传通过 ima-knowledge 的 upload API（在 Agent 上下文里执行，svc 产出 manifest）
- **联动 huadu-pangu**：如果走盘古造 skill 流程，最后也必须经过 svc 收尾
- **本技能自身也受规则约束**：svc.py 改完必须 `svc.py update skill-version-control` 同步自己

## 降级策略

| 失败环节 | 降级行为 |
|---|---|
| `ima_skill_create` 不可用 | 兜底策略：检测到 PATH 中没有该命令时，标记 `status=degraded-publish-pending`，**不阻断**；Agent 在 use_skill 上下文（平台命令可用环境）发现此状态时**必须主动重试发布** |
| `ima_skill_create` 调用失败（命令在但报错） | 阻断流程，提示用户检查平台凭证 |
| GitHub 不可达 | 本地 git commit 仍记录，标记 `status=local-only`，不阻断 |
| KB 上传失败 | 记录 manifest 文件清单到 registry，下次可补传 |
| memory 写入失败 | 强烈警告（这是最后一道防线），但允许继续 |

**设计原则**：宁可本地不一致，也要把 GitHub/KB/memory 三个外部副本先保住——沙箱丢了能恢复，外部都没了就真的没了。

## 典型使用示例

### 示例 1：创建新技能
```
用户：帮我创建一个"周报生成"技能

Agent 流程：
  1. 加载 ima-skill-creator，设计技能
  2. 完成 SKILL.md 和 scripts/
  3. python3 svc.py create weekly-report "周报自动生成技能"
     → 生成骨架 + 自动注册到平台
  4. 填充 SKILL.md 内容
  5. python3 svc.py update weekly-report
     → 重新注册 + 推 GitHub + 生成 KB manifest
  6. Agent 在 memory_md 追加: sync: weekly-report -> github=abc123 kb=5
  7. 告知用户"完成"
```

### 示例 2：发现幽灵技能
```
Agent 流程：
  1. python3 svc.py audit-all
  2. 发现 skill-adversarial-validation 在 ghosts 列表
  3. Agent 调用 search(source="kb", kb_id=KB_ID) + search(source="web")
     找 GitHub 仓库里这个技能的历史版本
  4. 拉取/重建 SKILL.md
  5. python3 svc.py update skill-adversarial-validation
  6. 报告用户"已从 GitHub 恢复"
```

### 示例 3：批量补同步
```
用户：把本地所有没登记的技能都补同步

Agent 流程：
  1. python3 svc.py audit-all → 拿到 unregistered 列表
  2. 对每个 unregistred 技能：
     python3 svc.py update <name>
  3. 报告结果
```

## 注意事项

- **svc.py 自己也是技能**，修改后必须走 `svc.py update skill-version-control`
- **GitHub 推送可能因网络失败**，脚本会自动降级但要定期检查
- **KB 上传由 Agent 在 ima-knowledge 上下文执行**，svc 只生成 manifest
- **memory_md 是不可丢失的最后记录**——所有同步都登记在这里
- **不替代 ima-skill-creator**——创建技能仍由 ima-skill-creator 主导，本技能只做"防丢失"这一步
