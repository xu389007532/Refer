import test1

def 基礎語法():
    """
    1. 标识符对大小写敏感.
    2. 保留字: 'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally',
    'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
    3.1 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）
    3.2 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）
    type(x) 類型: 'str', 'int', 'tuple', 'list'



    """

def 注意問題或用法():
    def map用法():

        """
        ***将元组转换成list***
        >>> map(int, (1,2,3))
        [1, 2, 3]
        ***将字符串转换成list***
        >>> map(int, '1234')
        [1, 2, 3, 4]
        ***提取字典的key，并将结果存放在一个list中***
        >>> map(int, {1:2,2:3,3:4})
        [1, 2, 3]
        ***字符串转换成元组，并将结果以列表的形式返回***
        >>> map(tuple, 'agdf')
        [('a',), ('g',), ('d',), ('f',)]
        #将小写转成大写

        """
    def rang用法():
        # rang() 在for中的用法
        for i in range(5):  # range(5) = 0,1,2,3,4 共5個數
            print(i, end=", ")
        for i in range(10, 18):  # range(10,18) = 10, 11, 12, 13, 14, 15, 16, 17 共8個數
            print(i, end="| ")
        for i in range(10, 18, 2):  # range(10,18,2) = 10,12,14,16 共4個數. 步長是2.
            print(i, end="* ")
        str1 = "123456"
        str2 = [i for i in str1]  # >>>['1', '2', '3', '4', '5', '6']
        str2 = [int(i) for i in str1]  # >>>[1, 2, 3, 4, 5, 6]
        print(str2)

def 運算符():
    """
    运算符	描述			                实例
    %	    取模 - 返回除法的余数	        b % a 输出结果 1
    **	    幂 - 返回 x 的 y 次幂	        a ** b 为 10 的 21 次方
    //	    取整除 - 返回商的整数部分	    9//2 输出结果 4 , 9.0//2.0 输出结果 4.0
    =	    简单的赋值运算符		        c = a + b 将 a + b 的运算结果赋值为 c
    +=	    加法赋值运算符		            c += a 等效于 c = c + a
    -=	    减法赋值运算符		            c -= a 等效于 c = c - a
    *=	    乘法赋值运算符		            c *= a 等效于 c = c * a
    /=	    除法赋值运算符		            c /= a 等效于 c = c / a
    %=	    取模赋值运算符		            c %= a 等效于 c = c % a
    **=	    幂赋值运算符		            c **= a 等效于 c = c ** a
    //=	    取整除赋值运算符		        c //= a 等效于 c = c // a
    and	    x and y			            布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。	(a and b) 返回 20。
    or	    x or y			            布尔"或" - 如果 x 是 True，它返回 x的值，否则它返回 y 的计算值。		(a or b) 返回 10。
    not	    not x			            布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	not(a and b) 返回 False
    in	    序列找到True, 否则False	    x 在 y 序列中 , 如果 x 在 y 序列中返回 True。
    not in	序列找不到True, 否则False	    x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。

    """

def 字符串():
    """
    '\'作为转义字符
    字符串的截取的语法格式如下：变量 [头下标: 尾下标: 步长]     (注意不包含尾下标)
    自然字符串， 通过在字符串前加 r 或 R。 如 r"this is a line with \n" 则\n会显示，并不是换行。
    Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
    """
    str1 = 'W3Cschool'
    print(str1)  # 输出字符串  >>>W3Cschool
    print(str1[0:-1])  # 输出第一个到倒数第二个的所有字符  >>>W3Cschoo
    print(str1[0])  # 输出字符串第一个字符   >>>W
    print(str1[2:5])  # 输出从第三个开始到第五个的字符     >>>Csc
    print(str1[2:])  # 输出从第三个开始后的所有字符    >>>Cschool
    print(str1[1:5:2])  # 输出从第二个开始到第五个且每隔两个的字符   >>>3s
    print(str1 * 2)  # 输出字符串两次
    print(str1 + '你好')  # 连接字符串

