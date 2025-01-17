"""
用字典調用函數
"""

def addition(x,y):
    return x+y

def subtraction(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def division(x,y):
    return x/y

dict1 = {
"1":addition,
"2":subtraction,
"3":multiplication,
"4":division
}

x,y=2,3
d="1"
result=dict1.get(d)(x,y)
print(result)




