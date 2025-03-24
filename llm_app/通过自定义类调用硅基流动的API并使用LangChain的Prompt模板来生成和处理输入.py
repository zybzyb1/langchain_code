# 以下是使用硅基流动平台的大模型（如 DeepSeek-V2.5 或 THUDM/glm-4-9b-chat）与 LangChain 结合的代码示例。
# 这个示例展示了如何通过自定义类调用硅基流动的 API，并使用 LangChain 的 Prompt 模板来生成和处理输入
# 1. 安装必要的库
# 确保安装了 langchain 和 requests 库：
# pip install langchain requests
# 2. 在win10系统中，设置环境变量中设置 API 密钥
# 3. 自定义大模型类
# 创建一个自定义的 LLM 类，用于调用硅基流动平台的大模型：

from langchain.llms.base import LLM
import requests
import os

class SiliconFlow(LLM):
    def __init__(self):
        super().__init__()
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.base_url = "https://api.siliconflow.cn/v1/chat/completions"

    @property
    def _llm_type(self) -> str:
        return "siliconflow"

    def _call(self, prompt: str, stop: list = None, model: str = "default-model") -> str:
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "stream": False
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": f"Bearer {self.api_key}"
        }

        response = requests.post(self.base_url, json=payload, headers=headers)
        response.raise_for_status()
        response_content = response.json()["choices"][0]["message"]["content"]

        if stop is not None:
            response_content = self.enforce_stop_tokens(response_content, stop)
        return response_content

    @staticmethod
    def enforce_stop_tokens(text: str, stop_tokens: list) -> str:
        for token in stop_tokens:
            if token in text:
                text = text[:text.index(token)]
        return text
    
# 4. 使用 LangChain 的 Prompt 模板
# 结合 LangChain 的 Prompt 模板，调用自定义的大模型：
from langchain.prompts import ChatPromptTemplate

# 创建自定义 LLM 实例
llm = SiliconFlow()

# 定义 Prompt 模板
template = """
任务: 根据输入内容生成一个简短的总结。
输入: {input_text}
总结:
"""
prompt_template = ChatPromptTemplate.from_template(template)

# 格式化 Prompt 并调用模型
input_text = "这是一个测试输入，用于展示如何使用硅基流动平台的大模型。"  # 示例输入
formatted_prompt = prompt_template.format_messages(input_text=input_text)
response = llm._call(formatted_prompt[0].content)

print("模型生成的响应：")
print(response)

# 代码说明
# 自定义 LLM 类：
# 使用 requests 库向硅基流动平台发送请求。
# 支持自定义模型名称（如 DeepSeek-V2.5 或 THUDM/glm-4-9b-chat）。
# Prompt 模板：
# 使用 LangChain 的 ChatPromptTemplate 来构建动态的 Prompt。
# 调用模型：
# 将格式化后的 Prompt 传递给自定义的 LLM 类，并获取模型的响应。
# 注意事项
# 确保替换 your_api_key_here 为你的硅基流动平台的 API 密钥。
# 根据需要选择合适的模型名称（如 DeepSeek-V2.5 或 THUDM/glm-4-9b-chat）。
# 如果需要处理响应中的特定格式（如 JSON），可以在 _call 方法中进一步解析响应内容。
# 通过上述代码，你可以轻松地将硅基流动平台的大模型与 LangChain 结合使用，实现复杂的语言任务。
