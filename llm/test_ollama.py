import requests

OLLAMA_URL = "http://localhost:11434/api/chat"

def chat(prompt):
    payload = {
        "model": "qwen3:4b",
        "messages": [{"role": "user", "content": prompt}],
        "stream": False
    }
    r = requests.post(OLLAMA_URL, json=payload)
    return r.json()["message"]["content"]

if __name__ == "__main__":
    print("=== 本地 Ollama 测试 ===")
    print(chat("用一句话介绍你自己"))