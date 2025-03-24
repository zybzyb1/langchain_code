import tkinter as tk
from tkinter import ttk
from langchain.prompts import PromptTemplate

# 定义多种Prompt模板
prompt_templates = {
    "文本总结": "任务: 根据输入内容生成一个简短的总结。\n输入: {input_text}\n总结:\n",
    "问答": "任务: 根据输入内容回答问题。\n输入: {input_text}\n问题: {question}\n答案:\n",
    "翻译": "任务: 将以下内容翻译成{target_language}。\n输入: {input_text}\n翻译:\n",
    "写作辅助": "任务: 根据输入内容生成一个相关的段落。\n输入: {input_text}\n生成内容:\n",
    "情感分析": "任务: 分析输入内容的情感倾向。\n输入: {input_text}\n情感分析:\n",
    "概念解释": "任务: 解释输入内容中的关键概念。\n输入: {input_text}\n解释:\n",
    "创意生成": "任务: 根据输入内容生成一个创意点子。\n输入: {input_text}\n创意点子:\n",
    "数据分析": "任务: 分析输入数据并总结关键信息。\n输入: {input_data}\n分析结果:\n",
    "对话生成": "任务: 根据输入内容生成一段对话。\n输入: {input_text}\n对话:\n",
    "逻辑推理": "任务: 根据输入内容进行逻辑推理。\n输入: {input_text}\n推理结果:\n",
    "代码生成": "任务: 根据输入需求生成代码。\n输入: {input_text}\n代码:\n",
    "文本润色": "任务: 对输入内容进行润色。\n输入: {input_text}\n润色后的内容:\n"
}

# 创建LangChain PromptTemplate
def create_prompt(template_name, **kwargs):
    template = prompt_templates[template_name]
    prompt = PromptTemplate.from_template(template)
    return prompt.format(**kwargs)

# GUI界面
def generate_output():
    template_name = template_var.get()
    input_text = input_entry.get("1.0", tk.END).strip()
    kwargs = {"input_text": input_text}
    if template_name == "问答":
        kwargs["question"] = question_entry.get()
    elif template_name == "翻译":
        kwargs["target_language"] = target_language_entry.get()
    elif template_name == "数据分析":
        kwargs["input_data"] = input_text
    output_text.delete("1.0", tk.END)
    try:
        result = create_prompt(template_name, **kwargs)
        output_text.insert("1.0", result)
    except Exception as e:
        output_text.insert("1.0", f"Error: {e}")

# 创建主窗口
root = tk.Tk()
root.title("Prompt Template Generator")
root.geometry("600x400")

# 下拉框选择模板
template_var = tk.StringVar()
template_label = tk.Label(root, text="选择模板：")
template_label.pack()
template_combobox = ttk.Combobox(root, textvariable=template_var, values=list(prompt_templates.keys()))
template_combobox.pack()

# 输入框
input_label = tk.Label(root, text="输入内容：")
input_label.pack()
input_entry = tk.Text(root, height=5)
input_entry.pack()

# 额外输入框（问答、翻译等）
question_label = tk.Label(root, text="问题（仅问答模板）：")
question_label.pack()
question_entry = tk.Entry(root)
question_entry.pack()

target_language_label = tk.Label(root, text="目标语言（仅翻译模板）：")
target_language_label.pack()
target_language_entry = tk.Entry(root)
target_language_entry.pack()

# 输出框
output_label = tk.Label(root, text="生成结果：")
output_label.pack()
output_text = tk.Text(root, height=10)
output_text.pack()

# 生成按钮
generate_button = tk.Button(root, text="生成", command=generate_output)
generate_button.pack()

root.mainloop()