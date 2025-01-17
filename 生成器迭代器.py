import timeit  # 时间模块
import sys  # 系统模块 可以通过getsizeof() 计算变量在内存中所使用的内存消耗
import datetime
def 生成器():
    a1=datetime.datetime.now()
    list_1 = [x for x in range(100000000)]
    total2=0
    for i in list_1:
        total2+=1
    print(total2)
    a2=datetime.datetime.now()
    print(a2-a1)

    # t = timeit.timeit(stmt='list_1 = [x for x in range(2, 1000000, 2)]', number=10)
    # print(f"创建列表耗时{t:f}")
    # print(f"创建列表内存消耗{sys.getsizeof(list_1):d}")
    b1=datetime.datetime.now()
    # 元组推导式创建生成器
    gen_1 = (x for x in range(100000000))

    # t1 = timeit.timeit(stmt='gen_1=(x for x in range(2,1000000,2))', number=10)
    # print(f"创建生成器耗时{t1:f}")
    # print(f"创建生成器内存消耗{sys.getsizeof(gen_1):d}")
    '''
    创建列表耗时0.266365
    创建列表内存消耗4167352
    创建生成器耗时0.000007
    创建生成器内存消耗104
    '''
    total1=0
    for i in gen_1:
        total1+=1
    print(total1)
    b2=datetime.datetime.now()
    print(b2-b1)
    # 可以明显看到创建生成器耗时以及内存消耗都比创建列表小很多


    c1=datetime.datetime.now()
    # 用yield创建生成器
    def gen_func():
        for x in range(100000000):
            yield x
    f=gen_func()
    total3=0
    for i in f:
        total3 += 1
    print(total3)
    c2=datetime.datetime.now()
    print(c2-c1)

def 生成器表达式():
    """
    1. 创建生成器函数
    生成器函数使用 def 关键字定义，但在函数体内使用 yield 而不是 return 来产生值。
    """

    def simple_generator():
        yield 1
        yield 2
        yield 3

    """
    2. 使用生成器
    你可以像使用迭代器一样使用生成器。例如，你可以使用 next() 函数来获取下一个值，或者使用循环来迭代生成器的值。
    """
    gen = simple_generator()

    print(next(gen))  # 输出: 1
    print(next(gen))  # 输出: 2
    print(next(gen))  # 输出: 3
    print(next(gen))  # 引发 StopIteration 异常

    #或者使用循环
    for value in simple_generator():
        print(value)
    # 输出:
    # 1
    # 2
    # 3
    """
    3.生成器表达式
    生成器表达式类似于列表推导式，但使用圆括号而不是方括号。它们返回一个生成器对象，而不是列表。
    return:
    """
    gen_expr = (x * x for x in range(5))

    for value in gen_expr:
        print(value)
    # 输出:
    # 0
    # 1
    # 4
    # 9
    # 16

def 嵌套生成器():
    """
    6. 嵌套生成器
    你可以在一个生成器内部调用另一个生成器，实现复杂的迭代逻辑。
    :return:
    """
    def nested_generator():
        for i in range(3):
            for j in range(2):
                yield (i, j)

    for value in nested_generator():
        print(value)
    # 输出:
    # (0, 0)
    # (0, 1)
    # (1, 0)
    # (1, 1)
    # (2, 0)
    # (2, 1)

def 生成器send():
    """
    7. 生成器的 send() 方法
    除了 next()，生成器对象还有 send() 方法，它允许你发送一个值到生成器内部，并在 yield 表达式处接收这个值。

    :return:
    """
    def echo_generator():
        while True:
            received = yield
            print(f"Echo: {received}")

    gen = echo_generator()
    next(gen)  # 启动生成器
    gen.send("Hello")  # 输出: Echo: Hello
    gen.send("World")  # 输出: Echo: World


生成器send()
# 生成器()