#!/usr/bin/env python3
"""
博查搜索 (Bocha Search) CLI 工具
使用博查AI搜索引擎进行联网搜索
"""

import os
import sys
import json
import argparse

import httpx


def bocha_search(query: str, count: int = 10, freshness: str = "noLimit") -> str:
    """
    执行博查搜索
    
    Args:
        query: 搜索关键词
        count: 返回结果数量 (1-50)
        freshness: 时间范围过滤
    
    Returns:
        格式化后的搜索结果
    """
    api_key = os.environ.get("BOCHA_API_KEY", "")
    
    if not api_key:
        return "错误: 博查API Key未配置。\n请设置环境变量 BOCHA_API_KEY\n获取地址: https://open.bochaai.com"
    
    endpoint = "https://api.bochaai.com/v1/web-search"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    
    payload = {
        "query": query,
        "summary": True,
        "freshness": freshness,
        "count": count
    }
    
    try:
        response = httpx.post(endpoint, headers=headers, json=payload, timeout=30.0)
        response.raise_for_status()
        resp = response.json()
        
        if "data" not in resp:
            return "搜索出错，请稍后重试。"
        
        data = resp["data"]
        
        if "webPages" not in data:
            return "未找到相关结果。"
        
        results = data["webPages"]["value"]
        
        if not results:
            return "未找到相关结果。"
        
        # 格式化输出
        output = []
        for i, result in enumerate(results, 1):
            title = result.get("name", "无标题")
            url = result.get("url", "")
            summary = result.get("summary", "")
            date_published = result.get("datePublished", "")
            site_name = result.get("siteName", "")
            
            output.append(f"{i}. {title}")
            if date_published:
                output.append(f"   📅 {date_published}")
            if site_name:
                output.append(f"   🏢 {site_name}")
            if summary:
                output.append(f"   📝 {summary}")
            if url:
                output.append(f"   🔗 {url}")
            output.append("")
        
        return "\n".join(output).strip()
    
    except httpx.HTTPStatusError as e:
        return f"HTTP错误: {e.response.status_code} - {e.response.text}"
    except httpx.RequestError as e:
        return f"网络错误: {str(e)}"
    except Exception as e:
        return f"未知错误: {str(e)}"


def main():
    parser = argparse.ArgumentParser(description="博查搜索 - AI搜索引擎")
    parser.add_argument("query", nargs="?", help="搜索关键词")
    parser.add_argument("count", nargs="?", type=int, default=10, help="返回结果数量 (1-50)")
    parser.add_argument("--freshness", "-f", default="noLimit", 
                        choices=["noLimit", "oneDay", "oneWeek", "oneMonth", "oneYear"],
                        help="时间范围过滤")
    
    args = parser.parse_args()
    
    if not args.query:
        parser.print_help()
        print("\n示例:")
        print("  python3 bocha_search.py '人工智能'")
        print("  python3 bocha_search.py '新闻' 20")
        print("  python3 bocha_search.py '科技动态' --freshness oneWeek")
        return
    
    result = bocha_search(args.query, args.count, args.freshness)
    print(result)


if __name__ == "__main__":
    main()