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


def github_api_upload_file(repo: str, path: str, content: bytes, message: str, branch: str = "main", token: str = "") -> dict:
    """通过 GitHub Contents API 上传单个文件（比 git push 更稳定）"""
    import base64
    if not token:
        return {"status": "fail", "error": "no token"}
    url = f"https://api.github.com/repos/{repo}/contents/{path}"
    payload = {
        "message": message,
        "content": base64.b64encode(content).decode("utf-8"),
        "branch": branch,
    }
    try:
        r = subprocess.run(
            ["curl", "-s", "-X", "PUT", url,
             "-H", f"Authorization: token {token}",
             "-H", "Content-Type: application/json",
             "-d", json.dumps(payload)],
            capture_output=True, text=True, timeout=30,
        )
        result = json.loads(r.stdout)
        if "content" in result:
            return {"status": "ok", "sha": result["content"]["sha"], "commit": result["commit"]["sha"][:10]}
        return {"status": "fail", "error": result.get("message", r.stdout[:200])}
    except Exception as e:
        return {"status": "fail", "error": str(e)}


def step3_sync_to_github(name: str, commit_msg: str = None) -> dict:
    """Step 3: 同步到 GitHub 仓库（GitHub Contents API 优先，git push 兜底）"""
    print(f"\n🐙 Step 3: 同步到 GitHub [{GITHUB_REPO}]")
    src = Path(LOCAL_SKILLS_DIR) / name
    if not src.exists():
        err(f"本地目录不存在: {src}")
        return {"status": "fail", "error": "local not found"}

    token = os.environ.get("GITHUB_TOKEN", "")
    if not token:
        warn("GITHUB_TOKEN 未设置，跳过 GitHub 同步（其他同步步骤继续）")
        return {"status": "skipped", "reason": "no token"}

    msg = commit_msg or f"sync: {name} @ {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    uploaded = 0
    failed = []

    # 收集所有非 __pycache__ 文件
    files = []
    for p in src.rglob("*"):
        if p.is_file() and "__pycache__" not in str(p) and not p.name.startswith("."):
            rel = p.relative_to(src)
            files.append((p, str(rel)))

    info(f"准备上传 {len(files)} 个文件（GitHub Contents API）")
    for src_path, rel_path in files:
        result = github_api_upload_file(
            repo=GITHUB_REPO,
            path=f"{name}/{rel_path}",
            content=src_path.read_bytes(),
            message=msg,
            branch="main",
            token=token,
        )
        if result["status"] == "ok":
            uploaded += 1
        else:
            failed.append((rel_path, result.get("error", "")))

    if not failed:
        ok(f"全部上传成功: {uploaded} 个文件")
        return {"status": "ok", "uploaded": uploaded, "method": "api"}
    elif uploaded > 0:
        warn(f"部分失败: {uploaded} 成功 / {len(failed)} 失败")
        for f, e in failed[:5]:
            err(f"  {f}: {e[:100]}")
        return {"status": "partial", "uploaded": uploaded, "failed": failed, "method": "api"}
    else:
        err(f"全部失败（{len(failed)} 个）")
        for f, e in failed[:5]:
            err(f"  {f}: {e[:100]}")
        return {"status": "fail", "failed": failed, "method": "api"}


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


