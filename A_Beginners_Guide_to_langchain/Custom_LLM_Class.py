# 一、LangChain自定义大模型，定义了一个自定义的LLM类，实现了__call__方法，使其可以像函数一样被其它脚本或代码调用。
# 下面使用二节的代码，将自定义的LLM实例化，并调用它来获取模型的响应。
# 这里以硅基流动网站的API接口为例，下面是LangChain自定义大模型的代码    #智谱zhipu的glm-3也可以，
#0.1 基于 openai 库的流式输出
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


# 自定义硅基流动大模型类
class CustomLLM_Siliconflow:
    def __call__(self, prompt: str) -> str:
        try:
            # 初始化OpenAI客户端（base_url是硅基流动网站的地址）
            client = OpenAI(api_key=API_KEY, base_url="https://api.siliconflow.cn/v1")
        
            # 发送请求到模型
            response = client.chat.completions.create(
                model= 'THUDM/glm-4-9b-chat',#"deepseek-ai/DeepSeek-V2.5",  #
                messages= #"""你是一个发言友好的 AI 助理。请现在回答用户的提问:{prompt}。"""
                [
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
                        print(chunk_content, end='')  # 可选：打印内容
                        content += chunk_content  # 将内容累加到总内容中
            else:
                raise ValueError("Unexpected response structure")

            return content  # 返回最终的响应内容
        except Exception as e:
            print(f"Error occurred: {e}")
            return str(e)  # 返回错误信息
         

# 注释说明
# API密钥：定义了访问OpenAI API的密钥。
# 自定义硅基流动大模型类：定义了一个自定义的LLM类，实现了__call__方法，使其可以像函数一样调用。
# 初始化OpenAI客户端：使用API密钥和基础URL初始化OpenAI客户端。
# 发送请求到模型：构建并发送一个包含用户输入提示的消息到指定的模型。
# 收集所有响应内容：遍历响应中的每个块，提取内容并累加到总内容中。
# 返回最终的响应内容：将收集到的所有内容作为最终结果返回。

# 二. 自定义LLM实例，这里是调用上面第一点定义的LLM类，
# # 创建自定义LLM实例
# 示例调用部分
# if __name__ == '__main__':
#     # 创建自定义LLM实例
#     llm = CustomLLM_Siliconflow()

#     # 示例查询：将大象装进冰箱分几步？
#     print("\nQuery: 把大象装进冰箱分几步？")
#     print("Response:")
#     llm("把大象装进冰箱分几步？")
#     

# 输出如下：
# 把大象装进冰箱一般被分为以下三个步骤：
# 打开冰箱门。
# 把大象放进冰箱里。
# 关闭冰箱门。
# 但实际上，这个问题通常是一个幽默性质的开场白，用来引起人们的兴趣或调侃。现实中，大象体形巨大，不可能被放进普通的家用冰箱中。这样的问题往往用于儿童游戏或成人间的玩笑。


