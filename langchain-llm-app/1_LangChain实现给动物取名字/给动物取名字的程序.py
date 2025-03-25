#给动物取名字的程序
from openai import OpenAI  # 导入OpenAI模块
from dotenv import load_dotenv  # 导入dotenv库，用于加载环境变量
import os

# 加载.env文件中的环境变量
load_dotenv()

# 读取环境变量
OPENAI_API_KEY = os.getenv("API_KEY")

# 检查API密钥是否已正确加载
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set. Please check your .env file.")

def generate_pet_name():  # 定义一个函数generate_pet_name
    # 创建OpenAI模型的实例
    # 注意：OpenAI 的客户端初始化方式可能因版本而异，以下代码基于 OpenAI 官方库的典型用法
    client = OpenAI(api_key=OPENAI_API_KEY, base_url="https://api.siliconflow.cn/v1")  # 设置API密钥和自定义API地址

    # 使用OpenAI模型生成宠物名字。这里的字符串是向模型提供的提示，模型会基于此生成宠物名字。
    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V2.5",  # 指定模型
        messages=[{"role": "user", "content": "I have a dog pet and I want a cool name for it. Suggest me five cool names for my pet."}],
        temperature=0.7  # 设置temperature参数为0.7以调整生成的多样性
    )

    # 提取生成的名字
    name = response.choices[0].message.content.strip()

    return name  # 返回生成的名字

# 当该脚本作为主程序运行时，执行以下代码
if __name__ == "__main__":
    try:
        print(generate_pet_name())  # 调用generate_pet_name函数，并打印返回的结果
    except Exception as e:
        print(f"An error occurred: {e}")
