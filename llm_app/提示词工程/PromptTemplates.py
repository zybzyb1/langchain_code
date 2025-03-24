# 1. PromptTemplates
# 语言模型提示词模板PromptTemplates，提示模板可以让我们重复的生成提示，复用我们的提示。它包含一个文本字符串（“模板”），从用户那里获取一组参数并生成提示，包含：

# 对语言模型的说明，应该扮演什么角色。
# 一组少量示例，以帮助LLM生成更好的响应。
# 具体的问题。

from langchain import PromptTemplate

template = """
I want you to act as a naming consultant for new companies.
What is a good name for a company that makes {product}?
"""

prompt = PromptTemplate(
    input_variables=["product"],
    template=template,
)
prompt.format(product="colorful socks")
# -> I want you to act as a naming consultant for new companies.
# -> What is a good name for a company that makes colorful socks?
