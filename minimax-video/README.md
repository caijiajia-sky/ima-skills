# MiniMax Video Skill - 测试说明

## 创建的文件

1. `/sandbox/workspace/skills/minimax-video/SKILL.md` - Skill 触发条件说明文档
2. `/sandbox/workspace/skills/minimax-video/scripts/generate_video.py` - Python 生成脚本

## 功能特性

- 支持命令行参数: --prompt, --duration, --resolution, --fps, --output-dir, --output-name
- 支持异步任务轮询，等待视频生成完成
- 自动通过 file_id 获取下载链接并下载视频

## API 端点

- 提交任务: `POST https://api.minimaxi.com/v1/video_generation`
- 查询状态: `GET https://api.minimaxi.com/v1/query/video_generation?task_id=xxx`
- 获取下载链接: `GET https://api.minimaxi.com/v1/files/retrieve?file_id=xxx`

## 测试结果

由于 Token Plan 今日配额已用完（3/3），无法进行实际视频生成测试。

脚本已通过以下验证:
1. 任务提交成功，返回 task_id
2. 状态查询端点已更正为 `/v1/query/video_generation`
3. 文件下载端点已添加 `/v1/files/retrieve`

## 使用示例

```bash
# 基本用法
python scripts/generate_video.py --prompt "A cute cat on a sunny windowsill"

# 指定参数
python scripts/generate_video.py -p "Sunset over ocean" -d 10 -r 1080P -o ./output

# 查看帮助
python scripts/generate_video.py --help
```

## 注意事项

1. 分辨率必须使用大写格式：768P 或 1080P
2. 视频生成为异步任务，需要等待 1-3 分钟
3. 建议使用英文提示词效果更好
4. 轮询间隔默认为 10 秒