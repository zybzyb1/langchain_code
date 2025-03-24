# 将代码分开到不同文件中
# 如果你希望将代码模块化，可以将 SiliconFlow 类放在一个单独的文件（如 llm.py）中，并在 main.py 中导入它。
# llm_app/
# │
# ├── llm.py          # 自定义 LLM 类
# ├── main.py         # 主逻辑
import os
from langchain.prompts import ChatPromptTemplate
from llm import SiliconFlow  # 导入自定义 LLM 类

# 打印环境变量以确认其值
print("API_KEY:", os.getenv("API_KEY"))

# 创建自定义 LLM 实例
llm = SiliconFlow()

# 定义 Prompt 模板
# template = """
# 任务: 根据输入内容生成一个简短的总结。
# 输入: {input_text}
# 总结:
# """
template = """
任务: 根据输入需求生成代码。
输入: {input_text}
代码:
"""
prompt_template = ChatPromptTemplate.from_template(template)

# 格式化 Prompt 并调用模型
input_text = "帮我用python脚本写一个屏幕取色器,并显示色值。" #"你好，我想问一下，你叫什么名字？"
formatted_prompt = prompt_template.format_messages(input_text=input_text)
response = llm._call(formatted_prompt[0].content,model='deepseek-ai/DeepSeek-V2.5')

print("模型生成的响应：")
print(response)
