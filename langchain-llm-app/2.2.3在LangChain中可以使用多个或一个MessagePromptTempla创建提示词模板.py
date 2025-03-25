# 在 LangChain 中，可以使用 MessagePromptTemplate 来创建提示词模板。
# 可以用-个或多个 MessagePromptTemplate 创建一个 ChatPromptTemplate，
# 示例代码如下:

from langchain.prompts.chat  import(
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

template=(
    "You are a helpful assistant that translates (input language) to "
    "{output language}."
)
system_message_prompt =SystemMessagePromptTemplate.from_template(template)

human_template = "{text}"
human_message_prompt=HumanMessagePromptTemplate.from_template(human_template)

chat_prompt=ChatPromptTemplate.from_messages([
    system_message_prompt,
    human_message_prompt
])

chat_prompt.format_messages(
    input_language="English",
    output_language="French",
    text="I love programming."
)

