#!/usr/bin/env python3
"""
MiniMax 语音合成 Skill
使用 MiniMax Token Plan API 进行文本转语音

用法:
    python tts.py "要转换的文本"
    python tts.py "文本" --voice female-tianmei --speed 1.0 --output speech.mp3
"""

import json
import urllib.request
import urllib.parse
import urllib.error
import sys
import os
import base64
import time
import threading

# ============== 配置 ==============
API_KEY = "sk-cp-BC0OPAa8Y5HiiKOIHZpC4WRiBF3PEeGXDl2WgAaG7mRI7WHsGXhMdQWXErRKZvrNu6gH_iH-tTMjQsozFC_akhP9VOPJSxh1gMzb-P2KchmzTXBRGjZWBbY"
API_HOST = "https://api.minimaxi.com"

# 同步接口（短文本 ≤500字符）
SYNC_ENDPOINT = "/v1/t2a_v2"
# 异步接口（长文本）
ASYNC_ENDPOINT = "/v1/t2a_async_v2"
# 异步任务查询
TASK_QUERY_ENDPOINT = "/v1/t2a_async_v2/query"

# 默认参数
DEFAULT_MODEL = "speech-02-turbo"
DEFAULT_VOICE = "female-tianmei"
DEFAULT_SPEED = 1.0

# 同步接口字符限制
SYNC_CHAR_LIMIT = 500

# ============== 工具函数 ==============
def create_request(url: str, data: dict, method: str = "POST") -> urllib.request.Request:
    """创建 API 请求"""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    body = json.dumps(data).encode("utf-8")
    return urllib.request.Request(url, data=body, headers=headers, method=method)


def call_api(request: urllib.request.Request) -> dict:
    """调用 API 并返回结果"""
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8") if e.fp else ""
        raise Exception(f"HTTP Error {e.code}: {error_body}")
    except urllib.error.URLError as e:
        raise Exception(f"Network Error: {e.reason}")


# ============== TTS API ==============
def text_to_speech_sync(
    text: str,
    model: str = DEFAULT_MODEL,
    voice_id: str = DEFAULT_VOICE,
    speed: float = DEFAULT_SPEED,
    volume: int = 5,
    pitch: float = 1.0
) -> bytes:
    """
    同步文本转语音（短文本 ≤500字符）
    
    Args:
        text: 要转换的文本
        model: 模型名称
        voice_id: 声音 ID
        speed: 语速 (0.5-2.0)
        volume: 音量 (0-10)
        pitch: 音调 (0.5-2.0)
        
    Returns:
        音频数据（字节）
    """
    if len(text) > SYNC_CHAR_LIMIT:
        raise ValueError(f"文本过长（{len(text)} 字符），同步接口限制 {SYNC_CHAR_LIMIT} 字符内，请使用异步接口")
    
    url = f"{API_HOST}{SYNC_ENDPOINT}"
    
    payload = {
        "model": model,
        "text": text,
        "voice_id": voice_id,
        "speed": speed,
        "vol": volume,
        "pitch": pitch
    }
    
    result = call_api(create_request(url, payload))
    
    # 解析音频数据
    if "data" in result and result["data"]:
        audio_data = result["data"]
    elif "audio" in result:
        audio_data = result["audio"]
    elif "b64_audio" in result:
        audio_data = result["b64_audio"]
    else:
        raise Exception(f"未找到音频数据: {result}")
    
    return base64.b64decode(audio_data)


def text_to_speech_async(
    text: str,
    model: str = DEFAULT_MODEL,
    voice_id: str = DEFAULT_VOICE,
    speed: float = DEFAULT_SPEED,
    volume: int = 5,
    pitch: float = 1.0
) -> str:
    """
    异步文本转语音（长文本）- 提交任务
    
    Args:
        text: 要转换的文本
        model: 模型名称
        voice_id: 声音 ID
        speed: 语速
        volume: 音量
        pitch: 音调
        
    Returns:
        任务 ID
    """
    url = f"{API_HOST}{ASYNC_ENDPOINT}"
    
    payload = {
        "model": model,
        "text": text,
        "voice_id": voice_id,
        "speed": speed,
        "vol": volume,
        "pitch": pitch
    }
    
    result = call_api(create_request(url, payload))
    
    if "task_id" in result:
        return result["task_id"]
    else:
        raise Exception(f"未获取到任务 ID: {result}")


def query_async_task(task_id: str) -> dict:
    """
    查询异步任务状态
    
    Args:
        task_id: 任务 ID
        
    Returns:
        任务状态信息
    """
    url = f"{API_HOST}{TASK_QUERY_ENDPOINT}?task_id={task_id}"
    
    result = call_api(create_request(url, {}, "GET"))
    return result


