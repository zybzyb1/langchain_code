# 二. 自定义LLM实例，这里是调用上面第一点定义的LLM类，
# # 创建自定义LLM实例
# 示例调用部分
if __name__ == '__main__':
    # 创建自定义LLM实例
    llm = CustomLLM_Siliconflow()

    # 示例查询：将大象装进冰箱分几步？
    print("\nQuery: 把大象装进冰箱分几步？")
    print("Response:")
    llm("把大象装进冰箱分几步？")
    # print(llm("把大象装进冰箱分几步？"))
