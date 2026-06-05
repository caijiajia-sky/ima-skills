#!/usr/bin/env python3
"""
skill-version-control 同步脚本
对一个技能目录执行强制 3 处同步：本地 + GitHub + ima 知识库 + 记忆登记

用法：
    # 创建新技能（生成 SKILL.md 模板 + 强制 3 处同步）
    python3 svc.py create <skill-name> "<description>"

    # 更新已存在技能
    python3 svc.py update <skill-name>

    # 仅检查 3 处同步状态
    python3 svc.py audit <skill-name>

    # 全量审计（盘查所有技能）
    python3 svc.py audit-all

依赖：仅使用 ima-skill-creator 提供的 init_skill.py 模板风格；
     同步通过 shell 包装的 git/curl/python 子进程完成。
"""

import os
import sys
import json
import shutil
import subprocess
import hashlib
import argparse
from datetime import datetime
from pathlib import Path

# ============================================================
# 配置
# ============================================================

GITHUB_REPO = "caijiajia-sky/ima-skills"
GITHUB_LOCAL_PATH = "/sandbox/workspace/github-mirror/ima-skills"
KB_NAME = "腾讯ima软件Skills备份"
KB_ID = "MisO3d_JF3Tk2l1fKGYmAVNj4ropntstRXCvOiWzlqU="
LOCAL_SKILLS_DIR = "/root/.skills"
WORKSPACE_SKILLS_DIR = "/sandbox/workspace/skills"
REGISTRY_FILE = "/root/.skills/.sync-registry.json"

SKILL_TEMPLATE = """---
name: {name}
description: {description}
---

# {name}

> 自动生成的占位 SKILL.md。请使用 ima-skill-creator 技能完善内容。

## 待办
- [ ] 编写完整 SKILL.md 正文
- [ ] 添加 scripts/ 目录（如需）
- [ ] 完成 3 处同步（git + 知识库 + 记忆）
- [ ] 调用 `python3 /root/.skills/skill-version-control/scripts/svc.py update {name}` 走完发布流程

## 同步状态
（将由 svc.py 脚本自动填充）
"""


# ============================================================
# 工具函数
# ============================================================

def compute_dir_hash(path: Path) -> str:
    """计算目录内容哈希（用于变更检测）"""
    if not path.exists():
        return ""
    h = hashlib.sha256()
    for p in sorted(path.rglob("*")):
        if p.is_file() and "__pycache__" not in str(p) and not p.name.startswith("."):
            h.update(str(p.relative_to(path)).encode())
            h.update(p.read_bytes())
    return h.hexdigest()[:16]


def load_registry() -> dict:
    if os.path.exists(REGISTRY_FILE):
        with open(REGISTRY_FILE) as f:
            return json.load(f)
    return {"version": 1, "skills": {}}


def save_registry(reg: dict):
    os.makedirs(os.path.dirname(REGISTRY_FILE), exist_ok=True)
    with open(REGISTRY_FILE, "w") as f:
        json.dump(reg, f, ensure_ascii=False, indent=2)


def run(cmd: str, cwd: str = None) -> tuple:
    """执行 shell 命令，返回 (returncode, stdout, stderr)"""
    try:
        r = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True, timeout=60)
        return r.returncode, r.stdout.strip(), r.stderr.strip()
    except Exception as e:
        return -1, "", str(e)


def info(msg: str):
    print(f"  ℹ️  {msg}")


def ok(msg: str):
    print(f"  ✅ {msg}")


def warn(msg: str):
    print(f"  ⚠️  {msg}")


def err(msg: str):
    print(f"  ❌ {msg}")


# ============================================================
# 子流程
# ============================================================

def step1_create_scaffold(name: str, description: str) -> Path:
    """Step 1: 创建本地技能骨架"""
    print(f"\n📦 Step 1: 创建技能骨架 [{name}]")
    skill_dir = Path(LOCAL_SKILLS_DIR) / name

    if skill_dir.exists():
        warn(f"技能目录已存在: {skill_dir}，将进入更新模式")
        return skill_dir

    skill_dir.mkdir(parents=True)
    (skill_dir / "scripts").mkdir()

    skill_md = skill_dir / "SKILL.md"
    skill_md.write_text(SKILL_TEMPLATE.format(name=name, description=description), encoding="utf-8")
    ok(f"创建 {skill_md}")
    return skill_dir