def 函数():
    """
    函数是封装好的，可重复使用的，用来实现单一，或相关联功能的代码段。 函数能提高程序的模块性，和代码的重复利用率。
    如何使用字符串调用函数/方法？
    可以把函數當對象賦值

    """

    var = 1   #全局變最

    def fun1():
        var = 2  #局部變量
        print('f1')
        print("var:",var)

    def fun2(var1):
        print(var1)

    def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'): # 第一個參數在調用時必須, 因為沒有默認值.
        print("-- This parrot wouldn't", action, end=' ')
        print("if you put", voltage, "volts through it.")
        print("-- Lovely plumage, the", type)
        print("-- It's", state, "!")
        return voltage

    class Foo:

        def do_foo(self):
            print("Do Foo")

        @staticmethod   # 将方法转换为静态方法, 静态方法不会接收隐式的第一个参数。
        def do_bar():
            print("Do Bar")

    # 直接調用

    fun1() #局部變量, >>var: 2  因為變量在函數內部.
    print("var:", var)  #全局變最  >>var: 1    因為局部變量在函數結束後就會釋放.

    # 函數參數傳遞方式
    parrot(1000)    # 1000 給了變量voltage, 其它的用參數默認值. 及默認位置.
    parrot(100, action="test")  # 100 給了變量voltage, test 給了變量action
    parrot(voltage=1000000, action='VOOOOOM')  # 指字典參數傳遞
    parrot('a million', 'bereft of life', 'jump')  # 順序傳遞
    returnvar = parrot(500)  #有返回值
    print(returnvar)

    # 用字典調用
    tel = {'Test1': fun1, 'Test2': fun2}
    tel["Test2"](5)

    # 用內置函數 getattr() 調用
    getattr(test1, "funb")()
    f1 = getattr(Foo, 'do_foo')
    f2 = getattr(Foo, 'do_bar')

    f1('self') # 如果不用@staticmethod,  調用就要加上第一個參數"self".
    f2()    # 加上@staticmethod,  調用不需要第一個參數"self".


    def arithmetic_mean(*args): #可變參數列表
        if len(args) == 0:
            return 0
        else:
            sum1 = 0
            for x in args:
                sum1 += x
            return sum1/len(args)


    print(arithmetic_mean(45,32,89,78))
    print(arithmetic_mean(8989.8,78787.78,3453,78778.73))
    print(arithmetic_mean(45,32))
    print(arithmetic_mean(45))
    print(arithmetic_mean())

    def fun3(**val):        #兩個** 可變參數, 即用字典傳遞. 注意函數調用時要指定key, value
        for v in val.items():
            print(v)
        for k,v in val.items():
            print(k,v)

    fun3(var1="a", var2="b", var3=3)

    def fun4():
        print("b")
        return "a"
    test4 = fun4 # 把函數當對象賦值
    test4()     #輪出b, 不是返回值.

    test4a=fun4()   # 把函數當函數調用,test4a 就是返回值.
    print(test4a)


    # 函數結束

def 列表():
    """
    List列表可以放任意数量的python对象，可以是字符串，字符，整数，浮点等等都可以，而且创建，添加，删除也很方便.
    列表使用方括号[]
    """
    List1 = ['apple', 100, 0.01, 'banana', 'A', 'B', 'C']
    List2 = [0, 1, 2, 3, 4, 5, 6, 7]
    List3 = [100, 200, ['aaa', 'bbb', 'ccc']]
    List4 = [100, 200, 50, 20, 35]
    List5 = [100, 200, 50, 20, 35, 200, 50, 200]
    print(List1[0], List1[-1], List1[-2])       #>>apple C B  通過下標訪問, 注意, 0 是第一位, -1 是最後一位, -2 是最後第二位.
    print(List4.index(50))  # 查找列表中某一个元素的索引  >>>2
    print(List2[4:6])    # 注意輸出的是第4位, 第五位下標的數據 [4, 5], "6" 是不輸出的.
    print(List3[2])     # 列表支持嵌套，就是列表里面可以套列表，甚至套字典，元组等. 輸出['aaa', 'bbb', 'ccc']
    print(List3[2][1])  # 列表嵌套: 輸出 bbb
    List1[1] = "Pear"   # # 列表通過下標修改內容:  輸出['apple', 'Pear', 0.01, 'banana', 'A', 'B', 'C']
    print(List1)
    List1.append("Test")    # 列表放在後面:  輸出['apple', 'Pear', 0.01, 'banana', 'A', 'B', 'C', 'Test']
    print(List1)
    List1.insert(1, "在第1位插入")    # 列表插入: ['apple', '在第1位插入', 'Pear', 0.01, 'banana', 'A', 'B', 'C', 'Test']
    print(List1)
    del List1[1]    # 列表刪除, 刪除第1位內容, 輸出 ['apple', 'Pear', 0.01, 'banana', 'A', 'B', 'C', 'Test']
    print(List1)
    List1.remove("Pear")    # 如果不知道位置, 或者只知道內容或對象, 用remove. 輸出['apple', 0.01, 'banana', 'A', 'B', 'C', 'Test']
    print(List1)
    List1.pop(5)    # 刪除第5位內容: 輸出['apple', 0.01, 'banana', 'A', 'B', 'Test']
    print(List1)
    List1.pop()     # 刪除最後一位: 輸出['apple', 0.01, 'banana', 'A', 'B', 'Test']
    print(List1)
    print(List2*2)   # 列表乘 [0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3, 4, 5, 6, 7]
    print(List2 + List3)    # 列表加[0, 1, 2, 3, 4, 5, 6, 7, 100, 200, ['aaa', 'bbb', 'ccc']]
    List4.sort(reverse=True)  # 降序排列  >>>[200, 100, 50, 35, 20]
    print(List4[0], len(List4), max(List4), min(List4))     # 降序後直接修改了列表下標位置. >>>200 5 200 20
    List4.extend(List3)  # extend是直接修改了列表: >>>[200, 100, 50, 35, 20, 100, 200, ['aaa', 'bbb', 'ccc']]
    print(List5.count(200)) # 统计某个元组在列表里面的次数 >>>3


    #列表結束

