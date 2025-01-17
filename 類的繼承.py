class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# 创建 Dog 和 Cat 类的实例
dog = Dog("Rex")
cat = Cat("Whiskers")
print(dog.speak()) # 输出: Rex says Woof!
print(cat.speak()) # 输出: Whiskers says Meow!
A=Animal("cd")
print(A.speak())
