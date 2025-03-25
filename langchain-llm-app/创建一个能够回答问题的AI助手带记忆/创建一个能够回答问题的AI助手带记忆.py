# 创建基础应用框架
# 让我们从最简单的开始，创建一个能够回答问题的AI助手：

#from openai import OpenAI  # 导入OpenAI模块
from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

# 加载环境变量
load_dotenv()

# 读取环境变量
OPENAI_API_KEY = os.getenv("API_KEY")

# 初始化LLM
llm =  OpenAI(api_key=OPENAI_API_KEY,base_url='https://api.siliconflow.cn/v1')

# 创建提示模板
prompt = PromptTemplate(
    input_variables=["question"],
    template="请回答下面的问题：{question}"
)
# 创建chain
chain = LLMChain(llm=llm, prompt=prompt)

# 测试运行
response = chain.run("什么是人工智能？")
print(response)

# 在这个基础框架中，我使用了几个重要的LangChain组件：

# LLM：语言模型的抽象层
# PromptTemplate：提示词模板
# LLMChain：将LLM和提示词模板串联起来