def 元組():
    """
    元组（tuple，简写为tup）与列表类似，不同之处在于元组的元素不能修改。
    元组使用小括号()，列表使用方括号[]
    """
    tup1 = ('Google', 'W3CSchool', 1997, 2020)
    tup2 = (1, 2, 3, 4, 5)
    tup3 = "a", "b", "c", "d"  # 不需括号也可以
    tup4 = ()   # 创建空元组
    tup5 = (50,)    # 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当做运算符使用。
    print("tup1[0]: ", tup1[0])
    print("tup2[1:3]: ", tup2[1:3]) # >> tup2[1:3]:  (2, 3) 注意[1:3]表示在第1位, 截到第2位. 是不包含第3位的.
    tup_add=tup1+tup2   #元组之间可以使用 + 号和 * 号进行运算
    print(tup_add)
    del tup4    # 元组中的元素值是不允许删除的，但可以使用del语句来删除整个元组
    print(tup1[1:], tup2[:3])  #1. 从第二个开始后的所有元素, 2. 從第一個開始到第3個元素
    list1 = ['Google', 'Taobao', 'W3CSchool', 'Baidu']
    tuple1 = tuple(list1)   #将列表转换为元组。
    print(tuple1)
    print(id(list1)) # 查看内存地址

    # 元組結束

def 字典():
    """
    字典（dictionary ，简写为dict）是另一种可变容器模型，且可存储任意类型对象。
    字典的每个键值 (key=>value) 对用冒号 (:) 分割，每个对之间用逗号 (,) 分割，整个字典包括在花括号 {} 中
    d = {key1 : value1, key2 : value2 }
    键必须是唯一的，但值则不必。
    值可以取任何数据类型，但键必须是不可变的(只能一種數據類型)，如字符串，数字或元组。
    radiansdict.items()	以列表返回可遍历的(键, 值) 元组数组
    radiansdict.keys()	以列表返回一个字典所有的键
    radiansdict.values()	以列表返回字典中的所有值
    """
    dict1 = {'match': 94, 'englist': 100, 'china': 100, 'name': 'xu'}
    print(dict1["name"], dict1['englist'], dict1.get("englist"))  # 用健訪問

    dict1["match"]=90   #用健修改
    dict1["Test"] = "添加"  # 用健修改
    print(dict1)
    del dict1["name"]  # 删除键 "Name'
    #dict1.clear()  # 清空字典
    print(dict1)
    #del dict1  # 删除字典
    dict2 = {'Name': 'W3CSchool', 'Age': 7, 'Name': '编程狮'}     #不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：
    dict3=dict2.copy()  #可以Copy, clear
    print(dict3)    # >>>{'Name': '编程狮', 'Age': 7}
    for k,v in dict1.items():       #遍歷字典, 注意變量k,v,  也可以一個變量.
        print(k,v)
    print(dict1.keys()) # 以列表返回一个字典所有的键
    print(dict1.values()) # 以列表返回一个字典所有的值
    dict1.setdefault("test1")
    print(dict1)    # >>>{'match': 90, 'englist': 100, 'china': 100, 'Test': '添加', 'test1': None}
    print(dict1["china"])    # >>>100
    dict1["test2"]="添加值"    # 添加字典值>>{'match': 90, 'englist': 100, 'china': 100, 'Test': '添加', 'test1': None, 'test2': '添加值'}
    print(dict1)
    dict1.update({"test1":90, "test2": 80}) #更新字典內容, 注意有大括號. >>{'match': 90, 'englist': 100, 'china': 100, 'Test': '添加', 'test1': 90, 'test2': 80}
    print(dict1)
    # 字典結束

