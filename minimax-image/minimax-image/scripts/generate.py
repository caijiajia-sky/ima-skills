#!/usr/bin/env python3
"""
MiniMax 文生图 Skill
使用 MiniMax Token Plan API 生成图片

用法:
    python generate.py "提示词"
    python generate.py "提示词" --aspect-ratio 16:9 --n 2
    python generate.py "提示词" --output-dir ./images --prefix my_image
"""

import json
import urllib.request
import urllib.parse
import urllib.error
import sys
import os
import base64
import time

# ============== 配置 ==============
API_KEY = "sk-cp-BC0OPAa8Y5HiiKOIHZpC4WRiBF3PEeGXDl2WgAaG7mRI7WHsGXhMdQWXErRKZvrNu6gH_iH-tTMjQsozFC_akhP9VOPJSxh1gMzb-P2KchmzTXBRGjZWBbY"
API_HOST = "https://api.minimaxi.com"
ENDPOINT = "/v1/image_generation"

# 支持的比例
ASPECT_RATIOS = ["1:1", "16:9", "9:16", "4:3", "3:4", "3:2", "2:3", "21:9"]

# ============== API 调用 ==============
def generate_image(
    prompt: str,
    model: str = "image-01",
    aspect_ratio: str = "1:1",
    n: int = 1
) -> list:
    """
    生成图片
    
    Args:
        prompt: 图片描述提示词
        model: 模型名称，默认 image-01
        aspect_ratio: 宽高比，默认 1:1
        n: 生成数量，默认 1
        
    Returns:
        base64 编码的图片数据列表
    """
    url = f"{API_HOST}{ENDPOINT}"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    
    payload = {
        "model": model,
        "prompt": prompt,
        "aspect_ratio": aspect_ratio,
        "n": n
    }
    
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    
    try:
        with urllib.request.urlopen(req, timeout=180) as response:
            result = json.loads(response.read().decode("utf-8"))
            
            images = []
            if "data" in result and isinstance(result["data"], list):
                for item in result["data"]:
                    if "b64_image" in item:
                        images.append(item["b64_image"])
            elif "images" in result and isinstance(result["images"], list):
                for item in result["images"]:
                    if "b64_image" in item:
                        images.append(item["b64_image"])
            elif "image" in result:
                images.append(result["image"])
            
            return images
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8") if e.fp else ""
        raise Exception(f"HTTP Error {e.code}: {error_body}")
    except urllib.error.URLError as e:
        raise Exception(f"Network Error: {e.reason}")


# ============== 文件保存 ==============
def save_images(images: list, output_dir: str, prefix: str) -> list:
    """
    保存 base64 图片到文件
    
    Args:
        images: base64 编码的图片数据列表
        output_dir: 输出目录
        prefix: 文件名前缀
        
    Returns:
        保存的文件路径列表
    """
    os.makedirs(output_dir, exist_ok=True)
    
    saved_paths = []
    timestamp = int(time.time())
    
    for i, b64_data in enumerate(images):
        # 解码 base64
        image_bytes = base64.b64decode(b64_data)
        
        # 生成文件名
        filename = f"{prefix}_{timestamp}_{i+1}.png"
        filepath = os.path.join(output_dir, filename)
        
        # 保存文件
        with open(filepath, "wb") as f:
            f.write(image_bytes)
        
        saved_paths.append(filepath)
        print(f"✅ 已保存: {filepath}")
    
    return saved_paths


# ============== 主函数 ==============
def main():
    prompt = None
    aspect_ratio = "1:1"
    n = 1
    output_dir = "."
    prefix = "generated"
    
    # 解析命令行参数
    args = sys.argv[1:]
    i = 0
    while i < len(args):
        arg = args[i]
        
        if arg in ("-r", "--aspect-ratio") and i + 1 < len(args):
            aspect_ratio = args[i + 1]
            i += 2
        elif arg in ("-n", "--num") and i + 1 < len(args):
            n = int(args[i + 1])
            i += 2
        elif arg in ("-o", "--output-dir") and i + 1 < len(args):
            output_dir = args[i + 1]
            i += 2
        elif arg in ("-p", "--prefix") and i + 1 < len(args):
            prefix = args[i + 1]
            i += 2
        elif arg in ("-h", "--help"):
            print("用法: python generate.py <提示词> [选项]")
            print("")
            print("参数:")
            print("  <提示词>                    图片描述")
            print("")
            print("选项:")
            print("  -r, --aspect-ratio <比例>   宽高比 (1:1, 16:9, 9:16, 4:3, 3:4, 3:2, 2:3, 21:9)")
            print("  -n, --num <数量>            生成数量 (1-9)")
            print("  -o, --output-dir <目录>     输出目录")
            print("  -p, --prefix <前缀>         文件名前缀")
            print("  -h, --help                  显示帮助")
            sys.exit(0)
        elif not arg.startswith("-"):
            prompt = arg
            i += 1
        else:
            i += 1
    
    if not prompt:
        print("用法: python generate.py \"图片描述提示词\"")
        print("   或: python generate.py \"描述\" --aspect-ratio 16:9 --n 2")
        print("")
        print("支持的宽高比:", ", ".join(ASPECT_RATIOS))
        sys.exit(1)
    
    # 验证参数
    if aspect_ratio not in ASPECT_RATIOS:
        print(f"❌ 不支持的宽高比: {aspect_ratio}")
        print(f"   支持: {', '.join(ASPECT_RATIOS)}")
        sys.exit(1)
    
    if n < 1 or n > 9:
        print("❌ 生成数量必须在 1-9 之间")
        sys.exit(1)
    
    try:
        print(f"🎨 正在生成图片...")
        print(f"   提示词: {prompt}")
        print(f"   宽高比: {aspect_ratio}")
        print(f"   数量: {n}")
        print()
        
        images = generate_image(prompt, aspect_ratio=aspect_ratio, n=n)
        
        if images:
            saved_paths = save_images(images, output_dir, prefix)
            print()
            print(f"✨ 成功生成 {len(saved_paths)} 张图片!")
        else:
            print("❌ 未获取到图片数据")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ 生成失败: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()