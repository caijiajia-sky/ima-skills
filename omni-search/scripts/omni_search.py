#!/usr/bin/env python3
"""
一体化极致搜索 CLI 工具
综合 4 大搜索源：系统内置搜索、博查、MiniMax、知识库

设计原则：
- 单次调用 = 一次最大化检索
- 多源并行 + 自动去重 + 交叉验证
- 私有知识优先，公共网络补全
- 时效性话题自动加日期
- 模糊查询自动扩写为多组关键词
"""

import os
import sys
import json
import argparse
import re
import time
from datetime import datetime
from typing import List, Dict, Any, Optional
from urllib.parse import urlparse

try:
    import httpx
except ImportError:
    httpx = None

try:
    import urllib.request
    import urllib.error
    import base64
except ImportError:
    pass


# ============================================================
# 配置
# ============================================================

BOCHA_API_KEY = os.environ.get("BOCHA_API_KEY", "")
BOCHA_ENDPOINT = "https://api.bochaai.com/v1/web-search"

MINIMAX_API_KEY = "sk-cp-BC0OPAa8Y5HiiKOIHZpC4WRiBF3PEeGXDl2WgAaG7mRI7WHsGXhMdQWXErRKZvrNu6gH_iH-tTMjQsozFC_akhP9VOPJSxh1gMzb-P2KchmzTXBRGjZWBbY"
MINIMAX_HOST = "https://api.minimaxi.com"

# 当前日期（用于时效性增强）
TODAY = datetime.now()
CURRENT_DATE_STR = TODAY.strftime("%Y年%m月%d日")
CURRENT_YEAR_MONTH = TODAY.strftime("%Y年%m月")


# ============================================================
# 工具函数
# ============================================================

def normalize_url(url: str) -> str:
    """URL 标准化用于去重"""
    if not url:
        return ""
    try:
        parsed = urlparse(url)
        # 去掉 fragment 和常见追踪参数
        netloc = parsed.netloc.replace("www.", "")
        path = parsed.path.rstrip("/")
        return f"{parsed.scheme}://{netloc}{path}".lower()
    except Exception:
        return url.lower()


def is_url(s: str) -> bool:
    return bool(s and (s.startswith("http://") or s.startswith("https://")))


def is_image_path(s: str) -> bool:
    if not s:
        return False
    s_lower = s.lower().lstrip("@")
    return any(s_lower.endswith(ext) for ext in [".jpg", ".jpeg", ".png", ".webp", ".gif", ".bmp"])


def time_range_for(topic_kind: str) -> str:
    """根据话题类型推断博查的 freshness 过滤值"""
    kind = (topic_kind or "").lower()
    if any(k in kind for k in ["新闻", "动态", "今日", "最新", "突发", "今天", "刚", "new", "today", "latest", "breaking"]):
        return "oneDay"
    if any(k in kind for k in ["本周", "这周", "周报", "weekly"]):
        return "oneWeek"
    if any(k in kind for k in ["本月", "这月", "月报", "monthly"]):
        return "oneMonth"
    if any(k in kind for k in ["今年", "年度", "年报", "yearly", "2024", "2025", "2026"]):
        return "oneYear"
    return "noLimit"


def expand_query(query: str, topic_kind: str = "") -> List[str]:
    """
    一组关键词 → 多组搜索关键词（极致利用）
    原则：
    - 主查询保留原貌
    - 时效性话题自动追加日期
    - 长查询提取关键实体并行检索
    """
    queries = [query.strip()]

    # 时效性增强
    freshness = time_range_for(topic_kind)
    if freshness in ("oneDay", "oneWeek", "oneMonth", "oneYear"):
        if not any(yr in query for yr in [str(y) for y in range(TODAY.year - 2, TODAY.year + 2)]):
            queries.append(f"{query} {CURRENT_DATE_STR}")

    # 长查询 → 拆出实体
    if len(query) > 15:
        # 先按标点/连接词分句
        chunks = re.split(r"[，,。；;的]", query)
        meaningful = [c.strip() for c in chunks if len(c.strip()) >= 4 and c.strip() != query]
        # 兜底：如果没标点可分，按空格/年份/数字边界拆
        if not meaningful and " " in query:
            words = query.split()
            # 抽包含行业词的短句（2-4 词）
            for i in range(len(words)):
                for j in range(i + 1, min(i + 5, len(words) + 1)):
                    sub = " ".join(words[i:j])
                    if 4 <= len(sub) <= 12 and sub != query:
                        meaningful.append(sub)
        # 兜底2：中文长查询无空格 → 用关键词窗口
        if not meaningful:
            keywords = ["行业", "技术", "发展", "研究", "方法", "应用", "产品", "治疗", "应用"]
            for kw in keywords:
                if kw in query and len(query) - len(kw) >= 4:
                    idx = query.index(kw)
                    # 取关键词前后 4-8 个字
                    start = max(0, idx - 3)
                    end = min(len(query), idx + len(kw) + 3)
                    sub = query[start:end]
                    if sub != query and sub not in meaningful:
                        meaningful.append(sub)
                        break
        for m in meaningful[:2]:  # 最多加 2 组
            if m and m not in queries:
                queries.append(m)

    # 去重保序
    seen = set()
    out = []
    for q in queries:
        if q and q not in seen:
            seen.add(q)
            out.append(q)
    return out[:4]  # 最多 4 组，避免过度


