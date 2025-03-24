#导入langchain 提示词模版库
from langchain_core.prompts  import ChatPromptTemplate

#通过一个消息数组创建消息模版
# 数组每个元素代表一个消息，每个消息元组，第一个元素代表消息角色(也成为消息类型)，第二个元素代表消息内容。
# 消息角色：system代表系统消息，human代表人类消息，ai代表LLM返回的消息内容
# 下面消息定义了2个模板参数name和user_input
chat_template = ChatPromptTemplate.from_messages(
    [
        ("system","你是一位人工智能助手，你的名字是{name}."),
        ("human","你好"),
        ("ai","我很好，谢谢"),
        ("human","{user_input}"),
    ]
)


#通过模板参数格式化模板内容
messages = chat_template.format_messages(name="Bob",user_input="你的名字叫什么？")
print(messages)




