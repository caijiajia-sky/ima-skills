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
import base64
import re

# ============== 配置 ==============
API_KEY = os.environ.get("MINIMAX_API_KEY", "your_api_key_here")
API_HOST = "https://api.minimaxi.com"
ENDPOINT = "/v1/coding_plan/vlm"

# ============== 工具函数 ==============
def load_image_as_base64(image_path: str) -> str:
    """
    将本地图片转换为 base64 data URL
    
    Args:
        image_path: 图片文件路径
        
    Returns:
        base64 data URL 字符串
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"图片文件不存在: {image_path}")
    
    # 获取文件扩展名确定 MIME 类型
    ext = os.path.splitext(image_path)[1].lower()
    mime_types = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".webp": "image/webp",
        ".gif": "image/gif"
    }
    mime_type = mime_types.get(ext, "image/jpeg")
    
    # 读取并编码
    with open(image_path, "rb") as f:
        image_data = base64.b64encode(f.read()).decode("utf-8")
    
    return f"data:{mime_type};base64,{image_data}"


def is_url(text: str) -> bool:
    """检查字符串是否为 URL"""
    url_pattern = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain
        r'localhost|'  # localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # IP address
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return bool(url_pattern.match(text))


def fetch_url_as_base64(url: str) -> str:
    """
    获取远程图片并转换为 base64 data URL
    
    Args:
        url: 图片 URL
        
    Returns:
        base64 data URL 字符串
    """
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            content_type = response.headers.get("Content-Type", "image/jpeg")
            data = response.read()
            encoded = base64.b64encode(data).decode("utf-8")
            return f"data:{content_type};base64,{encoded}"
    except Exception as e:
        raise Exception(f"无法获取图片: {e}")


# ============== API 调用 ==============
def analyze_image(image_source: str, prompt: str = "描述这张图片的内容") -> str:
    """
    分析图片并返回描述
    
    Args:
        image_source: 图片路径或 URL
        prompt: 分析提示词
        
    Returns:
        图片分析结果文本
    """
    url = f"{API_HOST}{ENDPOINT}"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    
    # 处理图片输入
    if is_url(image_source):
        image_url = image_source
    elif os.path.exists(image_source):
        image_url = load_image_as_base64(image_source)
    else:
        raise ValueError(f"无效的图片源: {image_source}，请提供有效的文件路径或 URL")
    
    payload = {
        "prompt": prompt,
        "image_url": image_url
    }
    
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    
    try:
        with urllib.request.urlopen(req, timeout=120) as response:
            result = json.loads(response.read().decode("utf-8"))
            return result.get("content", str(result))
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8") if e.fp else ""
        raise Exception(f"HTTP Error {e.code}: {error_body}")
    except urllib.error.URLError as e:
        raise Exception(f"Network Error: {e.reason}")


# ============== 主函数 ==============
def main():
    image_source = None
    prompt = "描述这张图片的内容"
    
    # 解析命令行参数
    args = sys.argv[1:]
    i = 0
    while i < len(args):
        arg = args[i]
        if arg in ("-i", "--image") and i + 1 < len(args):
            image_source = args[i + 1]
            i += 2
        elif arg in ("-p", "--prompt") and i + 1 < len(args):
            prompt = args[i + 1]
            i += 2
        elif arg in ("-h", "--help"):
            print("用法: python analyze.py [选项] <图片路径或URL> [分析提示词]")
            print("")
            print("选项:")
            print("  -i, --image <路径>     图片文件路径或 URL")
            print("  -p, --prompt <提示>   分析提示词")
            print("  -h, --help            显示帮助信息")
            sys.exit(0)
        elif not arg.startswith("-"):
            if image_source is None:
                image_source = arg
            else:
                prompt = arg
            i += 1
        else:
            i += 1
    
    if not image_source:
        print("用法: python analyze.py \"图片路径或URL\" [分析提示词]")
        print("   或: python analyze.py --image \"图片路径\" --prompt \"分析提示词\"")
        sys.exit(1)
    
    try:
        print(f"🖼️  正在分析图片: {image_source}")
        result = analyze_image(image_source, prompt)
        print("\n📋 分析结果:")
        print("-" * 50)
        print(result)
    except Exception as e:
        print(f"❌ 分析失败: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()