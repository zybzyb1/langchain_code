
# 方法 2：从系统环境变量中获取 API Token
# 将 API Token 存储在系统环境变量中，这样可以避免在代码中直接暴露 Token。
# 设置环境变量：
# 在 Windows 中：
# cmd
# 复制
# set API_TOKEN=你的API_KEY
# 在 Linux 或 macOS 中：
# bash
# 复制
# export API_TOKEN=你的API_TOKEN
# 代码实现：
import requests
import os
import sys
import json

def main(user_message):
    url = "https://api.siliconflow.cn/v1/chat/completions"  # 修复 URL 格式
    api_token = os.getenv("API_KEY")  # 从环境变量中获取 API Token
    if not api_token:
        print("错误：未找到环境变量 API_KEY。请设置环境变量后再运行脚本。")
        print("添加环境变量方法：在系统环境变量中设置 API_KEY=你的API_TOKEN")
        return

    payload = {
        "model": "deepseek-ai/DeepSeek-V2.5",
        "messages": [
            {
                "role": "user",
                "content": user_message
            }
        ],
        "stream": True
    }
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers, stream=True)
    full_response = ""
    if response.status_code == 200:
        for line in response.iter_lines():
            if line:
                decoded_line = line.decode("utf-8")
                if decoded_line.startswith("data: "):  # 流式响应通常以 "data: " 开头
                    try:
                        data = json.loads(decoded_line[5:])  # 去掉前缀 "data: "
                        if "choices" in data and data["choices"]:
                            delta_content = data["choices"][0].get("delta", {}).get("content", "")
                            full_response += delta_content  # 拼接内容
                            print(delta_content, end="", flush=True)  # 实时打印内容
                    except json.JSONDecodeError as e:
                        print(f"解析 JSON 数据失败：{e}")
                        print(f"返回的数据：{decoded_line}")
        print("\n\n完整回复：", full_response)  # 打印完整的回复内容
    else:
        print(f"请求失败，状态码：{response.status_code}")
        print(response.text)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法：python script.py <USER_MESSAGE>")
        sys.exit(1)

    user_message = sys.argv[1]
    main(user_message)

