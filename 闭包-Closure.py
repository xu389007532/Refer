# 闭包（Closure）的魔法
# 闭包是Python中一个非常强大的特性，它允许内部函数记住并访问外部函数的变量，即使外部函数已经执行完毕。
# 解析：remember_last_number返回了一个闭包tell_me，这个闭包记住了last的值。即使remember_last_number执行结束，last的值仍然被闭包保留。
# 闭包的应用场景：缓存计算结果、创建带状态的函数等。

def remember_last_number(last=0):
    def tell_me():
        return last
    return tell_me

memory = remember_last_number(42)
print(memory()) # 输出：42


def outer_function(x):
    def inner_function(y):
        return 'x + y'
    def inner_function2(y):
        return 'x * y'
    if x>10:
        return inner_function
    else:
        return inner_function2


closure = outer_function(15)
print(closure)
result = closure(3)
print(result)  # 输出 8
