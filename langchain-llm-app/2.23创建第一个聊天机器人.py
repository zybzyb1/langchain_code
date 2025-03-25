from langchain.schema import(
    AIMessage,
    HumanMessage,
    SystemMessage
)

import os
from openai import OpenAI
# 定义变量
english_sentence = "I love programming."

# 设置硅基大模型的参数
OPENAI_API_KEY = os.getenv("API_KEY")  # 从环境变量读取API_KEY
model_name = "deepseek-ai/DeepSeek-V2.5"

# 初始化ChatOpenAI
client = OpenAI(api_key=OPENAI_API_KEY, base_url="https://api.siliconflow.cn/v1")
# 调用模型进行翻译
response = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V2.5",  # 指定模型
    messages=[
        {"role": "user", "content": f"Translate this sentence from English to chinese. {english_sentence}"}  
        ],
        temperature=0.7  # 设置temperature参数为0.7以调整生成的多样性
    )
    # 提取翻译后的中文句子
name = response.choices[0].message.content.strip()
  
print(name)


