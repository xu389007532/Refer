"""
允许对象通过相同的接口（方法）表现出不同的行为。多态性增强了代码的灵活性和可扩展性。在Python中，多态性主要通过继承和接口（虽然Python没有显式的接口定义，但可以通过抽象基类来实现）来实现。
"""
#在这个例子中，Animal类是一个基类，它定义了一个抽象方法speak，该方法在派生类Dog和Cat中被重写。animal_speak函数接受一个Animal类型的参数，并在运行时调用speak方法，表现出不同的行为。
# 定义一个基类
class Animal:
    def speak(self):
        return "Subclasses must implement this method"

# 定义派生类
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# 使用基类类型的引用调用方法
def animal_speak(animal: Animal):
    print(animal.speak())

# 创建派生类的对象
dog = Dog()
cat = Cat()
animal=Animal()
# 调用方法，表现出不同的行为

animal_speak(dog)  # 输出: Woof!
animal_speak(cat)  # 输出: Meow!
animal_speak(animal)


##################################
#在这个例子中，Animal类通过继承ABC并定义抽象方法speak成为了一个抽象基类。这确保了所有派生类都必须实现speak方法。
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# 同样的使用方式
def animal_speak(animal: Animal):
    print(animal.speak())

dog = Dog()
cat = Cat()

animal_speak(dog)  # 输出: Woof!
animal_speak(cat)  # 输出: Meow!
######################################


