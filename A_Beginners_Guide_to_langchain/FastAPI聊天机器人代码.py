from fastapi import FastAPI, Request, HTTPException
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from openai import OpenAI
from dotenv import load_dotenv  # 导入dotenv库，用于加载环境变量
import os
from Custom_LLM_Class import CustomLLM_Siliconflow
from Custom_Stream_LLM_Class import Custom_Stream_LLM_Siliconflow
# 创建FastAPI应用实例
app = FastAPI()

# 定义请求模型
from pydantic import BaseModel

class ChatRequest(BaseModel):
    input: str

# 创建 LLMChain
# 假设你已经定义了CustomLLM_Siliconflow类和prompt模板
# 这里需要根据你的实际需求进行调整
# prompt = PromptTemplate(...)  # 定义你的提示模板
# llm = CustomLLM_Siliconflow()  # 创建自定义LLM实例
# chat_chain = LLMChain(llm=llm, prompt=prompt)

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        # 运行链式调用
        # 假设CustomLLM_Siliconflow是一个函数或类方法，能够处理输入并返回响应
        # 如果CustomLLM_Siliconflow是一个类，你需要先创建其实例
        # response = chat_chain.run(request.input)
        llm = CustomLLM_Siliconflow()
        response = llm(request.input)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


#  运行方式：
# 安装必要的依赖：
# pip install fastapi uvicorn langchain openai
# 将代码保存为 main.py，并在代码中替换 你的密钥 为你的 OpenAI API 密钥。
# 运行应用：
# python main.py
# 访问 http://localhost:8000/docs 可以看到 FastAPI 自动生成的 API 文档，测试 /chat 接口。
# 测试请求示例：
# {
#   "input": "你好，今天天气怎么样？"
# }
# 响应示例：
# {
#   "response": "今天天气不错哦！"
# } 