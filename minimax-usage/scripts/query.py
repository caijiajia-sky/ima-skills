#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
⚠️  安全说明: API Key 通过环境变量传入
使用前请设置: export MINIMAX_API_KEY=your_actual_key
或创建 .env 文件（不要提交到git）
"""

import json
import urllib.request
import urllib.parse
import urllib.error
import sys
import os

# ============== 配置 ==============
API_KEY = os.environ.get("MINIMAX_API_KEY", "your_api_key_here")
API_HOST = "https://api.minimaxi.com"
ENDPOINT = "/v1/api/openplatform/coding_plan/remains"

# ============== API 调用 ==============
def query_usage() -> dict:
    """
    查询 MiniMax Token Plan 用量
    
    Returns:
        用量信息字典
    """
    url = f"{API_HOST}{ENDPOINT}"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    
    req = urllib.request.Request(url, headers=headers, method="GET")
    
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            result = json.loads(response.read().decode("utf-8"))
            return result
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8") if e.fp else ""
        raise Exception(f"HTTP Error {e.code}: {error_body}")
    except urllib.error.URLError as e:
        raise Exception(f"Network Error: {e.reason}")


# ============== 格式化输出 ==============
def format_usage_table(data: dict) -> str:
    """格式化用量为表格"""
    output = []
    output.append("╔════════════════════════════════════════════════════════════╗")
    output.append("║           MiniMax Token Plan 用量查询                       ║")
    output.append("╠════════════════════════════════════════════════════════════╣")
    
    # 解析数据并显示
    if "data" in data:
        items = data["data"]
        if isinstance(items, dict):
            for key, value in items.items():
                # 格式化键名
                key_display = key.replace("_", " ").title()
                if isinstance(value, dict):
                    output.append(f"║  📊 {key_display}:")
                    for k, v in value.items():
                        output.append(f"║     {k}: {v}")
                else:
                    output.append(f"║  📊 {key_display}: {value}")
        elif isinstance(items, list):
            for item in items:
                if isinstance(item, dict):
                    name = item.get("name", item.get("model_name", "Unknown"))
                    remain = item.get("remain_quota", item.get("remain", "N/A"))
                    used = item.get("used_quota", item.get("used", "N/A"))
                    total = item.get("total_quota", item.get("total", "N/A"))
                    output.append(f"║  📦 {name}:")
                    output.append(f"║     已用: {used} | 剩余: {remain} | 总计: {total}")
    else:
        # 直接显示原始数据
        for key, value in data.items():
            if isinstance(value, dict):
                output.append(f"║  📊 {key}:")
                for k, v in value.items():
                    output.append(f"║     {k}: {v}")
            else:
                output.append(f"║  📊 {key}: {value}")
    
    output.append("╚════════════════════════════════════════════════════════════╝")
    
    return "\n".join(output)


def format_usage_json(data: dict) -> str:
    """格式化用量为 JSON"""
    return json.dumps(data, ensure_ascii=False, indent=2)


# ============== 主函数 ==============
def main():
    output_format = "table"
    
    # 解析命令行参数
    args = sys.argv[1:]
    for i, arg in enumerate(args):
        if arg in ("-f", "--format") and i + 1 < len(args):
            output_format = args[i + 1].lower()
        elif arg in ("-h", "--help"):
            print("用法: python query.py [选项]")
            print("")
            print("选项:")
            print("  -f, --format <格式>    输出格式 (table, json)")
            print("  -h, --help             显示帮助")
            print("")
            print("示例:")
            print("  python query.py                    # 表格格式输出")
            print("  python query.py --format json      # JSON 格式输出")
            sys.exit(0)
        elif arg.startswith("-"):
            continue
    
    if output_format not in ("table", "json"):
        print(f"❌ 不支持的输出格式: {output_format}")
        print("   支持: table, json")
        sys.exit(1)
    
    try:
        print("🔄 正在查询用量信息...")
        data = query_usage()
        
        if output_format == "json":
            print(format_usage_json(data))
        else:
            print(format_usage_table(data))
        
    except Exception as e:
        print(f"❌ 查询失败: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()