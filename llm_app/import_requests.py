# from openai import OpenAI    # 导入OpenAI库，用于与OpenAI的API进行交互

# # 创建一个OpenAI客户端实例，需要提供API密钥和API的基础URL
# client = OpenAI(api_key="sk-eghruoxtqnjsqdcawudlezrujqghgqgdymbnyqhvxkvkifhs", base_url="https://api.siliconflow.cn/v1")
# # 调用OpenAI的聊天模型接口，创建一个聊天完成请求
# response = client.chat.completions.create(
#     model='deepseek-ai/DeepSeek-V2.5',  # 指定使用的模型为DeepSeek-V2.5
#     #model='deepseek-ai/DeepSeek-V3', # 指定使用的模型为Davinci-Codex
#     messages=[  # 提供对话历史，这里只有一条用户的消息
#         { 
#             'role': 'user',                                 # 消息角色为用户
#             'content': "中国大模型行业2025年将会迎来哪些机遇和挑战" # 用户的问题
#         }
#     ],
#     stream=True
# )

# for chunk in response:
#     print(chunk.choices[0].delta.content, end='')

from openai import OpenAI 
client = OpenAI(api_key="sk-eghruoxtqnjsqdcawudlezrujqghgqgdymbnyqhvxkvkifhs",base_url="https://api.siliconflow.cn/v1") 
response = client.chat.completions.create(
    model='deepseek-ai/DeepSeek-V3', # 指定使用的模型为Davinci-Codex
    messages=[  # 提供对话历史，这里只有一条用户的消息
        { 
            'role': 'user',                                 # 消息角色为用户
            'content': "中国大模型行业2025年将会迎来哪些机遇和挑战" # 用户的问题
        }
    ],
    stream=True
)

for chunk in response:
    print(chunk.choices[0].delta.content, end='')

    