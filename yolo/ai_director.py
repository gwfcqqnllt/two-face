import requests

# 模拟YOLO检测到的画面元素
objects = ["树", "云", "海", "风", "山", "藤", "雾", "沙", "土", "花", "季"]
prompt = f"你是世界的孩子。请根据这些意象写一段100字的诗意短剧剧本：{', '.join(objects)}"

print("正在让本地大模型写剧本，请稍等...")
try:
    # 调用本地Ollama，设置60秒超时
    r = requests.post("http://localhost:11434/api/chat", json={
        "model": "qwen3:4b",
        "messages": [{"role": "user", "content": prompt}],
        "stream": False
    }, timeout=120)
    print("\n=== AI导演写的剧本 ===\n")
    print(r.json()["message"]["content"])
except Exception as e:
    print("\n[提示] 本地大模型响应超时或未启动，使用保底剧本文本：")
    print("""
    我的头发也会生长，泛黄，掉落，那我也是树吗。
    我的灵魂也会漂浮，游荡，消散，那我也是云吗。
    我的眼泪也会凝集、汹涌、登岸，那我也是海吗。
    ...
    你是世界的孩子，生来便有世界的样子。
    """)