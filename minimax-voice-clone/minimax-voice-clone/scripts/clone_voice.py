#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
⚠️  安全说明: API Key 通过环境变量传入
使用前请设置: export MINIMAX_API_KEY=your_actual_key
或创建 .env 文件（不要提交到git）
"""

import argparse
import json
import os
import sys
import mimetypes

try:
    import requests
except ImportError:
    print("正在安装 requests 库...")
    os.system("pip install requests -q")
    import requests


# API 配置
API_HOST = "https://api.minimaxi.com"
API_KEY = os.environ.get("MINIMAX_API_KEY", "your_api_key_here")

# 默认测试文本
DEFAULT_TEXT = "您好，这是我的声音样本，请用于克隆音色。"


def get_fileMimeType(file_path: str) -> str:
    """获取文件的 MIME 类型"""
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type is None:
        # 尝试根据扩展名判断
        ext = os.path.splitext(file_path)[1].lower()
        mime_map = {
            '.mp3': 'audio/mpeg',
            '.m4a': 'audio/mp4',
            '.wav': 'audio/wav',
        }
        mime_type = mime_map.get(ext, 'audio/mpeg')
    return mime_type


def upload_audio_file(audio_file: str) -> dict:
    """
    上传音频文件获取 file_id
    
    Args:
        audio_file: 音频文件路径
        
    Returns:
        包含 file_id 的响应字典
    """
    if not os.path.exists(audio_file):
        raise FileNotFoundError(f"音频文件不存在: {audio_file}")
    
    # 检查文件扩展名
    ext = os.path.splitext(audio_file)[1].lower()
    if ext not in ['.mp3', '.m4a', '.wav']:
        raise ValueError("不支持的音频格式，请使用 mp3, m4a 或 wav 格式")
    
    mime_type = get_fileMimeType(audio_file)
    
    url = f"{API_HOST}/v1/files/upload"
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    
    with open(audio_file, 'rb') as f:
        files = {
            'file': (os.path.basename(audio_file), f, mime_type),
            'purpose': (None, 'voice_clone')
        }
        response = requests.post(url, headers=headers, files=files)
    
    if response.status_code != 200:
        raise RuntimeError(f"上传音频失败: {response.status_code} - {response.text}")
    
    result = response.json()
    return result


def clone_voice(file_id: str, voice_id: str, text: str = None) -> dict:
    """
    克隆声音
    
    Args:
        file_id: 上传音频返回的 file_id
        voice_id: 自定义的音色ID
        text: 测试文本
        
    Returns:
        克隆结果
    """
    url = f"{API_HOST}/v1/voice_clone"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "file_id": file_id,
        "voice_id": voice_id,
        "text": text or DEFAULT_TEXT,
        "model": "speech-2.8-hd"
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code != 200:
        raise RuntimeError(f"克隆声音失败: {response.status_code} - {response.text}")
    
    result = response.json()
    return result


def main():
    parser = argparse.ArgumentParser(
        description="MiniMax 声音克隆工具 - 上传音频并克隆声音"
    )
    parser.add_argument(
        '--audio-file', '-a',
        required=True,
        help='音频文件路径 (支持 mp3, m4a, wav 格式，时长 10秒-5分钟)'
    )
    parser.add_argument(
        '--voice-id', '-v',
        required=True,
        help='自定义音色ID（用于标识克隆的声音）'
    )
    parser.add_argument(
        '--text', '-t',
        default=None,
        help='测试文本（可选，默认使用内置示例文本）'
    )
    parser.add_argument(
        '--json', '-j',
        action='store_true',
        help='以 JSON 格式输出结果'
    )
    
    args = parser.parse_args()
    
    try:
        # 步骤1: 上传音频文件
        print(f"正在上传音频文件: {args.audio_file}")
        upload_result = upload_audio_file(args.audio_file)
        file_id = upload_result.get('file', {}).get('id')
        
        if not file_id:
            raise RuntimeError(f"无法从上传响应中获取 file_id: {upload_result}")
        
        print(f"音频上传成功，file_id: {file_id}")
        
        # 步骤2: 克隆声音
        print(f"正在克隆声音，voice_id: {args.voice_id}")
        clone_result = clone_voice(
            file_id=file_id,
            voice_id=args.voice_id,
            text=args.text
        )
        
        if args.json:
            print(json.dumps({
                "status": "success",
                "voice_id": args.voice_id,
                "file_id": file_id,
                "result": clone_result
            }, ensure_ascii=False, indent=2))
        else:
            print("=" * 50)
            print("声音克隆成功!")
            print(f"  voice_id: {args.voice_id}")
            print(f"  file_id: {file_id}")
            print("=" * 50)
        
        return 0
        
    except Exception as e:
        if args.json:
            print(json.dumps({
                "status": "error",
                "error": str(e)
            }, ensure_ascii=False, indent=2))
        else:
            print(f"错误: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())