#0.2 基于 requests 库的流式输出
#如果您有非 openai 的场景，如您需要基于 request 库使用 siliconcloud API，请您注意： 除了 payload 中的 stream 需要设置外，request 请求的参数也需要设置stream = True, 才能正常按照 stream 模式进行返回。
import requests
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv  # 导入dotenv库，用于加载环境变量
import os

# 加载.env文件中的环境变量
load_dotenv()

# 读取环境变量--API密钥
API_KEY = os.getenv("API_KEY")

# 检查API密钥是否已正确加载
if not API_KEY:
    raise ValueError("API_KEY is not set. Please check your .env file.")

url = "https://api.siliconflow.cn/v1/chat/completions"


# 自定义硅基流动大模型类
class Custom_Stream_LLM_Siliconflow:
    def __call__(self, prompt: str) -> str:
        try:   
            payload = {
                "model": "deepseek-ai/DeepSeek-V2.5", # 替换成你的模型
                "messages": [
                    {
                        "role": "user",
                        'content': f"{prompt}",  # 用户输入的提示 "content": "SiliconCloud公测上线，每用户送3亿token 解锁开源大模型创新能力。对于整个大模型应用领域带来哪些改变？"
                    }
                ],
                "stream": True # 此处需要设置为stream模式
            }

            headers = {
                    "accept": "application/json",
                    "content-type": "application/json",
                    "authorization": API_KEY
            }
            response = requests.post(url, json=payload, headers=headers, stream=True) # 此处request需要指定stream模式
            # 收集所有响应内容
            content = ""
            # 打印流式返回信息
            if response.status_code == 200: 
                for chunk in response.iter_content(chunk_size=8192): 
                    if chunk:
                        decoded_chunk = chunk.decode('utf-8')
                        content += decoded_chunk
                        print(decoded_chunk, end='')
            else:
                print('Request failed with status code:', response.status_code)
            return content  # 返回最终的响应内容
        except Exception as e:
            print(f"Error occurred: {e}")
            return str(e)  # 返回错误信息
