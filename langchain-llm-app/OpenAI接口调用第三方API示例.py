
# 【方法2】通过 OpenAI接口调用。 如果你想要封装为一个大模型/对话模型，体验更高级功能，比如跟LangChain框架结合。
# 像下面这样调用openai的就叫OpenAI接口方法
from  openai import OpenAI

client = OpenAI(api_key='sk-eghruoxtqnjsqdcawudlezrujqghgqgdymbnyqhvxkvkifhs',base_url='https://api.siliconflow.cn/v1')

response =  client.chat.completions.create(
    model='deepseek-ai/DeepSeek-V2.5',
    messages=[
        {
            'role': 'user',
            'content': 'SiliconCloud摧出分层速率方案与免费模型RPM提升10倍速率',
        }
    ],
    stream=True
)
for chunk in response:
    print(chunk.choices[0].delta.content,end='')










