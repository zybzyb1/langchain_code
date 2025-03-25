from langchain.agents import Tool, AgentExecutor, LLMSingleActionAgent
from langchain import OpenAI, LLMChain
from langchain.utilities import DuckDuckGoSearchAPIWrapper
from langchain.prompts import PromptTemplate
import sys
sys.path.append("./2_LangChain2模块化prompt template并用streamlit生成网站实现给动物取名字./folder1")  # 将 script1.py 所在的文件夹路径添加到系统路径

from script1 import CustomLLM_Siliconflow
from LangChain自定义大模型以OPENAI接口调用为例 import CustomLLM_Siliconflow
# 定义一个工具组件来获取天气信息
def get_weather(city):
    # 这里可以调用实际的天气API，例如 OpenWeatherMap
    # 为了示例，我们使用一个简单的搜索工具
    search = DuckDuckGoSearchAPIWrapper()
    results = search.run(f"weather in {city}")
    return results

weather_tool = Tool(
    name="WeatherTool",
    func=get_weather,
    description="Useful for getting weather information"
)

# 定义一个工具组件来识别用户问题是否是关于天气的
def is_weather_question(question):
    # 简单的关键词匹配，可以扩展为更复杂的意图识别模型
    weather_keywords = ["weather", "temperature", "forecast", "rain", "sun"]
    return any(keyword in question.lower() for keyword in weather_keywords)

weather_question_tool = Tool(
    name="WeatherQuestionTool",
    func=is_weather_question,
    description="Useful for determining if the user's question is about weather"
)

# 定义一个链来处理用户问题
def process_user_question(question):
    # 首先检查问题是否是关于天气的
    if weather_question_tool.func(question):
        # 如果是天气问题，调用天气工具
        city = extract_city_from_question(question)
        return weather_tool.func(city)
    else:
        # 如果不是天气问题，返回一个通用回答
        return "I can help with other questions too! Please ask me anything."

# 定义一个函数来从问题中提取城市名称
def extract_city_from_question(question):
    # 简单的字符串匹配，可以扩展为更复杂的实体识别模型
    city_keywords = ["in", "at", "for"]
    words = question.split()
    for i, word in enumerate(words):
        if word.lower() in city_keywords and i + 1 < len(words):
            return words[i + 1]
    return "New York"  # 默认城市

# 定义一个简单的代理来处理用户问题
def weather_agent():
    tools = [weather_question_tool, weather_tool]
    llm = CustomLLM_Siliconflow()# OpenAI(temperature=0)
    prompt = PromptTemplate(
        input_variables=["question"],
        template="Question: {question}\nAnswer:"
    )
    llm_chain = llm(prompt=prompt) #LLMChain(llm=llm, prompt=prompt)
    agent = LLMSingleActionAgent(
        llm_chain=llm_chain,
        tools=tools,
        verbose=True
    )
    return AgentExecutor.from_agent_and_tools(agent=agent, tools=tools)

# 使用代理处理用户问题
agent = weather_agent()
user_question = "What's the weather like in London today?"
response = agent.run(user_question)
print(response)
