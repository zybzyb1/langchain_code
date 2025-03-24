#通过继承 StringPromptTemplate 创建自定义模板类
#重写 format 方法来自定义模板的格式化逻辑。format 方法的输入是一个字典，包含模板中需要的变量，输出是一个 PromptValue 对象。

from langchain.prompts import StringPromptTemplate

#这个自定义类的输入变量包括 question 和 context，模板会生成一个包含上下文和问题的提示。
class CustomQuestionTemplate(StringPromptTemplate):
    def format(self, input_variables: dict) -> str:
        question = input_variables.get("question", "No question provided.")
        context = input_variables.get("context", "No context provided.")
        prompt = f"Context: {context}\nQuestion: {question}\nAnswer:"
        return  prompt
    

#使用上面自定义模板
#创建自定义模板实例
custom_template = CustomQuestionTemplate(input_variables=["question", "context"])

# 输入变量
input_variables = {
    "question": "What is the capital of France?",
    "context": "France is a country in Europe."
}

# 格式化提示
formatted_prompt = custom_template.format(input_variables)

# 输出结果
print(formatted_prompt)

