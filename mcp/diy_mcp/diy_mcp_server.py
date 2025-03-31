# MCP Servers主要功能
# MCP Servers 作为一个轻量级的本地服务，旨在为客户端提供数据访问和功能执行的接口。
# 1. 资源暴露（Resource Exposure）
# 资源是服务器提供给客户端的数据实体，可以是文件、数据库记录、内存中的对象等。
# 例如：
# 文件资源：file:///home/user/report.txt
# 内存资源：memo://recent-insights
# 2. 工具提供（Tool Provisioning）
# 工具是服务器暴露的可执行功能，客户端可以通过调用这些工具完成特定任务。
# 例如：
# 查询数据库：query_database（参数：SQL 语句，返回：查询结果）
# 文件写入：write_file（参数：文件路径、内容）
# 3. 动态通知（Dynamic Notification）
# 当资源发生变化时，服务器可以通过通知机制（如 notification 消息）主动推送更新到客户端。
# 4. 会话管理（Session Management）
# 处理客户端的连接初始化、能力协商和会话关闭。
# 自定义 MCP Servers


import json
import sys

# 处理客户端请求
def handle_request(request):
    method = request.get("method")
    params = request.get("params", {})
    request_id = request.get("id")

    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "result": {"version": "1.0", "capabilities": ["resources", "tools"]},
            "id": request_id
        }
    elif method == "read_resource":
        uri = params.get("uri")
        with open(uri.replace("file:///", ""), "r") as f:
            content = f.read()
        return {"jsonrpc": "2.0", "result": content, "id": request_id}
    elif method == "call_tool":
        tool_name = params.get("name")
        if tool_name == "echo":
            return {"jsonrpc": "2.0", "result": params.get("message"), "id": request_id}
    else:
        return {"jsonrpc": "2.0", "error": {"code": -32601, "message": "Method not found"}, "id": request_id}

# 主循环：通过 Stdio 通信
def main():
    while True:
        # 从 stdin 读取请求
        raw_input = sys.stdin.readline().strip()
        if not raw_input:
            break
        request = json.loads(raw_input)
        
        # 处理请求并返回响应
        response = handle_request(request)
        sys.stdout.write(json.dumps(response) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()


# 通过 python 启动服务
# python mcp_server.py
# 在相同的目录下创建 test.txt 文件。
# Hello, this is a test file!
# 另外启动一个命令窗口，输入：
# echo '{"jsonrpc": "2.0", "method": "read_resource", "params": {"uri": "file:///D:/path/to/test.txt"}, "id": 2}' | python mcp_server.py

# {"jsonrpc": "2.0", "result": "Hello, this is a test file!", "id": 2}
# 注：此处使用的是 PowerShell，我们看到服务返回了文件的内容。