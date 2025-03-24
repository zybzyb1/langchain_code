# 2. ChatPrompt Templates
# 聊天模型提示词模板ChatPrompt Templates，ChatModels接受聊天消息列表作为输入。列表一般是不同的提示，并且每个列表消息一般都会有一个角色。

from langchain.prompts import (
    ChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
# HumanMessage:
# 这是一个用户（人类）发送的消息，需要助手处理或响应。
# 内容是：I love programming.
# SystemMessage:
# 这是一个系统消息，用于定义助手的行为或角色。在这个例子中，它告诉助手它是一个将英语翻译成法语的助手。
# 内容是：You are a helpful assistant that translates English to French.


# 你的代码通过 langchain 的模板系统构建了一个聊天提示（ChatPromptTemplate），并填充了具体的输入参数。
# 这里定义了一个系统消息模板，其中包含两个变量：{input_language} 和 {output_language}
template="You are a helpful assistant that translates {input_language} to {output_language}."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template="{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

# 将系统消息模板和用户消息模板组合成一个聊天提示模板。
chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
# 格式化并输出消息:
# 使用 format_prompt 方法填充模板中的变量：
# input_language 被替换为 "English"。
# output_language 被替换为 "French"。
# text 被替换为 "I love programming."。
# 调用 to_messages() 方法将格式化后的模板转换为实际的消息列表。
print(chat_prompt.format_prompt(input_language="English", output_language="French", text="I love programming.").to_messages())
# 输出结果是一个包含两条消息的列表：
# 系统消息：定义了助手的角色和任务（翻译英语到法语）。
# 用户消息：用户输入的内容（I love programming.），需要助手翻译。






