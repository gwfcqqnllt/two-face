import requests
import json

# ⚠️ 记得换成你自己的真实 Token！
TOKEN = "pat_"
url = "https://cvmp9dqtsp.coze.site/stream_run"

headers = {"Authorization": f"Bearer {TOKEN}",
           "Content-Type": "application/json"
           }

print("=== 扣子智能体 CLI 对话启动 (输入 q 退出) ===")

# 保持同一个 session_id，让智能体记住上下文
session_id = "cli_chat_001"

while True:
    # 1. 接收用户输入
    user_input = input("\n你: ")
    if user_input.lower() in ['q', 'quit', 'exit']:
        print("再见！")
        break

    # 2. 组装发送给扣子的数据
    payload = {
        "content": {
            "query": {
                "prompt": [{"type": "text", "content": {"text": user_input}}]
            }
        },
        "type": "query",
        "session_id": session_id,
        "project_id": 7693231355639087154
    }

    # 3. 发送请求并解析流式回复
    try:
        response = requests.post(url, json=payload, headers=headers, stream=True, timeout=30)
        if response.status_code == 200:
            print("观朔: ", end="", flush=True)
            for line in response.iter_lines():
                if line:
                    line_str = line.decode('utf-8')
                    if line_str.startswith("data:"):
                        json_str = line_str[5:].strip()
                        try:
                            data = json.loads(json_str)
                            if data.get("type") == "answer" and data.get("content"):
                                content = data["content"]
                                if isinstance(content, dict):
                                    print(content.get("answer", content.get("text", "")), end="", flush=True)
                                else:
                                    print(content, end="", flush=True)
                            elif data.get("type") == "message_end":
                                print()  # 换行
                        except json.JSONDecodeError:
                            pass
        else:
            print(f"\n❌ API 调用失败，状态码：{response.status_code}")
    except Exception as e:
        print(f"\n❌ 发生异常：{e}")
