# 方法 1：从命令行参数传递 API Token
# 你可以通过命令行参数传递 API Token，这样在运行脚本时动态输入 Token，避免直接暴露在代码中。
import requests
import os
import sys
import json

def main(api_token, user_message):
    url = "https://api.siliconflow.cn/v1/chat/completions"
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

    if response.status_code == 200:
        # 初始化变量用于拼接最终的回复内容
        full_response = ""
        for line in response.iter_lines():
            if line:
                decoded_line = line.decode("utf-8")
                # 解析 JSON 数据
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
    if len(sys.argv) != 3:
        print("用法：python script.py <API_TOKEN> <USER_MESSAGE>")
        sys.exit(1)

    api_token = sys.argv[1]
    user_message = sys.argv[2]
    main(api_token, user_message)

# 代码解析
# 流式响应处理：
# 使用 response.iter_lines() 逐行读取流式响应。
# 每行数据以 data:  开头，表示一个 JSON 数据块。
# 解析 JSON 数据：
# 使用 json.loads() 解析每行数据。
# 提取 choices[0].delta.content，这是模型生成的文本内容。
# 拼接内容：
# 将每次生成的文本内容拼接到 full_response 中。
# 同时实时打印内容，让用户可以看到生成过程。
# 完整回复：
# 在流式响应结束后，打印完整的回复内容。
# 注意事项
# 乱码问题：确保服务器返回的内容是 UTF-8 编码。如果仍然有乱码，可以尝试其他编码（如 latin1）进行解码。
# 错误处理：如果响应中包含错误信息（例如 finish_reason 为 stop 但内容为空），需要根据实际情况处理。
# 性能优化：对于大规模应用，可以考虑将流式响应写入文件或数据库，而不是直接打印到控制台。
# 通过这种方式，你可以正确处理流式响应，并提取出问题的答案。

# 以上源码运行方式：在终端中输入：
# python script.py <你的API_TOKEN> "你好，你叫什么名字？"
#python.exe  通过REST接口进行服务调用_方法1从命令行参数传递API_KEY.py sk-eghruoxtqnjsqdcawudlezrujqghgqgdymbnyqhvxkvkifhs  "你好，你叫什么名字？"
