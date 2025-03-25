第 1 章 Langchain 入门
1.1 开始学习之前
1.1.1 为什么需要 Langchain
1.1.2 环境和密钥配置
1.2 定义 Langchain	
1.3	Langchain 的优点
1.3.1 4 行代码开始
1.3.2 核心模块
1.3.3 解决大模型先天缺陷
1.4	创建你的第一个 Langchain	应用程序	
1.4.1 Langchain 开发流程
1.4.2 创建你的第一个聊天机器人
1.4.3 减少 Prompt 输入
1.4.4 开始对话
1.5 (本章小结)

第 2 章 模型输入输出 (Model I/O)
2.1 语言模型 (Language models)
2.1.1 大语言模型（LLMs）
2.1.2 聊天模型 (Chat Models)
2.1.3 文本嵌入模型 (Text Embedding Models)
2.2  提示 (Prompts)
2.2.1 提示模板 (PromptTemplate)
2.2.2 示例提示模板 (FewShotPromptTemplate)
2.2.3 控制提示长度 (LengthBasedExampleSelector)
2.3 输出解析器 (Output Parsers)
2.3.1 输出列表[]格式
2.3.2 输出JSON格式
2.4 (本章小结)

第 3 章 数据连接 (Data Connection)
3.1 文档加载器(Documentoaders)
3.1.1 How-to
3.1.2 Integrations
3.2 文档转换器 (document transformers)
3.3 文本嵌入模型 (Text embeddingmodels)
3.4 向量存储 (Vector stores)
3.5 Retrievers (检索器)
3.5.1 How-to
3.6 (本章小结)

第 4 章 链 (Chains)
4.1 链是什么？
4.1.1 How to
4.2 基础 (Foundational)
4.2.1 LLM 链
4.2.2 顺序链(Sequential)
4.3 文档链 ( Documents )
4.3.1 文档通用链 (Stuffdocuments)
4.3.2 精化链 (Refine)
4.3.3 Map reduce 链 (Map Reduce)
4.3.4 重排链(Map re-rank)
4.4 热门链(Popular)
4.4.1 添加记忆链(state)
4.4.2 检索型问答链 (Retrieval QA)
4.4.3 对话式检索问答链(Conversational RetrievaQA)
4.4.5 SQL 链
4.4.6 摘要链 (summarize)
4.5 工具(Tools)
4.6 工具包(Toolkits)
4.7 (本章小结)

第 5 章 记忆
5.1 记忆组件概述
5.1.1 概述
5.1.2 记忆组件的区别
5.2 会话记忆
5.2.1 会话记忆和窗口记忆
5.3 摘要记忆
5.3.1 会话摘要和窗口会话摘要
5.4 实体和知识图谱
5.4.1 实体和知识图谱记忆
5.5 自定义记忆
5.5.1 自定义记忆组件
5.6 本章小结


第 6 章 代理人 (Agents)
6.1 代理类型 (agent_types)
6.1.2 会话(Conversational)
6.1.3 OpenAl 函数代理 (Functions Agent)
6.1.4 ReAct 代理 (ReAct)
6.1.5 结构化聊天代理(structured chat)
6.1.6 计划和执行代理 (plan and execute)
6.2 How-to
6.2.1 自定义 LLM 代理(custom llm agent)
6.2.1 自定义 LLM 代理(带有 ChatModel)
6.2.1 MRKL (mrkl chat)
6.5 (本章小结)

第 8 章 使用 Langchain 构建应用程序
7.1 How-to
7.2 第一个带记忆的报修机器人(Memory)
7.2.1 环境与配置
7.2.2 挑战难题
7.2.3 基础 (Memory)
7.2.4 复杂 (Memory)
7.2.5 用 chain 链接完成 (Memory)
7.3 自制 chatPDF (Chains)
7.3.1 环境与配置
7.3.2 挑战难题
7.3.3 基础 (Chains) 类型
7.3.4 复杂 (Chains)
7.3.5 用 chain 链接完成
7.4 对话式表单 (Model I/O)
7.4.1 环境与配置
7.4.2 挑战难题
7.4.3 基础 (prompt) 类型
7.4.4 复杂 (prompt) 
7.4.5 输出解析器
7.5 自定义代理工具 (Agents)
7.5.1 环境与配置
7.5.2 挑战难题
7.5.3 基础 (Agents) 类型
7.5.4 自定义代理
7.5.5 用 chain 链接完成
7.6 (本章小结)

附录 Langchain 源码的基本类名解释

## 注意事项
- `python .\addnewfile.py` 添加文件目录和文件夹。
- menu.md 存放所有的目录结构，版本控制，可以添加新的文件，命名规则为① 1.1.1 Nodejs 和npm => 1.1.1 换成新的文件名 ； ② 1.1.1 Nodejs 和npm =》 1.1.1 Nodejs 和npm （v2)


## 格式

1. 注释中文在前，s复数去掉，英文在后。
2. 标题不要英文标注，正文第一次出现，标注一次。
3. LMs vs Chat Models 的区别 格式为： LMs 和 Chat Models 的区别
4. 技术书籍用你，而不是你
5. 2个标题不要重复，如果重复的地方补充过渡的解释。
6. 图片在说明段落的后面，并且标注 “图 章节-顺序号”,比如“图 2-1”
7. 标题后不能直接上代码，可以中间写正文，或者将标题换成正文



