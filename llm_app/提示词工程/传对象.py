from langchain.prompts import HumanMessagePromptTemplate
from langchain_core.messages import SystemMessage
from langchain_core.prompts import ChatPromptTemplate

#使用langchain定义的SystemMessage、HuamengPromptTemplate类工具类定义消息，跟前面的例子类似，下面定义了两条消息
chat_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content=("你是一个乐于助人的助手，可以润色内容，使其看起来更简单易读。")
        ),
        HumanMessagePromptTemplate.from_template("{text}"),
    ]
)

#使用模板参数格式化模板
messages = chat_template.format(text="我不喜欢吃好吃的东西")
print(messages)
