# 给动物取名字的程序

from openai import OpenAI  # 导入OpenAI模块
from dotenv import load_dotenv  # 导入dotenv库，用于加载环境变量
import os

# 加载.env文件中的环境变量
load_dotenv()

# 读取环境变量
API_KEY = os.getenv("API_KEY")

# 检查API密钥是否已正确加载
if not API_KEY:
    raise ValueError("API_KEY is not set. Please check your .env file.")

# 创建一个模板函数，用于生成不同动物的名字
def generate_pet_name(animal_type: str, prompt_template: str = None):
    """
    生成宠物名字的函数
    :param animal_type: 动物类型，例如 "dog", "cat" 等
    :param prompt_template: 提供给模型的提示模板，默认为 None，使用内置模板
    :return: 生成的名字（可选：带中文注释）
    """
    # 如果没有提供自定义模板，使用默认模板
    if not prompt_template:
        prompt_template = "I have a {animal_type} pet and I want a cool name for it. Suggest me five cool names for my pet."

    # 创建OpenAI模型的实例
    client = OpenAI(api_key=API_KEY, base_url="https://api.siliconflow.cn/v1")

    # 使用OpenAI模型生成宠物名字
    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V2.5",  # 指定模型
        messages=[{"role": "user", "content": prompt_template.format(animal_type=animal_type)}],
        temperature=0.7  # 设置temperature参数为0.7以调整生成的多样性
    )

    # 提取生成的名字
    name = response.choices[0].message.content.strip()
   
    return name  # 返回生成的名字

# 当该脚本作为主程序运行时，执行以下代码
if __name__ == "__main__":
    try:
        # 示例：为狗生成名字
        animal_type = input("Enter the type of your pet (e.g., dog, cat): ").strip().lower()
        print(f"Generated name for your {animal_type}: {generate_pet_name(animal_type)}")
    except Exception as e:
        print(f"An error occurred: {e}")