def step2_register_to_platform(name: str) -> dict:
    """Step 2: 注册到 IMA 平台（调用 ima_skill_create）"""
    print(f"\n🚀 Step 2: 注册到 IMA 平台")

    # 探测 ima_skill_create 是否在 PATH
    if not shutil.which("ima_skill_create"):
        # 兜底：尝试几个常见位置
        candidates = ["/usr/local/bin/ima_skill_create", "/opt/ima/bin/ima_skill_create"]
        found = None
        for c in candidates:
            if os.path.exists(c):
                found = c
                break
        if not found:
            warn("ima_skill_create 在 PATH 中不可用")
            warn("可能原因：平台 CLI 未注入到本沙箱、平台命令临时降级、跨沙箱未同步")
            warn("兜底策略：登记到 registry，标记 platform=degraded-publish-pending")
            warn("Agent 在 use_skill 上下文里发现 platform.status=degraded 时应主动重试")
            return {
                "status": "degraded-publish-pending",
                "reason": "ima_skill_create 不可用，需在 use_skill 上下文重试",
                "fallback": "Agent 应在有 ima_skill_create 的环境里补跑一次发布",
            }

    skill_dir = Path(LOCAL_SKILLS_DIR) / name
    rc, out, stderr = run(f"ima_skill_create -d {skill_dir}")
    if rc != 0:
        err(f"平台注册失败: {stderr}")
        return {"status": "fail", "error": stderr}
    try:
        result = json.loads(out)
        ok(f"平台注册成功: ID={result.get('id')}, name={result.get('name')}, status={result.get('status')}")
        return result
    except Exception:
        warn(f"平台返回非 JSON: {out}")
        return {"status": "unknown", "raw": out}


def step3_sync_to_github(name: str, commit_msg: str = None) -> dict:
    """Step 3: 同步到 GitHub 仓库"""
    print(f"\n🐙 Step 3: 同步到 GitHub [{GITHUB_REPO}]")
    src = Path(LOCAL_SKILLS_DIR) / name
    if not src.exists():
        err(f"本地目录不存在: {src}")
        return {"status": "fail", "error": "local not found"}

    # 初始化本地镜像（如果不存在）
    if not Path(GITHUB_LOCAL_PATH).exists():
        info("初始化 GitHub 镜像...")
        Path(GITHUB_LOCAL_PATH).parent.mkdir(parents=True, exist_ok=True)
        rc, _, stderr = run(f"git clone https://github.com/{GITHUB_REPO}.git {GITHUB_LOCAL_PATH}")
        if rc != 0:
            # 网络/认证失败时降级为本地 git，不阻断流程
            warn(f"克隆失败（{stderr[:100]}），降级为本地 git 仓库记录")
            if not Path(GITHUB_LOCAL_PATH).exists():
                run(f"mkdir -p {GITHUB_LOCAL_PATH}")
                run(f"cd {GITHUB_LOCAL_PATH} && git init -q && git config user.email 'sky@ima.local' && git config user.name 'Sky'")
            return {"status": "degraded", "note": "github 不可达，仅本地 git 记录"}

    # 拷贝技能目录到镜像
    dst = Path(GITHUB_LOCAL_PATH) / name
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    ok(f"复制 {src} → {dst}")

    # git add + commit + push
    msg = commit_msg or f"sync: {name} @ {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    rc, out, stderr = run(f"cd {GITHUB_LOCAL_PATH} && git add {name}/ && git commit -m '{msg}'")
    if "nothing to commit" in (out + stderr):
        info("无变更，跳过 commit")
        return {"status": "no-change"}
    if rc != 0:
        err(f"commit 失败: {stderr}")
        return {"status": "fail", "error": stderr}

    rc, out, stderr = run(f"cd {GITHUB_LOCAL_PATH} && git push origin main 2>&1")
    if rc != 0:
        warn(f"push 失败（{stderr[:200]}），仅本地 commit 成功")
        return {"status": "local-only", "commit": out}
    ok(f"推送成功: {out[:100]}")
    return {"status": "ok", "commit": out}


