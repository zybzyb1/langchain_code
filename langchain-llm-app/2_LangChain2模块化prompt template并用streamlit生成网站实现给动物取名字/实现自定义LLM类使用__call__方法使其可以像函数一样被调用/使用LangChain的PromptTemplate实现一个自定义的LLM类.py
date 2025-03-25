# 三、使用LangChain的PromptTemplate,实现一个自定义的LLM类，使用了__call__方法，使其可以像函数一样调用。
# 这里以LangChain的PromptTemplate为例，下面是使用LangChain的PromptTemplate的代码
from openai import OpenAI
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

def generate_prompt(country_name: str) -> str:
    template = """
    任务: 输入一个国家，输出该国家的首都。
    语言：中文

    输入格式：
    国家名称（请输入国家名称）: {country_name}

    输出格式（JSON格式）:
    {{
        "country_name": "国家名称",
        "capital_name": "首都名称"
    }}

    示例：
    国家名称：中国
    输出：
    {{
        "country_name": "中国",
        "capital_name": "北京"
    }}

    现在，请输入一个国家名称：
    """
    return template.format(country_name=country_name)

# 自定义硅基流动大模型类
class CustomLLM_Siliconflow:
    def __call__(self, prompt: str) -> str:
        # 初始化OpenAI客户端
        client = OpenAI(api_key=API_KEY, base_url="https://api.siliconflow.cn/v1")
        
        # 发送请求到模型
        response = client.chat.completions.create(
            model='THUDM/glm-4-9b-chat',
            messages=[
                {'role': 'user', 
                 'content': f"{prompt}"}  # 用户输入的提示
            ],
        )

        # 打印响应结构，以便调试
        # print("Response structure:", response)

        # 收集所有响应内容
        content = ""
        if hasattr(response, 'choices') and response.choices:
            for choice in response.choices:
                if hasattr(choice, 'message') and hasattr(choice.message, 'content'):
                    chunk_content = choice.message.content
                    # print(chunk_content, end='')  # 可选：打印内容
                    content += chunk_content  # 将内容累加到总内容中
        else:
            raise ValueError("Unexpected response structure")

        return content  # 返回最终的响应内容


if __name__ == '__main__':
    # 创建自定义LLM实例
    llm = CustomLLM_Siliconflow()
    
	# 基础版
    # 定义国家名称
    #country = """中国"""
     # 使用模板创建提示
    country_name = "法国"
    messages = generate_prompt(country_name)
    print(messages)

    # 获取模型响应
    response = llm(messages)
    print(response)  # 打印响应内容