def wait_for_async_task(task_id: str, max_wait: int = 300) -> bytes:
    """
    等待异步任务完成并返回音频
    
    Args:
        task_id: 任务 ID
        max_wait: 最大等待时间（秒）
        
    Returns:
        音频数据（字节）
    """
    start_time = time.time()
    
    print(f"⏳ 等待语音合成任务完成...")
    
    while time.time() - start_time < max_wait:
        result = query_async_task(task_id)
        
        status = result.get("status", "")
        
        if status == "success":
            # 获取音频数据
            if "data" in result and result["data"]:
                audio_data = result["data"]
            elif "b64_audio" in result:
                audio_data = result["b64_audio"]
            else:
                raise Exception(f"任务成功但未找到音频: {result}")
            
            return base64.b64decode(audio_data)
        
        elif status == "failed":
            raise Exception(f"语音合成任务失败: {result.get('error', '未知错误')}")
        
        elif status == "pending" or status == "processing":
            print(f"   状态: {status}...")
            time.sleep(5)
        else:
            print(f"   状态: {status}...")
            time.sleep(5)
    
    raise TimeoutError(f"等待任务完成超时（{max_wait}秒）")


# ============== 主函数 ==============
def main():
    text = None
    voice_id = DEFAULT_VOICE
    speed = DEFAULT_SPEED
    volume = 5
    pitch = 1.0
    output_file = None
    
    # 解析命令行参数
    args = sys.argv[1:]
    i = 0
    while i < len(args):
        arg = args[i]
        
        if arg in ("-v", "--voice") and i + 1 < len(args):
            voice_id = args[i + 1]
            i += 2
        elif arg in ("-s", "--speed") and i + 1 < len(args):
            speed = float(args[i + 1])
            i += 2
        elif arg in ("--vol") and i + 1 < len(args):
            volume = int(args[i + 1])
            i += 2
        elif arg in ("-p", "--pitch") and i + 1 < len(args):
            pitch = float(args[i + 1])
            i += 2
        elif arg in ("-o", "--output") and i + 1 < len(args):
            output_file = args[i + 1]
            i += 2
        elif arg in ("-h", "--help"):
            print("用法: python tts.py <文本> [选项]")
            print("")
            print("参数:")
            print("  <文本>                       要转换的文本")
            print("")
            print("选项:")
            print("  -v, --voice <ID>             声音 ID")
            print("  -s, --speed <速度>           语速 (0.5-2.0)")
            print("  --vol <音量>                 音量 (0-10)")
            print("  -p, --pitch <音调>           音调 (0.5-2.0)")
            print("  -o, --output <文件>           输出文件路径")
            print("  -h, --help                   显示帮助")
            print("")
            print("常用声音:")
            print("  female-tianmei    甜美女声 (默认)")
            print("  female-yujie     成熟女声，适合讲故事")
            print("  female-shaonv    少女声")
            print("  male-qn-qingse   青年男声")
            print("  male-jieshuo     主持人男声")
            print("")
            print("详见 voices.md")
            sys.exit(0)
        elif not arg.startswith("-"):
            text = arg
            i += 1
        else:
            i += 1
    
    if not text:
        print("用法: python tts.py \"要转换的文本\"")
        print("   或: python tts.py \"文本\" --voice female-yujie --output speech.mp3")
        print("   使用 -h 查看更多选项")
        sys.exit(1)
    
    # 验证参数
    if speed < 0.5 or speed > 2.0:
        print("❌ 语速必须在 0.5-2.0 之间")
        sys.exit(1)
    
    if pitch < 0.5 or pitch > 2.0:
        print("❌ 音调必须在 0.5-2.0 之间")
        sys.exit(1)
    
    if volume < 0 or volume > 10:
        print("❌ 音量必须在 0-10 之间")
        sys.exit(1)
    
    # 生成默认输出文件名
    if output_file is None:
        timestamp = int(time.time())
        output_file = f"speech_{timestamp}.mp3"
    
    try:
        print(f"🔊 正在生成语音...")
        print(f"   文本: {text[:50]}{'...' if len(text) > 50 else ''}")
        print(f"   声音: {voice_id}")
        print(f"   语速: {speed}")
        print()
        
        # 根据文本长度选择接口
        if len(text) <= SYNC_CHAR_LIMIT:
            print("📡 使用同步接口...")
            audio_data = text_to_speech_sync(text, voice_id=voice_id, speed=speed, volume=volume, pitch=pitch)
        else:
            print("📡 使用异步接口（长文本）...")
            task_id = text_to_speech_async(text, voice_id=voice_id, speed=speed, volume=volume, pitch=pitch)
            audio_data = wait_for_async_task(task_id)
        
        # 保存音频文件
        with open(output_file, "wb") as f:
            f.write(audio_data)
        
        print(f"\n✅ 语音已保存: {output_file}")
        print(f"   文件大小: {len(audio_data) / 1024:.1f} KB")
        
    except Exception as e:
        print(f"❌ 语音合成失败: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()