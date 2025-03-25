import requests
import sys

# 检查是否提供了命令行参数
if len(sys.argv) != 2:
    print("用法: python send_request.py '你的问题'")
    sys.exit(1)

# 获取命令行参数作为输入数据
user_input = sys.argv[1]

# 定义请求的URL
url = "http://localhost:8000/chat"

# 定义请求的JSON数据
data = {
    "input": user_input
}

# 发送POST请求
response = requests.post(url, json=data)

# 打印响应结果
print(f"状态码: {response.status_code}")
print("响应内容:", response.json())

# 使用方法：
# 将上述代码保存为一个 Python 文件，例如 send_request.py。
# 在命令行中运行以下命令，并将你的问题作为参数传递：
# python send_request.py "你好，世界！"
# 示例输出：
# 如果一切正常，你应该会看到类似以下输出：

# 状态码: 200
# 响应内容: {'response': '这是来自聊天机器人的回复。'}
# 注意事项：
# 确保你的 FastAPI 应用正在运行，并且可以通过 http://localhost:8000 访问。
# 如果你在远程服务器上运行应用，需要将 localhost 替换为服务器的 IP 地址。
# 如果你需要添加请求头（例如 Content-Type），可以使用 headers 参数：
# headers = {"Content-Type": "application/json"}
# response = requests.post(url, json=data, headers=headers)
# 通过这种方式，你可以直接在命令行中输入问题，并将其作为参数传递给脚本。