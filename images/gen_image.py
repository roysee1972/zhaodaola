#!/usr/bin/env python3
"""
找到啦网站配图生成工具
使用阿里云通义万相API生成文章配图

用法：
  DASHSCOPE_API_KEY=xxx python3 gen_image.py "描述文字" [输出文件名.png] [风格]

风格选项：
  - illustration (默认): 插画风格，温暖治愈
  - realistic: 写实风格
  - watercolor: 水彩风格
  - chinese: 中国水墨风格
"""

import sys
import os
import json
import time
import subprocess

API_KEY = os.environ.get("DASHSCOPE_API_KEY", "")
API_URL = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis"
TASK_URL = "https://dashscope.aliyuncs.com/api/v1/tasks"
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

STYLE_PROMPTS = {
    "illustration": "warm illustration style, soft lighting, warm colors, cozy atmosphere",
    "realistic": "photorealistic, natural lighting, detailed textures",
    "watercolor": "watercolor painting style, soft edges, gentle colors, artistic",
    "chinese": "chinese ink painting style, traditional, elegant, simple",
}

def get_auth_header():
    return "Authorization: Bearer %s" % API_KEY

def submit_task(prompt, size="1024*1024", n=1):
    """提交图片生成任务"""
    payload = json.dumps({
        "model": "wanx2.1-t2i-turbo",
        "input": {"prompt": prompt},
        "parameters": {"size": size, "n": n}
    })
    
    cmd = [
        "curl", "-s", "-X", "POST", API_URL,
        "-H", "X-DashScope-Async: enable",
        "-H", get_auth_header(),
        "-H", "Content-Type: application/json",
        "-d", payload
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    data = json.loads(result.stdout)
    return data.get("output", {}).get("task_id", "")

def poll_task(task_id, max_wait=60):
    """轮询任务状态，返回图片URL列表"""
    for i in range(max_wait // 3):
        time.sleep(3)
        cmd = ["curl", "-s", "%s/%s" % (TASK_URL, task_id), "-H", get_auth_header()]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
        data = json.loads(result.stdout)
        status = data.get("output", {}).get("task_status", "")
        
        if status == "SUCCEEDED":
            results = data.get("output", {}).get("results", [])
            return [r.get("url", "") for r in results]
        elif status == "FAILED":
            print("Error: %s" % json.dumps(data, ensure_ascii=False)[:300])
            return []
    
    print("Timeout waiting for task")
    return []

def download_image(url, filepath):
    """下载图片到本地"""
    cmd = ["curl", "-s", "-o", filepath, url]
    subprocess.run(cmd, timeout=30)
    return os.path.exists(filepath)

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    if not API_KEY:
        print("Error: DASHSCOPE_API_KEY environment variable not set")
        sys.exit(1)
    
    prompt = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "output.png"
    style = sys.argv[3] if len(sys.argv) > 3 else "illustration"
    
    # 构建完整提示词
    style_suffix = STYLE_PROMPTS.get(style, STYLE_PROMPTS["illustration"])
    full_prompt = "%s, %s" % (prompt, style_suffix)
    
    print("Prompt: %s" % full_prompt)
    print("Output: %s" % output_file)
    print("Style: %s" % style)
    print()
    
    # 提交任务
    print("Submitting task...")
    task_id = submit_task(full_prompt)
    if not task_id:
        print("Failed to submit task")
        sys.exit(1)
    
    print("Task ID: %s" % task_id)
    print("Waiting for result...")
    
    # 轮询结果
    urls = poll_task(task_id)
    if not urls:
        print("No images generated")
        sys.exit(1)
    
    # 下载图片
    output_path = os.path.join(OUTPUT_DIR, output_file)
    url = urls[0]
    print("Downloading: %s..." % url[:80])
    
    if download_image(url, output_path):
        size = os.path.getsize(output_path)
        print("Saved: %s (%.1f KB)" % (output_path, size/1024.0))
    else:
        print("Failed to download image")
        sys.exit(1)

if __name__ == "__main__":
    main()
