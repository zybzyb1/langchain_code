from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# 初始化 ChatOpenAI，指定 DeepSeek 的 API Key 和模型
llm = ChatOpenAI(
    api_key="sk-eghruoxtqnjsqdcawudlezrujqghgqgdymbnyqhvxkvkifhs",  # 替换为你的 DeepSeek API Key
    model="deepseek-ai/DeepSeek-V3",  # 使用 DeepSeek 的对话模型
    base_url="https://api.siliconflow.cn/v1"
)

# 定义 ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是世界级的技术专家"),
    ("user", "{input}")
])

# 构建链式调用
chain = prompt | llm

# 调用链并获取结果
result = chain.invoke({"input": "帮我写一篇关于AI的技术文章,100个字"})
print(result)

# import requests
# import json

# # 百度智能云 API 配置
# API_KEY = "bce-v3/ALTAK-djDqM5mS3sORqXyvStB8f/bd194e45cf25c4ea605abbe8d628a68ea4d9b782"  # 替换为你的百度智能云 API Key
# SECRET_KEY = "b2c2bd72aaae448c9948cf60bacfbc67"  # 替换为你的百度智能云 Secret Key
# ACCESS_TOKEN_URL = "https://aip.baidubce.com/oauth/2.0/token"
# MODEL_API_URL = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/DeepSeek-R1-Distill-Qwen-32B"  # 替换为实际的模型API地址

# # 获取 Access Token
# def get_access_token(api_key, secret_key):
#     payload = {
#         "grant_type": "client_credentials",
#         "client_id": api_key,
#         "client_secret": secret_key
#     }
#     response = requests.post(ACCESS_TOKEN_URL, data=payload)
#     response_data = response.json()
#     return response_data.get("access_token")

# # 调用百度智能云的模型
# def call_baidu_model(access_token, prompt):
#     headers = {
#         "Content-Type": "application/json"
#     }
#     payload = {
#         "messages": [
#             {"role": "system", "content": "你是世界级的技术专家"},
#             {"role": "user", "content": prompt}
#         ]
#     }
#     response = requests.post(
#         MODEL_API_URL + f"?access_token={access_token}",
#         headers=headers,
#         data=json.dumps(payload)
#     )
#     response_data = response.json()
#     return response_data.get("result")

# # 获取 Access Token
# access_token = get_access_token(API_KEY, SECRET_KEY)

# # 调用模型并获取结果
# result = call_baidu_model(access_token, "帮我写一篇关于AI的技术文章,100个字")
# print(result)

