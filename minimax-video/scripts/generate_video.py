#!/usr/bin/env python3
"""
MiniMax Video Generation Script - 简化版
通过 MiniMax API 生成视频

用法:
    python generate_video.py --prompt "视频描述"
    python generate_video.py --prompt "描述" --duration 10 --resolution 1080p
"""

import urllib.request
import urllib.error
import json
import os
import sys
import time
import argparse


# ============== 配置 ==============
API_KEY = "sk-cp-BC0OPAa8Y5HiiKOIHZpC4WRiBF3PEeGXDl2WgAaG7mRI7WHsGXhMdQWXErRKZvrNu6gH_iH-tTMjQsozFC_akhP9VOPJSxh1gMzb-P2KchmzTXBRGjZWBbY"
API_HOST = "https://api.minimaxi.com"
ENDPOINT = "/v1/video_generation"
QUERY_ENDPOINT = "/v1/query/video_generation"
FILE_ENDPOINT = "/v1/files/retrieve"

# 模型选项
MODELS = ["MiniMax-Hailuo-2.3"]

# 时长选项
DURATIONS = [6, 10]

# 分辨率选项
RESOLUTIONS = ["768P", "1080P"]

# 帧率选项
FPS_OPTIONS = [24, 30]


# ============== API 调用 ==============

def submit_video_task(prompt: str, model: str = "MiniMax-Hailuo-2.3",
                     duration: int = 6, resolution: str = "768P",
                     fps: int = 24) -> dict:
    """提交视频生成任务"""
    url = f"{API_HOST}{ENDPOINT}"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": model,
        "prompt": prompt,
        "duration": duration,
        "resolution": resolution,
        "fps": fps
    }
    
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    
    try:
        with urllib.request.urlopen(req, timeout=60) as response:
            result = json.loads(response.read().decode("utf-8"))
            
            base_resp = result.get("base_resp", {})
            if base_resp.get("status_code", 0) != 0:
                error_msg = base_resp.get("status_msg", "未知错误")
                raise Exception(f"API 错误: {error_msg}")
            
            return result
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        raise Exception(f"HTTP Error {e.code}: {error_body}")
    except urllib.error.URLError as e:
        raise Exception(f"Network Error: {e.reason}")


def query_task_status(task_id: str) -> dict:
    """查询视频生成任务状态"""
    url = f"{API_HOST}{QUERY_ENDPOINT}?task_id={task_id}"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    
    req = urllib.request.Request(url, headers=headers, method="GET")
    
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            result = json.loads(response.read().decode("utf-8"))
            return result
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        raise Exception(f"HTTP Error {e.code}: {error_body}")
    except urllib.error.URLError as e:
        raise Exception(f"Network Error: {e.reason}")


def poll_until_complete(task_id: str, poll_interval: int = 10,
                        max_wait: int = 600) -> dict:
    """轮询等待任务完成"""
    start_time = time.time()
    poll_count = 0
    
    print(f"⏳ 任务已提交，等待生成... (task_id: {task_id})")
    print("   (视频生成可能需要 1-3 分钟，请耐心等待...)")
    
    while True:
        elapsed = time.time() - start_time
        
        if elapsed > max_wait:
            raise Exception(f"等待超时 ({max_wait}秒)")
        
        time.sleep(poll_interval)
        poll_count += 1
        
        try:
            result = query_task_status(task_id)
            # 状态可能在 data 中或直接在根级别
            data = result.get("data", result)
            status = data.get("status", "Unknown")
            
            status_text = {"Preparing": "准备中", "Queueing": "排队中", "Processing": "处理中", "Success": "成功", "Fail": "失败"}
            
            print(f"   [{poll_count}] 状态: {status_text.get(status, status)} ({elapsed:.0f}s)")
            
            if status == "Success":
                print("✅ 视频生成完成!")
                return data
            elif status == "Fail":
                error_msg = data.get("failed_reason", data.get("status_msg", "未知错误"))
                raise Exception(f"任务失败: {error_msg}")
        except Exception as e:
            # 如果查询失败，可能视频还在生成中，继续等待
            print(f"   [{poll_count}] 查询失败: {e}，继续等待...")
            if elapsed > 60:  # 超过60秒后可能真的有问题
                raise