# ============================================================
# 搜索源 1：博查
# ============================================================

def bocha_search(query: str, count: int = 10, freshness: str = "noLimit", timeout: float = 30.0) -> Dict[str, Any]:
    """
    博查 AI 搜索
    返回: {source, query, results: [...], error}
    """
    if not BOCHA_API_KEY:
        return {"source": "bocha", "query": query, "results": [], "error": "BOCHA_API_KEY 未配置"}
    if httpx is None:
        return {"source": "bocha", "query": query, "results": [], "error": "httpx 未安装"}

    headers = {
        "Authorization": f"Bearer {BOCHA_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "query": query,
        "summary": True,
        "freshness": freshness,
        "count": count,
    }

    try:
        resp = httpx.post(BOCHA_ENDPOINT, headers=headers, json=payload, timeout=timeout)
        resp.raise_for_status()
        data = resp.json().get("data", {})
        pages = data.get("webPages", {}).get("value", [])
        results = []
        for r in pages:
            results.append({
                "title": r.get("name", ""),
                "url": r.get("url", ""),
                "summary": r.get("summary", ""),
                "date": r.get("datePublished", ""),
                "site": r.get("siteName", ""),
            })
        return {"source": "bocha", "query": query, "freshness": freshness, "results": results, "error": None}
    except Exception as e:
        return {"source": "bocha", "query": query, "results": [], "error": str(e)}


# ============================================================
# 搜索源 2：MiniMax
# ============================================================

def minimax_request(path: str, payload: dict, timeout: float = 30.0) -> dict:
    url = f"{MINIMAX_HOST}{path}"
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {MINIMAX_API_KEY}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8") if e.fp else str(e)
        raise Exception(f"HTTP {e.code}: {body}")
    except urllib.error.URLError as e:
        raise Exception(f"网络错误: {e.reason}")


def minimax_web_search(query: str, timeout: float = 30.0) -> Dict[str, Any]:
    """MiniMax web_search"""
    try:
        result = minimax_request("/v1/coding_plan/search", {"q": query.strip()}, timeout=timeout)
        # 结果结构：organic + related_searches
        organic = result.get("organic") or result.get("results") or result.get("data", {}).get("organic") or []
        related = result.get("related_searches") or result.get("related") or []
        results = []
        for r in organic:
            if isinstance(r, dict):
                results.append({
                    "title": r.get("title") or r.get("name", ""),
                    "url": r.get("url") or r.get("link", ""),
                    "summary": r.get("snippet") or r.get("summary") or r.get("description", ""),
                    "date": r.get("date", ""),
                    "site": r.get("source") or r.get("site", ""),
                })
        return {
            "source": "minimax",
            "query": query,
            "results": results,
            "related": related if isinstance(related, list) else [],
            "raw": result,
            "error": None,
        }
    except Exception as e:
        return {"source": "minimax", "query": query, "results": [], "related": [], "error": str(e)}