def step4_sync_to_kb(name: str) -> dict:
    """Step 4: 同步到 ima 知识库（通过 ima-knowledge API）"""
    print(f"\n📚 Step 4: 同步到知识库 [{KB_NAME}]")
    info("通过 search/upload API 上传（实际由 Agent 在 use_skill 上下文里执行）")
    info(f"目标知识库 ID: {KB_ID}")
    info(f"目标技能目录: /root/.skills/{name}")
    # 实际 API 调用由 Agent 在 ima-knowledge 技能上下文中完成
    # 这里只产出 manifest 供 Agent 参考
    manifest = {
        "action": "upload_folder",
        "kb_id": KB_ID,
        "kb_name": KB_NAME,
        "source_dir": f"/root/.skills/{name}",
        "files": [],
    }
    skill_dir = Path(LOCAL_SKILLS_DIR) / name
    if skill_dir.exists():
        for p in skill_dir.rglob("*"):
            if p.is_file() and "__pycache__" not in str(p):
                manifest["files"].append(str(p.relative_to(skill_dir)))
    print(f"  📄 准备上传 {len(manifest['files'])} 个文件:")
    for f in manifest["files"][:10]:
        print(f"     - {f}")
    if len(manifest["files"]) > 10:
        print(f"     ... 还有 {len(manifest['files']) - 10} 个")
    return manifest


def step5_log_to_registry(name: str, platform_info: dict, github_info: dict, kb_manifest: dict):
    """Step 5: 登记到本地 sync-registry.json（供下次 audit 比对）"""
    print(f"\n📋 Step 5: 登记同步记录")
    reg = load_registry()
    skill_dir = Path(LOCAL_SKILLS_DIR) / name
    reg["skills"][name] = {
        "local_path": str(skill_dir),
        "local_hash": compute_dir_hash(skill_dir),
        "platform": platform_info,
        "github": github_info,
        "kb": kb_manifest,
        "last_sync": datetime.now().isoformat(),
    }
    save_registry(reg)
    ok(f"已登记到 {REGISTRY_FILE}")


# ============================================================
# 完整工作流
# ============================================================

def cmd_create(args):
    name = args.name
    description = args.description
    print(f"\n{'='*60}")
    print(f"🚀 skill-version-control: 创建新技能 [{name}]")
    print(f"{'='*60}")

    # Step 1
    step1_create_scaffold(name, description)

    # Step 2
    platform_info = step2_register_to_platform(name)

    # Step 3
    github_info = step3_sync_to_github(name, commit_msg=f"feat: create {name}")

    # Step 4
    kb_manifest = step4_sync_to_kb(name)

    # Step 5
    step5_log_to_registry(name, platform_info, github_info, kb_manifest)

    print(f"\n{'='*60}")
    print(f"✨ 完成！请在下一步:")
    print(f"   1. 编辑 /root/.skills/{name}/SKILL.md")
    print(f"   2. 添加 scripts/ 内容")
    print(f"   3. 完成后运行: python3 svc.py update {name}")
    print(f"   4. 最后 Agent 会自动写入 memory_md")
    print(f"{'='*60}\n")


