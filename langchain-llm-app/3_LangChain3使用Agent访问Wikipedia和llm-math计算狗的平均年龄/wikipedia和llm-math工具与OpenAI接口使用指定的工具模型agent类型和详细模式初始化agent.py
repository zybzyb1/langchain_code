# 从langchain库中导入模块
#pip install langchain-community -i https://pypi.tuna.tsinghua.edu.cn/simple 从国内指定的源安装langchain-community
#from openai import OpenAI  # 从openai导入OpenAI模块
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate  # 从langchain.prompts导入PromptTemplate模块
from langchain.chains import LLMChain  # 从langchain.chains导入LLMChain模块
from dotenv import load_dotenv  # 从dotenv导入load_dotenv，用于加载环境变量
#from langchain.agents import load_tools  # 从langchain.agents导入load_tools函数
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import initialize_agent  # 从langchain.agents导入initialize_agent函数
from langchain.agents import AgentType  # 从langchain.agents导入AgentType枚举类
from langchain_community.tools import WikipediaQueryRun  # 从langchain.tools导入WikipediaQueryRun
#from langchain.utilities import WikipediaAPIWrapper  # 从langchain.utilities导入WikipediaAPIWrapper
from langchain_community.utilities import WikipediaAPIWrapper
import os  # 导入os模块

load_dotenv()  # 加载.env文件中的环境变量
# 读取环境变量--API密钥
API_KEY = os.getenv("API_KEY")

# 检查API密钥是否已正确加载
if not API_KEY:
    raise ValueError("API_KEY is not set. Please check your .env file.")
def langchain_agent():
    try:
        llm = OpenAI(
                api_key=API_KEY,
                base_url="https://api.siliconflow.cn/v1",  # 确保 base_url 正确
                model="deepseek-ai/DeepSeek-V2.5"  # 确保模型名称正确
            ) # 创建OpenAI模型实例
        tools = load_tools(["wikipedia", "llm-math"], llm=llm)  # 加载wikipedia和llm-math工具，与OpenAI模型实例一起使用
        agent = initialize_agent(
            tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True  # 使用指定的工具、模型、agent类型和详细模式初始化agent
        )
        result = agent.run(
            "What is the average age of a dog? Multiply the age by 3"  # 使用一个提示语来运行agent进行处理
        )
        print(result)  # 打印agent的输出
    except Exception as e:
            print(f"Error occurred: {e}")
# 主执行检查
if __name__ == "__main__":
    langchain_agent()  # 如果脚本是主程序，则运行langchain_agent函数

