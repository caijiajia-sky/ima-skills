#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
⚠️  安全说明: API Key 通过环境变量传入
使用前请设置: export MINIMAX_API_KEY=your_actual_key
或创建 .env 文件（不要提交到git）
"""


import os
import sys
import json
import base64
import urllib.request
import urllib.error

# API 配置
API_KEY = os.environ.get("MINIMAX_API_KEY", "your_api_key_here")
API_HOST = "https://api.minimaxi.com"


def api_request(path, payload):
    """发送 API 请求到 MiniMax"""
    url = f"{API_HOST}{path}"
    data = json.dumps(payload).encode('utf-8')
    
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {API_KEY}'
        },
        method='POST'
    )
    
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            return json.loads(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8') if e.fp else str(e)
        raise Exception(f"API 请求失败 (状态码 {e.code}): {error_body}")
    except urllib.error.URLError as e:
        raise Exception(f"网络请求失败: {e.reason}")


def web_search(query):
    """执行网络搜索"""
    if not query or not query.strip():
        raise ValueError("搜索关键词不能为空")
    
    result = api_request('/v1/coding_plan/search', {"q": query.strip()})
    return result


def understand_image(prompt, image_source):
    """分析图片"""
    if not prompt or not prompt.strip():
        raise ValueError("分析提示词不能为空")
    if not image_source or not image_source.strip():
        raise ValueError("图片来源不能为空")
    
    # 处理图片 URL 或本地文件
    image_source = image_source.strip()
    
    if image_source.startswith('http://') or image_source.startswith('https://'):
        # 远程图片 - 下载并转为 base64
        try:
            with urllib.request.urlopen(image_source, timeout=30) as response:
                content_type = response.headers.get('content-type', 'image/png')
                image_data = response.read()
                base64_data = base64.b64encode(image_data).decode('utf-8')
                image_url = f"data:{content_type};base64,{base64_data}"
        except Exception as e:
            raise ValueError(f"无法访问图片 URL: {image_source}, 错误: {e}")
    elif image_source.startswith('data:'):
        # 已经是 data URL
        image_url = image_source
    else:
        # 本地文件路径
        file_path = image_source.lstrip('@')
        try:
            with open(file_path, 'rb') as f:
                image_data = f.read()
            # 获取文件扩展名确定 MIME 类型
            ext = os.path.splitext(file_path)[1].lower()
            mime_type = 'image/jpeg' if ext == '.jpg' else f'image/{ext[1:]}'
            base64_data = base64.b64encode(image_data).decode('utf-8')
            image_url = f"data:{mime_type};base64,{base64_data}"
        except FileNotFoundError:
            raise ValueError(f"找不到图片文件: {file_path}")
        except Exception as e:
            raise ValueError(f"无法读取图片文件: {file_path}, 错误: {e}")
    
    result = api_request('/v1/coding_plan/vlm', {
        "prompt": prompt.strip(),
        "image_url": image_url
    })
    
    # 提取返回的内容
    content = result.get('content', '')
    if not content:
        base_resp = result.get('base_resp', {})
        error_msg = json.dumps(base_resp, ensure_ascii=False, indent=2)
        raise Exception(f"图片理解失败，未返回内容。错误信息: {error_msg}")
    
    return {"content": content}


def main():
    if len(sys.argv) < 2:
        print("用法:")
        print("  python3 minimax_tools.py web_search \"搜索关键词\"")
        print("  python3 minimax_tools.py understand_image \"分析提示词\" \"图片URL或路径\"")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == 'web_search':
        if len(sys.argv) < 3:
            print("错误: web_search 需要提供搜索关键词")
            print("用法: python3 minimax_tools.py web_search \"搜索关键词\"")
            sys.exit(1)
        query = sys.argv[2]
        try:
            result = web_search(query)
            print(json.dumps(result, ensure_ascii=False, indent=2))
        except Exception as e:
            print(f"错误: {e}", file=sys.stderr)
            sys.exit(1)
    
    elif command == 'understand_image':
        if len(sys.argv) < 4:
            print("错误: understand_image 需要提供提示词和图片来源")
            print("用法: python3 minimax_tools.py understand_image \"分析提示词\" \"图片URL或路径\"")
            sys.exit(1)
        prompt = sys.argv[2]
        image_source = sys.argv[3]
        try:
            result = understand_image(prompt, image_source)
            print(json.dumps(result, ensure_ascii=False, indent=2))
        except Exception as e:
            print(f"错误: {e}", file=sys.stderr)
            sys.exit(1)
    
    else:
        print(f"错误: 未知命令 '{command}'")
        print("支持的命令: web_search, understand_image")
        sys.exit(1)


if __name__ == '__main__':
    main()