def cmd_update(args):
    name = args.name
    print(f"\n{'='*60}")
    print(f"🔄 skill-version-control: 更新技能 [{name}]")
    print(f"{'='*60}")

    skill_dir = Path(LOCAL_SKILLS_DIR) / name
    if not skill_dir.exists():
        err(f"技能不存在: {skill_dir}")
        sys.exit(1)

    # Step 2: 平台重新注册（覆盖）
    platform_info = step2_register_to_platform(name)
    # Step 3: GitHub 同步
    github_info = step3_sync_to_github(name, commit_msg=f"update: {name} @ {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    # Step 4: KB 同步 manifest
    kb_manifest = step4_sync_to_kb(name)
    # Step 5: 登记
    step5_log_to_registry(name, platform_info, github_info, kb_manifest)

    print(f"\n{'='*60}")
    print(f"✨ 更新完成！")
    print(f"   下一步: 在 memory_md 登记本次同步")
    print(f"{'='*60}\n")


def cmd_audit(args):
    name = args.name
    print(f"\n🔍 审计技能: {name}")
    reg = load_registry()
    if name not in reg.get("skills", {}):
        err(f"未在 sync-registry 中找到 {name}")
        return

    record = reg["skills"][name]
    skill_dir = Path(LOCAL_SKILLS_DIR) / name
    current_hash = compute_dir_hash(skill_dir)
    last_hash = record.get("local_hash", "")

    print(f"  本地路径: {record['local_path']}")
    print(f"  本地哈希: {current_hash} (上次同步: {last_hash})")
    print(f"  本地变更: {'⚠️ 有变更' if current_hash != last_hash else '✅ 一致'}")
    print(f"  平台: {record.get('platform', {}).get('status', '?')}")
    print(f"  GitHub: {record.get('github', {}).get('status', '?')}")
    print(f"  KB manifest: {len(record.get('kb', {}).get('files', []))} 个文件待上传")
    print(f"  上次同步: {record.get('last_sync', '?')}")


def cmd_audit_all(args):
    """全量审计：发现本地有但未登记的技能 / 登记了但本地缺失的（幽灵）"""
    print(f"\n{'='*60}")
    print(f"🔍 全量审计: 技能同步状态")
    print(f"{'='*60}\n")

    reg = load_registry()
    registered = set(reg.get("skills", {}).keys())

    # 扫描所有可能位置
    local_skills = set()
    for d in [LOCAL_SKILLS_DIR, WORKSPACE_SKILLS_DIR]:
        if Path(d).exists():
            for p in Path(d).iterdir():
                if p.is_dir() and (p / "SKILL.md").exists() and not p.name.startswith("."):
                    local_skills.add(p.name)

    # 三类
    ghosts = registered - local_skills  # 登记了但本地没了
    unregistered = local_skills - registered  # 本地有但没登记
    synced = local_skills & registered  # 都有的

    print(f"📊 统计:")
    print(f"  本地技能: {len(local_skills)}")
    print(f"  同步登记: {len(registered)}")
    print(f"  完整同步: {len(synced)}")
    print(f"  幽灵（登记无本地）: {len(ghosts)}")
    print(f"  未登记（本地无登记）: {len(unregistered)}")

    if ghosts:
        print(f"\n🔴 幽灵技能（建议从云端恢复或删除登记）:")
        for g in sorted(ghosts):
            print(f"   - {g}")
    if unregistered:
        print(f"\n🟡 未登记技能（建议立即同步）:")
        for u in sorted(unregistered):
            print(f"   - {u} → 运行: svc.py update {u}")


# ============================================================
# CLI
# ============================================================

def main():
    p = argparse.ArgumentParser(
        description="skill-version-control: 技能强制 3 处同步（git + 知识库 + 记忆）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  svc.py create omni-search "一体化搜索技能"
  svc.py update omni-search
  svc.py audit omni-search
  svc.py audit-all
        """,
    )
    sub = p.add_subparsers(dest="cmd")

    p_create = sub.add_parser("create", help="创建新技能（生成骨架 + 强制 3 处同步）")
    p_create.add_argument("name", help="技能名（kebab-case）")
    p_create.add_argument("description", help="description 字段内容")

    p_update = sub.add_parser("update", help="更新已存在技能")
    p_update.add_argument("name", help="技能名")

    p_audit = sub.add_parser("audit", help="审计单个技能同步状态")
    p_audit.add_argument("name", help="技能名")

    sub.add_parser("audit-all", help="全量审计所有技能")

    args = p.parse_args()
    if not args.cmd:
        p.print_help()
        return

    {"create": cmd_create, "update": cmd_update, "audit": cmd_audit, "audit-all": cmd_audit_all}[args.cmd](args)


if __name__ == "__main__":
    main()
