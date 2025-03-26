# 在 LangChain 中，可以使用 MessagePromptTemplate 来创建提示词模板。
# 可以用-个或多个 MessagePromptTemplate 创建一个 ChatPromptTemplate，
# 示例代码如下:

from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

# 定义系统消息模板
template = (
    "You are a helpful assistant that translates {input_language} to "
    "{output_language}."
)
system_message_prompt = SystemMessagePromptTemplate.from_template(template)

# 定义人类消息模板
human_template = "{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

# 创建聊天提示模板
chat_prompt = ChatPromptTemplate.from_messages([
    system_message_prompt,
    human_message_prompt
])

# 格式化消息
messages = chat_prompt.format_messages(
    input_language="English",
    output_language="French",
    text="I love programming."
)

# 打印结果
for message in messages:
    print(f"{message.type}: {message.content}\n")
