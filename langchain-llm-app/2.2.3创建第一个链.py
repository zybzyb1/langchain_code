from langchain import LLMChain
from openai import OpenAI
from langchain.prompts.chat import(
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

#初始化 ChatopenAI聊天模型，温度设置为0
chat =OpenAI(temperature=0)

#定义系统消息模板
template =(
    "You are a helpful assistant that translates (input_language)to "
    "{output_language}."
)
system_message_prompt=SystemMessagePromptTemplate.from_templahe(template)

#定义人类消息模板
human_template="{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

#将这两个模板组合到聊天提示词模板中
chat_prompt=ChatPromptTemplate.from_messages([
    system_message_prompt,
    human_message_prompt
])

#使用 LLMChain 组合聊天模型组件和提示词板
chain =LLMChain(llm=chat,prompt=chat_prompt)

#运行链，传人参数
chain.run(
    input_language="English",
    output_language="French",
    text="I love programming."
)
#输出结果：Je suis un assistant utile qui traduit (English) en Français.