def minimax_understand_image(prompt: str, image_source: str, timeout: float = 60.0) -> Dict[str, Any]:
    """MiniMax 图片理解（VLM）"""
    try:
        image_source = image_source.strip()
        if image_source.startswith(("http://", "https://")):
            with urllib.request.urlopen(image_source, timeout=30) as r:
                ct = r.headers.get("content-type", "image/png")
                b64 = base64.b64encode(r.read()).decode("utf-8")
                image_url = f"data:{ct};base64,{b64}"
        elif image_source.startswith("data:"):
            image_url = image_source
        else:
            fp = image_source.lstrip("@")
            with open(fp, "rb") as f:
                img_data = f.read()
            ext = os.path.splitext(fp)[1].lower()
            mime = "image/jpeg" if ext == ".jpg" else f"image/{ext.lstrip('.')}"
            b64 = base64.b64encode(img_data).decode("utf-8")
            image_url = f"data:{mime};base64,{b64}"

        result = minimax_request("/v1/coding_plan/vlm", {"prompt": prompt.strip(), "image_url": image_url}, timeout=timeout)
        content = result.get("content", "")
        if not content:
            base_resp = result.get("base_resp", {})
            return {"source": "minimax-vlm", "content": "", "error": f"未返回内容: {json.dumps(base_resp, ensure_ascii=False)}"}
        return {"source": "minimax-vlm", "content": content, "error": None}
    except Exception as e:
        return {"source": "minimax-vlm", "content": "", "error": str(e)}


# ============================================================
# 融合 / 去重
# ============================================================

