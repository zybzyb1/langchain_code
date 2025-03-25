from langchain import LLMChain
from langchain.llms.base import LLM
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from dotenv import load_dotenv  # 导入dotenv库，用于加载环境变量
import os
from openai import OpenAI




# 加载环境变量
load_dotenv()

# 获取API密钥
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY is not set. Please check your .env file.")

# 自定义硅基流动大模型类
class CustomLLM_Siliconflow(LLM):
    def _call(self, prompt: str, stop: list = None) -> str:
        try:
            # 初始化OpenAI客户端，使用硅基流动的API地址
            client = OpenAI(api_key=API_KEY, base_url="https://api.siliconflow.cn/v1")
            
            # 发送请求到模型
            response = client.chat.completions.create(
                model="THUDM/glm-4-9b-chat",
                messages=[
                    {'role': 'user', 'content': prompt}
                ],
            )

            # 提取响应内容
            content = ""
            if hasattr(response, 'choices') and response.choices:
                for choice in response.choices:
                    if hasattr(choice, 'message') and hasattr(choice.message, 'content'):
                        content += choice.message.content
            else:
                raise ValueError("Unexpected response structure")

            return content
        except Exception as e:
            print(f"Error occurred: {e}")
            return str(e)
    
    def _llm_type(self) -> str:
        return "custom_siliconflow_llm"

# 初始化自定义的硅基流动大模型
siliconflow_llm = CustomLLM_Siliconflow()

# 定义提示词模板
template = (
    "You are a helpful assistant that translates {input_language} to "
    "{output_language}. {text}"
)
prompt = PromptTemplate.from_template(template)

# 使用LLMChain组合模型和提示词模板
chain = LLMChain(llm=siliconflow_llm, prompt=prompt)

# 运行链，传入参数
result = chain.invoke({"input_language": "English", "output_language": "Chinese", "text": "Hello, welcome to langchain!"})

print(result)