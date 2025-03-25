# 二. 自定义LLM实例，这里是调用上面第一点定义的LLM类，
# # 创建自定义LLM实例
# 示例调用部分
from openai import OpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv  # 导入dotenv库，用于加载环境变量
import os
from LangChain自定义大模型以OPENAI接口调用为例 import CustomLLM_Siliconflow

if __name__ == '__main__':
    # 创建自定义LLM实例
    llm = CustomLLM_Siliconflow()

    # 示例查询：将大象装进冰箱分几步？
    print("\nQuery: 把大象装进冰箱分几步？")
    print("Response:")
    llm("把大象装进冰箱分几步？")
    # print(llm("把大象装进冰箱分几步？"))

# 输出如下：
# 把大象装进冰箱一般被分为以下三个步骤：
# 打开冰箱门。
# 把大象放进冰箱里。
# 关闭冰箱门。
# 但实际上，这个问题通常是一个幽默性质的开场白，用来引起人们的兴趣或调侃。现实中，大象体形巨大，不可能被放进普通的家用冰箱中。这样的问题往往用于儿童游戏或成人间的玩笑。