def merge_and_dedupe(source_results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    多源结果融合去重
    - 同一 URL 只保留一次
    - 优先保留有 summary 的源
    - 标注来源（用 | 分隔多源）
    """
    seen = {}  # norm_url -> result
    for sr in source_results:
        for r in sr.get("results", []):
            url = r.get("url", "")
            key = normalize_url(url) if url else f"title:{r.get('title','')}"
            if not key:
                continue
            if key in seen:
                # 合并来源
                old = seen[key]
                src_set = set(old.get("sources", [old.get("source", "unknown")]))
                src_set.add(sr.get("source", "unknown"))
                old["sources"] = list(src_set)
                # 优先保留更详细的 summary
                if len(r.get("summary", "")) > len(old.get("summary", "")):
                    old["summary"] = r.get("summary", "")
                if not old.get("date") and r.get("date"):
                    old["date"] = r.get("date")
            else:
                r2 = dict(r)
                r2["sources"] = [sr.get("source", "unknown")]
                seen[key] = r2

    merged = list(seen.values())
    # 简单排序：有日期的优先 + 多源命中靠前
    def sort_key(r):
        src_count = len(r.get("sources", []))
        has_date = 1 if r.get("date") else 0
        return (src_count, has_date)

    merged.sort(key=sort_key, reverse=True)
    return merged


def format_results(merged: List[Dict[str, Any]], max_items: int = 20) -> str:
    """格式化输出（极致利用版：每条带来源标记）"""
    if not merged:
        return "（无结果）"

    lines = [f"共 {len(merged)} 条去重结果（已跨源合并，按命中数 × 时效性排序），展示前 {min(max_items, len(merged))} 条：", ""]
    for i, r in enumerate(merged[:max_items], 1):
        title = r.get("title") or "（无标题）"
        url = r.get("url", "")
        summary = r.get("summary", "")
        date = r.get("date", "")
        site = r.get("site", "")
        sources = "|".join(r.get("sources", []))

        lines.append(f"### {i}. {title}")
        if date:
            lines.append(f"- 📅 {date}")
        if site:
            lines.append(f"- 🏢 {site}")
        if sources:
            lines.append(f"- 🔍 命中来源：{sources}")
        if summary:
            lines.append(f"- 📝 {summary}")
        if url:
            lines.append(f"- 🔗 {url}")
        lines.append("")
    return "\n".join(lines)


# ============================================================
# 一体化入口
# ============================================================

def omni_search(query: str, sources: List[str], topic_kind: str = "", count: int = 10,
                kb_id: str = "", include_kb: bool = True, max_output: int = 20) -> Dict[str, Any]:
    """
    一体化搜索 - 极致利用版

    sources: 子集 ['bocha', 'minimax', 'web', 'kb', 'note'] 中的任意
             web / kb / note 由上层 search 工具处理（这里只返回占位）
    """
    queries = expand_query(query, topic_kind)
    freshness = time_range_for(topic_kind)

    bocha_results = []
    minimax_results = []
    minimax_related = []

    # 博查：跑多组关键词
    if "bocha" in sources:
        for q in queries:
            r = bocha_search(q, count=count, freshness=freshness)
            bocha_results.append(r)

    # MiniMax：跑多组关键词 + 合并 related
    if "minimax" in sources:
        for q in queries:
            r = minimax_web_search(q)
            minimax_results.append(r)
            minimax_related.extend(r.get("related", []))

    # 融合去重
    merged = merge_and_dedupe(bocha_results + minimax_results)

    return {
        "query": query,
        "expanded_queries": queries,
        "freshness": freshness,
        "bocha_raw": bocha_results,
        "minimax_raw": minimax_results,
        "minimax_related": list({r if isinstance(r, str) else json.dumps(r, ensure_ascii=False) for r in minimax_related}),
        "merged": merged,
        "summary": {
            "total_unique": len(merged),
            "bocha_hits": sum(len(r.get("results", [])) for r in bocha_results),
            "minimax_hits": sum(len(r.get("results", [])) for r in minimax_results),
            "errors": [r for r in bocha_results + minimax_results if r.get("error")],
        },
    }


# ============================================================
# CLI
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description="一体化极致搜索：博查 + MiniMax（系统内置搜索 / 知识库请用主对话的 search 工具）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 联网搜索（自动启用 bocha + MiniMax 双源融合）
  omni_search.py search "人工智能最新进展"

  # 指定时间范围 + 单源
  omni_search.py search "科技新闻" --topic news --sources bocha --count 15

  # 关键词扩展预览（不实际搜索）
  omni_search.py expand "深度学习在医疗影像中的应用"

  # 图片理解
  omni_search.py vlm "描述图片内容" https://example.com/x.jpg
        """,
    )

    sub = parser.add_subparsers(dest="cmd")

    p_search = sub.add_parser("search", help="一体化联网搜索")
    p_search.add_argument("query", help="搜索关键词")
    p_search.add_argument("--topic", default="", help="话题类型（news/tech/health/...），用于自动选 freshness 和关键词扩展")
    p_search.add_argument("--sources", default="bocha,minimax", help="逗号分隔的源：bocha,minimax")
    p_search.add_argument("--count", type=int, default=10, help="每个源每组关键词的结果数（默认 10）")
    p_search.add_argument("--max-output", type=int, default=20, help="最终展示条数")
    p_search.add_argument("--json", action="store_true", help="输出原始 JSON")

    p_expand = sub.add_parser("expand", help="仅做关键词扩展（不实际搜索）")
    p_expand.add_argument("query", help="原始查询")
    p_expand.add_argument("--topic", default="", help="话题类型")

    p_vlm = sub.add_parser("vlm", help="MiniMax 图片理解")
    p_vlm.add_argument("prompt", help="分析提示词")
    p_vlm.add_argument("image", help="图片 URL 或本地路径")

    args = parser.parse_args()

    if args.cmd == "search":
        sources = [s.strip() for s in args.sources.split(",") if s.strip()]
        out = omni_search(args.query, sources, topic_kind=args.topic, count=args.count, max_output=args.max_output)
        if args.json:
            print(json.dumps(out, ensure_ascii=False, indent=2))
        else:
            print(f"🔎 原始查询：{out['query']}")
            print(f"📌 话题类型：{args.topic or '（未指定）'}")
            print(f"⏱  时间范围（博查）：{out['freshness']}")
            print(f"🧠 关键词扩展：{out['expanded_queries']}")
            print()
            print(f"📊 命中统计：博查 {out['summary']['bocha_hits']} 条 / MiniMax {out['summary']['minimax_hits']} 条 / 去重后 {out['summary']['total_unique']} 条")
            if out["summary"]["errors"]:
                print(f"⚠️  错误：")
                for r in out["summary"]["errors"]:
                    print(f"   - [{r['source']}] {r.get('query','')}: {r.get('error','')}")
            print()
            print(format_results(out["merged"], args.max_output))
            if out.get("minimax_related"):
                print("\n💡 MiniMax 推荐相关搜索：")
                for rq in out["minimax_related"][:8]:
                    print(f"   - {rq}")

    elif args.cmd == "expand":
        out = expand_query(args.query, args.topic)
        print(json.dumps({"query": args.query, "topic": args.topic, "freshness": time_range_for(args.topic), "expanded": out}, ensure_ascii=False, indent=2))

    elif args.cmd == "vlm":
        result = minimax_understand_image(args.prompt, args.image)
        if result.get("error"):
            print(f"❌ {result['error']}", file=sys.stderr)
            sys.exit(1)
        print(result["content"])

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
