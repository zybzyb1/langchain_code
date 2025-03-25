# 方法 3：使用配置文件存储API Token并支持多模型选择
# 1、使用配置文件存储API Token：避免直接在代码中或环境变量中暴露敏感信息。
# 2、增加错误处理和日志记录：方便调试和追踪问题。
# 3、支持多模型选择：允许用户在运行时选择不同的模型。
# 4、优化用户体验：例如支持从文件读取用户消息，或者将结果保存到文件
# 1. 创建配置文件 config.json
# 在项目根目录下创建一个 config.json 文件，内容如下：
# {
#     "api_token": "你的API_TOKEN",
#     "default_model": "deepseek-ai/DeepSeek-V2.5",
#     "available_models": [
#         "deepseek-/aiDeepSeek-V2.5",
#         "another-model/example"
#     ]
# }

# 2. 修改代码实现
import requests
import os
import json
import sys
import logging

def load_config(config_path="config.json"):
    """加载配置文件"""
    if not os.path.exists(config_path):
        logging.error(f"错误：未找到配置文件 {config_path}。请确保配置文件存在。")
        print(f"错误：未找到配置文件 {config_path}。请确保配置文件存在。")
        sys.exit(1)

    try:
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)
    except PermissionError:
        logging.error(f"错误：没有权限读取配置文件 {config_path}。")
        print(f"错误：没有权限读取配置文件 {config_path}。")
        sys.exit(1)
    except json.JSONDecodeError as e:
        logging.error(f"错误：配置文件 {config_path} 格式错误。详细信息：{e}")
        print(f"错误：配置文件 {config_path} 格式错误。详细信息：{e}")
        sys.exit(1)

    return config

def main(user_message, model=None):
    config = load_config()
    api_token = config.get("api_token")
    if not api_token:
        print("错误：配置文件中未找到API Token。请检查配置文件。")
        return

    url = "https://api.siliconflow.cn/v1/chat/completions"
    model = model or config.get("default_model")
    if model not in config.get("available_models", []):
        print(f"警告：选择的模型 {model} 不在支持列表中。将使用默认模型。")
        model = config.get("default_model")

    payload = {
        "model": model,
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
                            # print(delta_content, end="", flush=True)  # 实时打印内容
                    except json.JSONDecodeError as e:
                        print(f"解析 JSON 数据失败：{e}")
                        print(f"返回的数据：{decoded_line}")
        print("\n\n完整回复：", full_response)  # 打印完整的回复内容
    else:
        print(f"请求失败，状态码：{response.status_code}")
        print(response.text)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法：python script.py <USER_MESSAGE> [MODEL]")
        sys.exit(1)

    user_message = sys.argv[1]
    model = sys.argv[2] if len(sys.argv) > 2 else None
    main(user_message, model)

# 3. 使用方法
# 将API Token和模型信息写入 config.json 文件。
# 运行脚本时，可以通过命令行传递用户消息和可选的模型名称：
# python script.py "你的问题" "deepseek-ai/DeepSeek-V2.5"

#   说明
# 配置文件：将API Token和模型信息存储在配置文件中，避免直接暴露在代码或环境变量中。
# 多模型支持：用户可以在运行时选择不同的模型，如果选择的模型不在支持列表中，会自动使用默认模型。
# 错误处理：增加了对配置文件缺失、API Token缺失等错误的处理。  

