def step_restore_from_github(name: str, force: bool = False, target: str = "both") -> dict:
    """Step R: 从 GitHub 远端恢复技能（兜底机制）

    target: "both"=本地+workspace, "local"=仅/root/.skills, "workspace"=仅workspace
    """
    print(f"\n📥 Step R: 从 GitHub 恢复 [{name}]")
    info(f"源: https://github.com/{GITHUB_REPO}/tree/main/{name}")

    token = os.environ.get("GITHUB_TOKEN", "")
    if not token:
        warn("GITHUB_TOKEN 未设置，可能因权限不足无法访问远端")
        warn("如需认证访问，从 ima-knowledge 技能 SKILL.md 查找 GitHub Token 配置")
    headers = {"Authorization": f"token {token}"} if token else {}

    # 检查远端是否存在
    rc, out, _ = run(
        f'curl -s -o /dev/null -w "%{{http_code}}" '
        f'-H "Authorization: token {token}" '
        f'https://api.github.com/repos/{GITHUB_REPO}/contents/{name}?ref=main'
        if token else
        f'curl -s -o /dev/null -w "%{{http_code}}" '
        f'https://api.github.com/repos/{GITHUB_REPO}/contents/{name}?ref=main'
    )
    if rc != 0 or out.strip() not in ("200",):
        err(f"远端不存在 {name}（HTTP {out}）")
        return {"status": "not_found", "http": out}

    # 用 tarball 拉取（最快）
    info("下载 tarball...")
    tarball_url = f"https://api.github.com/repos/{GITHUB_REPO}/tarball/main"
    tmpdir = Path("/tmp/svc-restore")
    if tmpdir.exists():
        shutil.rmtree(tmpdir)
    tmpdir.mkdir(parents=True)

    rc, _, stderr = run(f"curl -s -L -o {tmpdir}/repo.tar.gz {tarball_url}")
    if rc != 0:
        err(f"下载失败: {stderr}")
        return {"status": "download_fail"}

    rc, _, stderr = run(f"cd {tmpdir} && tar -xzf repo.tar.gz")
    if rc != 0:
        err(f"解压失败: {stderr}")
        return {"status": "extract_fail"}

    extracted = list(tmpdir.glob("caijiajia-sky-ima-skills-*"))
    if not extracted:
        err("找不到解压目录")
        return {"status": "extract_fail"}
    skill_src = extracted[0] / name
    if not skill_src.exists():
        err(f"tarball 中没有 {name} 目录")
        return {"status": "not_in_tarball"}

    ok(f"下载完成: {len(list(skill_src.rglob('*')))} 个文件")

    # 恢复目标
    targets = []
    if target in ("both", "local"):
        targets.append(Path(LOCAL_SKILLS_DIR) / name)
    if target in ("both", "workspace"):
        targets.append(Path(WORKSPACE_SKILLS_DIR) / name)

    restored_to = []
    for dst in targets:
        dst.parent.mkdir(parents=True, exist_ok=True)
        if dst.exists():
            if not force:
                warn(f"目标已存在: {dst}（用 --force 覆盖）")
                continue
            warn(f"覆盖现有: {dst}")
            shutil.rmtree(dst)
        shutil.copytree(skill_src, dst)
        ok(f"恢复 → {dst}")
        restored_to.append(str(dst))

    # 清理临时
    shutil.rmtree(tmpdir)

    # 更新 registry
    reg = load_registry()
    if name in reg["skills"]:
        reg["skills"][name]["local_path"] = str(Path(LOCAL_SKILLS_DIR) / name)
        reg["skills"][name]["local_hash"] = compute_dir_hash(Path(LOCAL_SKILLS_DIR) / name)
        reg["skills"][name]["last_restore"] = datetime.now().isoformat()
        reg["skills"][name]["restore_source"] = "github"
    save_registry(reg)
    ok("已更新 sync-registry.json")

    return {"status": "ok", "restored_to": restored_to, "source": "github"}


def cmd_restore(args):
    """从 GitHub 远端恢复单个技能"""
    name = args.name
    print(f"\n{'='*60}")
    print(f"📥 skill-version-control: 从 GitHub 恢复 [{name}]")
    print(f"{'='*60}")
    result = step_restore_from_github(name, force=args.force, target=args.target)
    if result.get("status") == "ok":
        print(f"\n{'='*60}")
        print(f"✨ 恢复完成！")
        print(f"   建议运行: svc.py audit {name} 验证同步状态")
        print(f"{'='*60}\n")
    else:
        err(f"恢复失败: {result}")
        sys.exit(1)


