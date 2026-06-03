#!/usr/bin/env python3
"""
MiniMax Music Generation Script
通过 MiniMax API 生成音乐
"""

import urllib.request
import urllib.error
import json
import os
import sys
import base64
import argparse


# API 配置
API_KEY = "sk-cp-BC0OPAa8Y5HiiKOIHZpC4WRiBF3PEeGXDl2WgAaG7mRI7WHsGXhMdQWXErRKZvrNu6gH_iH-tTMjQsozFC_akhP9VOPJSxh1gMzb-P2KchmzTXBRGjZWBbY"
API_HOST = "https://api.minimaxi.com"
ENDPOINT = "/v1/music_generation"


def generate_music(prompt, model="music-2.6", lyrics=None, lyrics_type="user", 
                   instrumental=False, style=None, title=None):
    """调用 MiniMax API 生成音乐"""
    
    url = f"{API_HOST}{ENDPOINT}"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": model,
        "prompt": prompt
    }
    
    # 可选参数
    if lyrics:
        data["lyrics"] = lyrics
        data["lyrics_type"] = lyrics_type
    
    if instrumental:
        data["instrumental"] = True
    
    if style:
        data["style"] = style
    
    if title:
        data["title"] = title
    
    json_data = json.dumps(data).encode("utf-8")
    
    req = urllib.request.Request(url, data=json_data, headers=headers, method="POST")
    
    try:
        with urllib.request.urlopen(req, timeout=180) as response:
            result = json.loads(response.read().decode("utf-8"))
            
            # 检查响应状态
            base_resp = result.get("base_resp", {})
            if base_resp.get("status_code", 0) != 0:
                error_msg = base_resp.get("status_msg", "未知错误")
                print(f"❌ API 错误: {error_msg}")
                return None
            
            return result
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        print(f"❌ HTTP 错误: {e.code}")
        print(f"   {error_body}")
        return None
    except Exception as e:
        print(f"❌ 请求失败: {str(e)}")
        return None


def save_audio(data, output_path):
    """保存音频数据（支持 base64 或 URL）"""
    
    try:
        # 如果是 base64 编码的音频数据
        if isinstance(data, str):
            # 尝试解码 base64
            try:
                audio_bytes = base64.b64decode(data)
                with open(output_path, "wb") as f:
                    f.write(audio_bytes)
                print(f"✅ 音频已保存: {output_path}")
                return True
            except Exception:
                # 可能是 URL
                if data.startswith("http"):
                    return download_from_url(data, output_path)
                print(f"❌ 无法解析音频数据")
                return False
        
        print(f"❌ 未知音频数据类型")
        return False
    except Exception as e:
        print(f"❌ 保存失败: {str(e)}")
        return False


def download_from_url(url, output_path):
    """从 URL 下载音频"""
    
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=120) as response:
            with open(output_path, "wb") as f:
                f.write(response.read())
        print(f"✅ 音频已下载: {output_path}")
        return True
    except Exception as e:
        print(f"❌ 下载失败: {str(e)}")
        return False


def parse_response(result, output_path):
    """解析 API 响应并保存音频"""
    
    data = result.get("data", {})
    
    if not data:
        print("❌ 响应中无音频数据")
        return False
    
    status = data.get("status", 0)
    audio_data = data.get("audio", "")
    
    # status: 0=处理中, 1=处理中, 2=完成
    if status == 2 and audio_data:
        return save_audio(audio_data, output_path)
    else:
        print(f"⚠️ 任务状态: {status} (0=处理中, 2=完成)")
        print("   音频数据可能在异步处理后可用")
        return False


def main():
    parser = argparse.ArgumentParser(description="MiniMax 音乐生成工具")
    parser.add_argument("--prompt", "-p", required=True, help="音乐描述/灵感（英文效果更好）")
    parser.add_argument("--model", "-m", default="music-2.6", help="模型版本: music-2.5 或 music-2.6")
    parser.add_argument("--lyrics", "-l", help="歌词（JSON 格式或文本）")
    parser.add_argument("--lyrics-type", default="user", choices=["user", "ai_generated"], help="歌词类型")
    parser.add_argument("--instrumental", action="store_true", help="生成纯音乐（无歌词）")
    parser.add_argument("--style", "-s", help="音乐风格")
    parser.add_argument("--title", "-t", help="歌曲标题")
    parser.add_argument("--output", "-o", default="output.mp3", help="输出文件路径")
    
    args = parser.parse_args()
    
    print("=" * 50)
    print("🎵 MiniMax 音乐生成器")
    print("=" * 50)
    
    # 调用 API
    result = generate_music(
        prompt=args.prompt,
        model=args.model,
        lyrics=args.lyrics,
        lyrics_type=args.lyrics_type,
        instrumental=args.instrumental,
        style=args.style,
        title=args.title
    )
    
    if not result:
        sys.exit(1)
    
    # 解析并保存音频
    if parse_response(result, args.output):
        print(f"\n🎉 音乐生成成功！")
        print(f"   文件: {os.path.abspath(args.output)}")
    else:
        print("\n⚠️ 音频保存失败，请查看上方信息")
        
    # 打印额外信息
    extra_info = result.get("extra_info", {})
    if extra_info:
        print("\n📊 音频信息:")
        print(f"   时长: {extra_info.get('music_duration', 'N/A')} ms")
        print(f"   采样率: {extra_info.get('music_sample_rate', 'N/A')} Hz")
        print(f"   声道: {extra_info.get('music_channel', 'N/A')}")
        print(f"   比特率: {extra_info.get('bitrate', 'N/A')} bps")
        print(f"   大小: {extra_info.get('music_size', 'N/A')} bytes")


if __name__ == "__main__":
    main()