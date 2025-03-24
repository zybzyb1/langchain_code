#MessagesPlaceholder 这个提示模板负责在特定位置添加消息列表。在上面的ChatPromptTemplate中，
# 我们看到了如何格式化两条消息，每条消息都是一个字符串。 但是，如果我们希望用户传入一个消息列表，
# 我们将其插入到特定位置，该怎么办?这就是您使用 MessagesPlaceholder的方式。
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant"),
    MessagesPlaceholder("msgs")
])

prompt_template.invoke({"msgs": [HumanMessage(content="hi!")]})