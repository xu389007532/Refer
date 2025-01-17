# import Info_tkinter
import csv

# user=input("test").strip()
# print(user)
# Info_tkinter()

"""
1. open(file, mode='r', buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
file 是一个 path-like object，表示将要打开的文件的路径（绝对路径或者相对当前工作目录的路径），也可以是要封装文件对应的整数类型文件描述符。
mode 是可选的字符串，用于指定打开文件的模式。默认值是 'r'
    'r'：读(默认)
    'w'：写
    'x': 排它性创建，如果文件已存在则失败
    'a'：打开文件用于写入，如果文件存在则在末尾追加
    'b': 二进制模式
    'r+' == r+w（可读可写，文件若不存在就报错(IOError)）
    'w+' == w+r（可读可写，文件若不存在就创建）
    'a+' ==a+r（可追加可写，文件若不存在就创建）
    对应的，如果是二进制文件，就都加一个b就好啦：
    'rb'　　'wb'　　'ab'　　'rb+'　　'wb+'　　'ab+'
buffering 是一个可选的整数，用于设置缓冲策略
encoding 是用于解码或编码文件的编码的名称
newline 控制 universal newlines 模式如何生效（它仅适用于文本模式）。它可以是 None，''，'\n'，'\r' 和 '\r\n'

2.
 csv.reader(csvfile, dialect='excel', **fmtparams)
 dialect : csv.excel, csv.excel_tab,csv.Sniffer
 **fmtparams
    delimiter 分隔符用于分隔字段的单字符字符串。它默认为“，”
    doublequote  双引号 控制如何引用字段中出现的 quotechar 实例本身。当为 True 时，字符加倍。当为 False 时，escapechar 用作quotechar 
                 的前缀。它默认为 True。
                 在输出中，如果 doublequote 为 False 且未设置转义字符，则如果在字段中找到quotechar，则会引发错误。
    escapechar  转义符 如果quoting 设置为QUOTE_NONE 和quotechar 如果doublequote 为False，则作者用于转义分隔符的单字符字符串。
                在阅读时，转义字符会从以下字符中删除任何特殊含义。它默认为 None，即禁用转义
    lineterminator  行终结符 用于终止编写器生成的行的字符串。它默认为 '\r\n'。
    quotechar 一个单字符字符串，用于引用包含特殊字符（例如分隔符或引号字符）或包含换行符的字段。它默认为'"'。
    quoting 控制何时应由作者生成引号并由读者识别。它可以采用任何 QUOTE_* 常量（参见模块内容部分）并且默认为 QUOTE_MINIMAL
    skipinitialspace 当为 True 时，紧跟在分隔符之后的空格将被忽略。默认值为假。
    strict 如果为 True，则在错误的 CSV 输入上引发异常错误。默认值为假。          
    例如:
    csv.reader(csvfile, delimiter=' ', quotechar='|')
 3. csv.writer(csvfile, dialect='excel', **fmtparams)
    例如:
    csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)   
 4. csv.DictReader(f, fieldnames=None, restkey=None, restval=None, dialect='excel', *args, **kwds)
    fieldnames=None 讀全部字段內容, 如果要列出來， 要注意順序要一樣， 如果不一樣， 會更改字段名。 指定後, 後面取其他字段數據就取不到.
    例如：
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['first_name'], row['last_name'])
 5. csv.DictWriter(f, fieldnames, restval='', extrasaction='raise', dialect='excel', *args, **kwds)  注意 fieldnames 必須的.
    例如：
     with open('names.csv', 'w', newline='') as csvfile:
        fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
        writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
        writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})    
"""

'''
test = "C:/abc/itprog02"
test = "C:/"
test2 = "C:/Program Files"
# r=csv.reader(open("./SourceFile/JobNum List.csv"), dialect=csv.excel )
for i in r:
    print (i)
# w1=open("./SourceFile/JobNum List.csv","a+")
w=csv.writer(w1)
w.writerow("test")

for i in r:
    print (i)
'''

img = './SourceFile/ima.png'
# filename = "D:/xu/Python/refer/SourceFile/JobNum List.csv" # 絕對路徑
filename = "./SourceFile/JobNum List.csv"  # 相對路徑

with open(filename, mode='r', newline='') as csvfile:    #讀CSV newline=''.
    fieldnames = ['ProcessPartNum', 'ProcessERP_JobNum', 'ProcessERP_PartNum']

    # reader = csv.DictReader(csvfile,fieldnames=fieldnames)    # 指定fieldnames 輸出時會把第一列標題也輸出.
    reader = csv.DictReader(csvfile)                            # 不指定fieldnames, 輸出開始是從第二行數據行開始
    fieldnames = reader.fieldnames
    for row in reader:
        #print(row)     # 輸出字典 key, value
        #print(row['ProcessPartNum'], row['ProcessERP_JobNum'], row['ProcessERP_PartNum'])   # 輸出value
        for fn in fieldnames:   # 不用指定字段名全部輸出內容.
            print(row[fn])
print(fieldnames)
with open(filename, mode='a+', newline='') as csvfile:  # 讀CSV newline=''.
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)  # fieldnames 參數是必須的.
    #writer.writeheader()  #寫標題
    #writer.writerow({'ProcessPartNum': "test1", 'ProcessERP_PartNum': 'test2'})