def 集合():
    """
    集合（set）是一个无序的不重复元素序列. 因此在每次运行的时候集合的运行结果的内容都是相同的
    集合用大括號{} 或set 創建.  创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
    parame = {value01,value02,...}
    或者
    set(value)
    """
    basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    print(basket)  # 去自動去重複, 輸出內容每次有可能會不同. 無序的.
    print('orange' in basket)   # 判断元素是否在集合内
    aa = {"abcd"}
    bb = {"abcefg"}
    a = set("abc")
    b = set("abcdef")

    print(b - a)
    print(a | b)
    print(a & b)
    print(a ^ b)
    basket.pop()    # 随机删除集合中的一个元素
    basket.remove("apple")
    basket.add("test")

    # 集合結束

def 條件控制和循環():
    """
    if 语句語法:
    if condition_1:
        statement_block_1
    elif condition_2:
        statement_block_2
    else:
        statement_block_3

    condition(條件) 可以用: >, >=, <, <=, ==, !=, and, or, not, is, is not, not in
    每个条件后面要使用冒号（:），表示接下来是满足条件后要执行的语句块

    while 循环語法
    while 判断条件：
        statements
    else
        statements

    for 语句語法:  for 循环可以遍历任何序列的项目，如一个列表或者一个字符串
    for <variable> in <sequence>:
        <statements>
    else:
        <statements>

    break 语句用于跳出最近的 for 或 while 循环
    continue 語句話继续执行循环的下一次迭代
    else while 循环还是 for 循环，其后都可以紧跟着一个 else 代码块，它的作用是当循环条件为 False 跳出循环时，程序会最先执行 else 代码块中的代码.
    怎麼才會有實際作用? 當用了break 跳出循环裏, 不會執行else, 正常循环是會執行else的.
    rang() 通常會用在for 循环裏.
    """
    list1=["Test1", "Test2", 1,5,9]
    if 1 in list1:
        print("Yes")
    else:
        print("no")

    edibles = ["ham", "spam","eggs","nuts"]
    for food in edibles:
        if food == "spam":
            print("No more spam please!")
            break
        print("Great, delicious " + food)
    else:
        print("I am so glad: No spam!")    #因為break 中斷了循環, 沒有執行else 語句塊
    print("Finally, I finished stuffing myself")

    # 在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来
    knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    for k, v in knights.items():
        print(k, v)

    # 在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到：
    for i, v in enumerate(['tic', 'tac', 'toe']):
        print(i, v)

    # 同时遍历两个或更多的序列，可以使用zip() 组合：
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    for q, a in zip(questions, answers):
        print('What is your {0}?  It is {1}.'.format(q, a))
        print(q,a)

    # 要反向遍历一个序列，首先指定这个序列，然后调用 reversesd() 函数：
    for i in reversed(range(1, 10, 2)):
        print(i)
    # 要按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，并不修改原值：
    basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    for f in sorted(basket):
        print(f)
    for f in sorted(set(basket)):
        print(f)    #set 返回集合, 集合是不能重複的, 所以就去重複了.



def 迭代器与生成器():
    """
    迭代器是一个可以记住遍历的位置的对象, 是访问集合元素的一种方式. 迭代器只能往前不会后退
    迭代器有两个基本的方法：iter() 創建 和 next() 迭代器下一個元素。
    字符串，列表或元组对象都可用于创建迭代器
    yield 的函数被称为生成器, 生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
    在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值。并在下一次执行 next() 方法时从当前位置继续运行。
    """
    import sys  # 引入 sys 模块

    list1 = [1, 2, 3, 4]
    it = iter(list1)  # 创建迭代器对象
    for x in it:    # 迭代器对象可以使用常规 for 语句进行遍历：
        print(x, end=" ")

    list1=[1,2,3,4]
    it = iter(list1)    # 创建迭代器对象
    while True:
        try:
            print(next(it))     # 也可以使用 next() 函数
        except StopIteration:
                break
                # sys.exit()


    def fun1():
        a=["test1", "test2", "test3"]
        for i in a:
            yield i
            print(i)
    f=fun1()
    '''
    for j in f:
        print(j)
    '''
    print(next(f))  # 輸出test1
    print(next(f))  # >>>開始在print(i)運行(yield i 下一個),  即輸出test1, 再test2.
    print(next(f))  # >>>開始在print(i)運行(yield i 下一個),  即輸出test2, 再test3.


# 運行
# 函数()
# 列表()
# 元組()
# 字典()
# 集合()
# 條件控制和循環()
# 字符串()
# 迭代器与生成器()
條件控制和循環()


