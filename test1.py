# a1:str=1
# names = ['Alice', 'Bob', 'Charlie']
# ages = [25, 30, 35]
# pairs = zip(names, ages)
# for p in pairs:
#     print(p)
#
# # for name, age in pairs:
# #       print(f"{name} is {age} years old.")
#
#
# from functools import reduce
# def test(x,y):
#     return x+y
#
#
# total=[]
# numbers = [1, 2, 3, 4, 5]
# total = reduce(test,numbers)
# print(total)  # 输出: 15
#
# for i in range(26):
#     globals()[chr(ord('a') + i)] = i + 1
#
# print(globals())
# fruits = ['苹果', '香蕉', '橙子']
# for fruit in fruits:
#     if fruit == '橙子':
#         break
#     print(fruit)
# else:
#     print("没有循环被中断")
#
#
# places = ["India", "London", "Poland", "Netherlands"]
# for place in places:
#     if place.startswith(('Lo', 'Po')):
#         print(place)

# def switch_case(case):
#     return {
#         'case1': 'This is case 1',
#         'case2': 'This is case 2',
#         'default': 'This is the default case'
#     }.get(case, 'Invalid case')
#
# result = switch_case('')
# print(result)

def power(exponent):
    print("exponent:", exponent)
    def calculate(number):
        print("number:",number)
        return number * exponent
    return calculate

square = power(3)
# cube = power(3)

a=square(4)
b=square(5)

print("a,b:",a,b)


# print(square(5))  # 输出: 25
# print(cube(2))   # 输出: 8


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

import os


# 加载.env文件
# os.environ["Home"]="test"

Home = os.environ.get('Home')


print(Home)

my_list=['a','b','c']
l1=dict(zip(range(len(my_list)), my_list))
for i,k in l1:

    print(i,k)