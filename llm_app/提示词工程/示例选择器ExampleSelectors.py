# 3. Example Selectors
# 示例选择器Example Selectors，如果有多个案例的时候，使用ExampleSelectors选择一个案例让提示词使用：

# 自定义的案例选择器。
# 基于长度的案例选择器，输入长的时候按理会少一点，输入多的时候，案例会多一些。
# 相关性选择器，选择一个和输入最相关的案例。
# 你的代码实现了一个自定义的 CustomExampleSelector 类，继承自 langchain 的 BaseExampleSelector。
# 这个类用于从一组示例中选择示例，并且可以根据需要添加新的示例。以下是对代码的详细解析和一些补充说明。
from langchain.prompts.example_selector.base import BaseExampleSelector
from typing import Dict, List
import numpy as np
# BaseExampleSelector 是 LangChain 提供的基类，用于定义示例选择器的基本接口。
# Dict 和 List 是类型注解，用于明确函数和变量的类型。
# numpy 用于实现随机选择功能。

# 定义 CustomExampleSelector 类
class CustomExampleSelector(BaseExampleSelector):
# __init__ 方法初始化一个示例列表 self.examples，存储所有示例数据。
# 每个示例是一个字典，例如 {"foo": "1"}。
    def __init__(self, examples: List[Dict[str, str]]):
        self.examples = examples
# 添加示例的方法,add_example 方法允许向示例列表中添加新的示例。
    def add_example(self, example: Dict[str, str]) -> None:
        """Add new example to store for a key."""
        self.examples.append(example)

# 选择示例的方法
    def select_examples(self, input_variables: Dict[str, str]) -> List[dict]:
        """Select which examples to use based on the inputs."""
        return np.random.choice(self.examples, size=2, replace=False)
# select_examples 方法根据输入变量选择示例。
# 在你的实现中，选择逻辑是随机从 self.examples 中选择 2 个示例，且不重复（replace=False）。
# 返回的是一个包含两个随机选择的示例的列表。

# 测试代码
examples = [
    {"foo": "1"},
    {"foo": "2"},
    {"foo": "3"}
]

# Initialize example selector.
example_selector = CustomExampleSelector(examples)
# Select examples
print(example_selector.select_examples({"foo": "foo"}))
# -> array([{'foo': '2'}, {'foo': '3'}], dtype=object)
# Add new example to the set of examples
example_selector.add_example({"foo": "4"})
print(example_selector.examples)
# -> [{'foo': '1'}, {'foo': '2'}, {'foo': '3'}, {'foo': '4'}]
# Select examples
print(example_selector.select_examples({"foo": "foo"}))
# -> array([{'foo': '1'}, {'foo': '4'}], dtype=object)
# 初始化示例选择器时传入了 3 个示例。
# 第一次调用 select_examples 随机选择了 2 个示例。
# 添加了一个新的示例后，再次调用 select_examples，随机选择了 2 个示例。

# 补充说明
# 随机性：
# np.random.choice 的 size=2 和 replace=False 确保每次随机选择两个不重复的示例。
# 如果 self.examples 中的示例数量少于 2，会抛出错误。可以添加检查逻辑来避免这种情况。
# 输入变量的作用：
# 在你的实现中，input_variables 参数没有被使用。select_examples 方法完全是基于随机性选择示例。
# 如果需要根据 input_variables 进行更复杂的筛选逻辑，可以在 select_examples 方法中添加相关的逻辑。
# 返回类型：
# np.random.choice 返回的是一个 NumPy 数组，但你的方法注解返回的是 List[dict]。虽然这不会影响代码运行，但为了保持一致性，可以将返回值转换为列表：
# return list(np.random.choice(self.examples, size=2, replace=False))
# def select_examples(self, input_variables: Dict[str, str]) -> List[dict]:
#     """Select which examples to use based on the inputs."""
#     # 假设根据 input_variables 中的 'foo' 键筛选
#     filtered_examples = [example for example in self.examples if example.get("foo") == input_variables.get("foo")]
    
#     # 如果筛选结果为空，返回随机选择的示例
#     if not filtered_examples:
#         return list(np.random.choice(self.examples, size=2, replace=False))
    
#     # 如果有匹配的示例，返回匹配的示例
#     return filtered_examples[:2]
# 这样，select_examples 方法会根据输入变量的值筛选示例，如果没有匹配的示例，则随机选择。






# 改进建议
# 如果你希望根据输入变量对示例进行筛选，可以修改 select_examples 方法。例如，根据 input_variables 中的某个键值对筛选出与之匹配的示例：