def cmd_restore_all(args):
    """全量恢复：对比远端 vs 本地，列出差异 + 一键恢复"""
    print(f"\n{'='*60}")
    print(f"📥 skill-version-control: 全量恢复（远端 vs 本地）")
    print(f"{'='*60}\n")

    token = os.environ.get("GITHUB_TOKEN", "")
    if not token:
        err("GITHUB_TOKEN 未设置，无法拉取远端清单")
        sys.exit(1)

    # 拉远端清单
    info("拉取远端技能清单...")
    rc, out, stderr = run(
        f'curl -s "https://api.github.com/repos/{GITHUB_REPO}/contents/?ref=main" '
        f'-H "Authorization: token {token}"'
    )
    if rc != 0:
        err(f"远端 API 失败: {stderr}")
        sys.exit(1)
    try:
        remote_items = json.loads(out)
    except Exception as e:
        err(f"解析远端响应失败: {e}")
        sys.exit(1)

    remote_skills = {x["name"] for x in remote_items
                     if x.get("type") == "dir"} - {".github"}

    # 本地清单
    local_skills = set()
    for d in [LOCAL_SKILLS_DIR, WORKSPACE_SKILLS_DIR]:
        if Path(d).exists():
            for p in Path(d).iterdir():
                if p.is_dir() and (p / "SKILL.md").exists() and not p.name.startswith("."):
                    local_skills.add(p.name)

    # 三类
    remote_only = remote_skills - local_skills  # 远端有本地没 → 需要恢复
    local_only = local_skills - remote_skills  # 本地有远端没 → 异常
    both = remote_skills & local_skills  # 都有

    print(f"📊 统计:")
    print(f"   远端技能: {len(remote_skills)}")
    print(f"   本地技能: {len(local_skills)}")
    print(f"   两端都有: {len(both)}")
    print(f"   🟡 仅远端（建议恢复）: {len(remote_only)}")
    print(f"   ⚠️  仅本地（异常/未上传）: {len(local_only)}")

    if remote_only:
        print(f"\n🟡 仅远端有的技能:")
        for s in sorted(remote_only):
            print(f"   - {s}")

    if local_only:
        print(f"\n⚠️  仅本地有的技能（异常，需要上传到远端）:")
        for s in sorted(local_only):
            print(f"   - {s}")

    if not remote_only:
        print(f"\n✅ 远端所有技能本地都有，无需恢复")
        return

    # 自动恢复（除非 --dry-run）
    if args.dry_run:
        print(f"\n🔍 干跑模式，不实际恢复。运行 svc.py restore-all 实际执行")
        return

    print(f"\n🚀 开始批量恢复...")
    failed = []
    for s in sorted(remote_only):
        result = step_restore_from_github(s, force=False, target="both")
        if result.get("status") != "ok":
            failed.append(s)
            err(f"  {s} 失败: {result}")
        else:
            ok(f"  {s} 恢复成功")

    print(f"\n{'='*60}")
    print(f"✨ 批量恢复完成：成功 {len(remote_only) - len(failed)} / 失败 {len(failed)}")
    if failed:
        print(f"   失败列表: {failed}")
    print(f"{'='*60}\n")


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

    # 新增：检查远端（如果有 Token）
    token = os.environ.get("GITHUB_TOKEN", "")
    remote_skills = set()
    if token:
        rc, out, _ = run(
            f'curl -s "https://api.github.com/repos/{GITHUB_REPO}/contents/?ref=main" '
            f'-H "Authorization: token {token}"'
        )
        if rc == 0:
            try:
                items = json.loads(out)
                remote_skills = {x["name"] for x in items if x.get("type") == "dir"} - {".github"}
            except Exception:
                pass

    print(f"📊 统计:")
    print(f"  本地技能: {len(local_skills)}")
    print(f"  同步登记: {len(registered)}")
    print(f"  远端技能: {len(remote_skills) if remote_skills else '(未配置 GITHUB_TOKEN)'}")
    print(f"  完整同步: {len(synced)}")
    print(f"  幽灵（登记无本地）: {len(ghosts)}")
    print(f"  未登记（本地无登记）: {len(unregistered)}")
    if remote_skills:
        remote_only = remote_skills - local_skills
        print(f"  🟡 仅远端（可恢复）: {len(remote_only)}")

    if ghosts:
        print(f"\n🔴 幽灵技能（建议从 GitHub 恢复或删除登记）:")
        for g in sorted(ghosts):
            print(f"   - {g}")
            print(f"     → 恢复: svc.py restore {g}")
    if unregistered:
        print(f"\n🟡 未登记技能（建议立即同步）:")
        for u in sorted(unregistered):
            print(f"   - {u} → 运行: svc.py update {u}")
    if remote_skills:
        remote_only = remote_skills - local_skills
        if remote_only:
            print(f"\n🟢 仅远端有的技能（建议从 GitHub 拉回）:")
            for r in sorted(remote_only):
                print(f"   - {r} → 恢复: svc.py restore {r}")
            print(f"   或一键恢复: svc.py restore-all")


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

    p_restore = sub.add_parser("restore", help="从 GitHub 远端恢复单个技能")
    p_restore.add_argument("name", help="技能名")
    p_restore.add_argument("--force", action="store_true", help="强制覆盖本地")
    p_restore.add_argument("--target", choices=["both", "local", "workspace"],
                           default="both", help="恢复到哪个位置")

    p_restore_all = sub.add_parser("restore-all", help="全量恢复（远端 vs 本地）")
    p_restore_all.add_argument("--dry-run", action="store_true", help="只看差异不实际恢复")

    args = p.parse_args()
    if not args.cmd:
        p.print_help()
        return

    cmd_map = {
        "create": cmd_create,
        "update": cmd_update,
        "audit": cmd_audit,
        "audit-all": cmd_audit_all,
        "restore": cmd_restore,
        "restore-all": cmd_restore_all,
    }
    cmd_map[args.cmd](args)


if __name__ == "__main__":
    main()
