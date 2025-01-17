"""
在 Python 中，封装（Encapsulation）是面向对象编程（OOP）的一个核心概念。它通过将对象的属性和方法隐藏起来，只暴露必要的接口给外界，从而实现对对象的内部状态的保护和控制。

封装的主要目的是：

保护数据：防止外部代码直接访问或修改对象的内部状态。
简化接口：只提供必要的接口，使对象的使用更加简单和直观。
灵活性：可以在不改变外部接口的情况下，修改内部实现。
在 Python 中，可以通过以下方式实现封装：

使用双下划线（__）前缀的私有属性：虽然 Python 并没有真正的私有属性，但使用双下划线前缀的变量名会被“名称重整”（name mangling），使得它们从外部难以直接访问。
使用属性装饰器（@property）：可以定义只读的属性，或者添加对属性值的校验逻辑。
提供公共的 getter 和 setter 方法：通过定义这些方法，可以控制对属性的访问和修改。
"""
class Person:
    def __init__(self, name, age):
        self.__name = name  # 私有属性，使用双下划线前缀
        self.__age = age    # 私有属性，使用双下划线前缀
        self.name1=name+"1"

    # 使用 @property 装饰器提供公共的 getter 方法
    @property
    def name(self):
        return self.__name

    # 使用 @name.setter 装饰器提供公共的 setter 方法
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise ValueError("Name must be a string")
        self.__name = new_name

    # 提供一个公共的 getter 方法
    def get_age(self):
        return self.__age

    # 提供一个公共的 setter 方法，并添加校验逻辑
    def set_age(self, new_age):
        if not isinstance(new_age, int) or new_age < 0:
            raise ValueError("Age must be a non-negative integer")
        self.__age = new_age

# 创建一个 Person 对象
person = Person("Alice", 30)

# 访问公共属性
print(person.name)  # 输出: Alice

# 修改公共属性
person.name = "Bob"
print(person.name)  # 输出: Bob

# 使用公共的 getter 和 setter 方法
print(person.get_age())  # 输出: 30
person.set_age(31)
print(person.get_age())  # 输出: 31

# 尝试直接访问私有属性（会报错）
# print(person.__name)  # AttributeError: 'Person' object has no attribute '__name'
# 尝试设置无效的年龄（会报错）
# person.set_age(-5)  # ValueError: Age must be a non-negative integer