def fetch_video_url(file_id: str) -> str:
    """通过 file_id 获取视频下载 URL"""
    url = f"{API_HOST}{FILE_ENDPOINT}?file_id={file_id}"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    
    req = urllib.request.Request(url, headers=headers, method="GET")
    
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            result = json.loads(response.read().decode("utf-8"))
            
            file_data = result.get("file", {})
            download_url = file_data.get("download_url", "")
            
            if not download_url:
                raise Exception("未获取到下载 URL")
            
            return download_url
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        raise Exception(f"HTTP Error {e.code}: {error_body}")
    except urllib.error.URLError as e:
        raise Exception(f"Network Error: {e.reason}")


def download_video(video_url: str, output_path: str) -> bool:
    """从 URL 下载视频文件"""
    try:
        print(f"📥 正在下载视频...")
        
        req = urllib.request.Request(video_url)
        with urllib.request.urlopen(req, timeout=300) as response:
            with open(output_path, "wb") as f:
                while True:
                    chunk = response.read(1024 * 1024)
                    if not chunk:
                        break
                    f.write(chunk)
        
        print(f"✅ 视频已保存: {output_path}")
        return True
    except Exception as e:
        print(f"❌ 下载失败: {str(e)}")
        return False


# ============== 主函数 ==============

def main():
    parser = argparse.ArgumentParser(description="MiniMax 视频生成工具")
    
    parser.add_argument("--prompt", "-p", required=True,
                        help="视频描述提示词（必填）")
    parser.add_argument("--model", "-m", default="MiniMax-Hailuo-2.3",
                        choices=MODELS,
                        help="模型版本，默认 MiniMax-Hailuo-2.3")
    parser.add_argument("--duration", "-d", type=int, default=6,
                        choices=DURATIONS,
                        help="视频时长(秒)，可选 6 或 10，默认 6")
    parser.add_argument("--resolution", "-r", default="768P",
                        choices=RESOLUTIONS,
                        help="分辨率，可选 768P 或 1080P，默认 768P")
    parser.add_argument("--fps", "-f", type=int, default=24,
                        choices=FPS_OPTIONS,
                        help="帧率，可选 24 或 30，默认 24")
    parser.add_argument("--output-dir", "-o", default="./videos",
                        help="输出目录，默认 ./videos")
    parser.add_argument("--output-name", "-n", default=None,
                        help="输出文件名，默认 video_{timestamp}.mp4")
    parser.add_argument("--poll-interval", "-i", type=int, default=10,
                        help="轮询间隔(秒)，默认 10")
    parser.add_argument("--max-wait", "-w", type=int, default=600,
                        help="最大等待时间(秒)，默认 600")
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("🎬 MiniMax 视频生成器")
    print("=" * 60)
    print(f"   提示词: {args.prompt}")
    print(f"   模型: {args.model}")
    print(f"   时长: {args.duration}秒")
    print(f"   分辨率: {args.resolution}")
    print(f"   帧率: {args.fps}fps")
    print("=" * 60)
    
    try:
        # 1. 提交任务
        print("\n📤 正在提交视频生成任务...")
        result = submit_video_task(
            prompt=args.prompt,
            model=args.model,
            duration=args.duration,
            resolution=args.resolution,
            fps=args.fps
        )
        
        # 获取 task_id
        task_id = result.get("task_id", "")
        
        if not task_id:
            raise Exception("未获取到 task_id")
        
        print(f"✅ 任务已提交: {task_id}")
        
        # 2. 轮询等待完成
        complete_data = poll_until_complete(
            task_id=task_id,
            poll_interval=args.poll_interval,
            max_wait=args.max_wait
        )
        
        # 3. 获取视频 URL 并下载
        # 先通过 file_id 获取下载链接
        file_id = complete_data.get("file_id", "")
        
        if not file_id:
            raise Exception("未获取到 file_id")
        
        print(f"📥 正在获取下载链接 (file_id: {file_id})...")
        video_url = fetch_video_url(file_id)
        
        if not video_url:
            raise Exception("未获取到视频 URL")
        
        # 准备输出路径
        os.makedirs(args.output_dir, exist_ok=True)
        
        if args.output_name:
            output_path = os.path.join(args.output_dir, args.output_name)
        else:
            timestamp = int(time.time())
            output_path = os.path.join(args.output_dir, f"video_{timestamp}.mp4")
        
        # 下载视频
        if download_video(video_url, output_path):
            file_size = os.path.getsize(output_path) / (1024 * 1024)
            print(f"\n🎉 视频生成成功!")
            print(f"   文件: {os.path.abspath(output_path)}")
            print(f"   大小: {file_size:.2f} MB")
            print(f"   task_id: {task_id}")
        else:
            sys.exit(1)
        
    except Exception as e:
        print(f"\n❌ 错误: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()