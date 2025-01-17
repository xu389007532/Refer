"""
aaabbbcccdd
"""
import pandas as pd
import numpy as np



class Pandas():
    """Pandas 基本知识

        DataFrame.at : Access a single value for a row/column pair by label.
        DataFrame.iat : Access a single value for a row/column pair by integer position.
        DataFrame.loc : Access a group of rows and columns by label(s).
        DataFrame.iloc : Access a group of rows and columns by integer position(s).
        Series.at : Access a single value by label.
        Series.iat : Access a single value by integer position.
        Series.loc : Access a group of rows by label(s).
        Series.iloc : Access a group of rows by integer position(s).

    """

    def Seriser(self):
        '''
         一种一维标记的数组型对象, 能够保存任何数据类型. 包含了数据标签(索引)和数据
         索引(index), 数据(values)
         索引是自动创建, 也可以指定.

        '''
        s1 = pd.Series(["a", "b", "c"], index=["i1", "i2", "i3"])
        s1_index = s1.index
        # print(s1)
        # print(s1.values,s1.index.values)

        dict1 = {"a": "i1", "b": "i2", "c": "i3"}
        dict1 = {"a": 1, "b": 2, "c": 3, "d": 4}

        s2 = pd.Series(dict1)
        # s2 = pd.Series(dict1,index=["b","c","a","d"])
        print(s2)
        # print(s2.isnull())    #检查缺失值
        # print(s2.notnull())  # 检查是否不为空
        # print(s2.a,s2[1])
        # print(s2[[1,2]])    #选择第1,2 个数据
        # print(s2[1:2])  #索引切片
        # print(s2['b':'c'])  #标签切片
        # print(s2['b':])  #标签切片
        # print(s2[s2>1]) #Serier 数据大于1的数据
        # s3=s2>1     #将Seriers 大于是的改为True, 否则为False, 生成一个新的Seriers s3
        # print(s3)
        # print(s2*2)     #Seriers 的运算
        s2.name = "var_test"  # 对象名
        s2.index.name = "indexName"  # 对象索引名
        # print(s2.head(2))   #取前2个
        print(s2.tail(2))  # 取后2个

    def dataFram(self):
        pd.DataFrame.at
        pd.DataFrame.iat
        pd.DataFrame.loc
        pd.DataFrame.iloc
        pd.DataFrame.axes   #dataframe坐标轴x,y
        pd.DataFrame.dropna()
        pd.DataFrame.drop()
        pd.DataFrame.groupby
        # pd.pivot_tab
        # pd.DataFrame.fillna()
        # pd.DataFrame.isna()
        # pd.DataFrame.isin()
        # pd.DataFrame.duplicated()
        # pd.DataFrame.drop_duplicates
        # pd.DataFrame.reindex    #重新索引
        # pd.DataFrame.set_index()  # 设置某列为索引
        # pd.DataFrame.reset_index() #重新设置索引
        # pd.DataFrame.sort_values()
        # pd.DataFrame.rank() #排名
        # pd.DataFrame.apply()    #对每一行或每一列内容运行一个函数
        # pd.DataFrame.applymap()  # 对每个元素内容运行一个函数
        # pd.Series.map() #每Series 内容运行一个函数. 或字典对应

        """
        是一个表格型的数据结构, 它每列可以是不同类型的值, Data Frame 有行索引也有列索引. 它可以补看做是由Seriers 组成的字典(共用同一个索引).
        iloc 索引序号
        loc 索引名称
        切片 理解: [1:2:2] : [开始:结束:步长]
        DataFrame 重要属性:
            values: 所有元素值
            dtypes: 类型
            index: 行名
            columns: 列名
            T: 行列转换
            head: 前几条数据库. head(2) 是前2条
            tail: 后几条数据库. head(2) 是后2条
            shape: 行列数. shape[0]是先. shape[1]是列
        DataFrame 函数
            describe() 查看每列的统计汇总信息. DataFrame 类型
            count() 返回每列的非空值个数
            sum() , max, min
            
        """

        data="D:\\xu\\Python\\refer\\Pandas\\Pandas_data.xlsx"
        data2={"job num":["4096742-2","4096742-2","4096742-2","4096742-2","4096742-2"],
               "Lot":(1,2,3,4,5),
               "Component":["OE","OE","OE","OE","OE"],
               "Ord": np.arange(1,6)
               }
        job1 = pd.read_excel(data, sheet_name="job")
        job2=pd.DataFrame(data2)
        # print(job2)
        # print(job2.index,job2.columns )
        jv=job2.values #ndarrary 类型
        # print(job2.values)
        # print(job2.T)   #行列转换
        Ord=job2['Ord'] #返回Seriers
        # print(job2['Ord'])
        job2['Perso']=["Yes","No","No","Yes","no"]  #增加列
        del(job2['Perso'])  #删除列
        job2_s=job2["Lot"]

        # print(job2_s)
        des=job2.describe()
        # print(job2.describe())
        # print(job2_s[1])
        # print(job2.index)
        # print(job2)
        # print(job2.loc[2])
        iloc_1=job2.iloc[2]      #返回Serier
        test=iloc_1["job num"]
        # print(job2.iloc[2])
        # print(job2.loc[[2,4]])
        iloc_2=job2.iloc[[2, 4]]    #返回DataFrame
        # print(job2.loc[3,"Lot"])  #提取index是3的Lot 数据.  逗号左边是index, 右边是列名, 返回整数据.
        loc_1=job2.loc[[2, 4], ["Lot","Ord"]]
        # print(job2.loc[[2,4], "Lot"])  # 提取index是2,4的Lot 数据.  逗号左边是index, 右边是列名, 返回数据: 如果是多列, 返回DataFrame, 如果只有一列, 返回Seriers
        # print(job2.loc[(job2["Ord"]>2) & (job2["Lot"]>3)])  #条件查询 注意多条件双边要加括号
        # print(job2.iloc[[2,4]])
        job2.rename(columns={"Ord":"Ord1"},inplace=True)    #修改列名, inplace是否直接修改DataFrame
        index1=job2.index
        # print(type(index1)==pd.RangeIndex)      #类型检测
        # print(isinstance(job2.index,(pd.RangeIndex,int)))   #类型检测, 可以用元组
        job2.rename({0: 0.1}, inplace=True, axis=0)  # 修改行名, inplace是否直接修改DataFrame, axis=0 是行, 1 是列. 建议加上
        index2=job2.index
        # print(type(index2) == pd.RangeIndex)
        job2['Ord1']=job2["Lot"]+1  #整列数据修改
        job2["Component"]=["OE","RE","RC","OE",np.nan]
        # print(job2)
        job2.loc[job2["Component"]=="OE","Ord1"]=1      #查找Component=OE 的数据, 找到的数据, 把列名"Ord1"的内容改为1
        job2.loc[job2["Component"] == "OE", "Ord1"] = job2["Lot"]   #查找Component=OE 的数据, 找到的数据, 把列名"Ord1"的内容用"Lot"列代替
        #job2.drop(["Ord1"],axis=1,inplace=True) #删除列为"Ord1"
        #job2.drop(columns="Ord1", inplace=True) #删除列为"Ord1"
        # job2.drop([1.0], axis=0,inplace=True) #删除行
        #job2.drop(index=1.0, inplace=True) #删除行
        #job2.drop(job2[job2["Component"]=='OE'].index, inplace=True)    #条件删除行
        # job2.drop(job2[job2["Component"] == 'OE'].index[0], inplace=True)  # 条件删除第一行

        test=job2.info
        # print(job2)
        job3=job2.dropna()  #删除NaN 值, 详细可看此函数.
        # print(job3)
        test1=job3.axes
        # for name, group in job1.groupby("Lot"):
        #     print(group)
        # for (k1,k2), group in job1.groupby(["Package Code","Component"]):
        #     print(k1,k2)
        #     print(group)
        # print(job3.axes)
        dict1={"OE - Paper":"OE/RE/ME",
               "Reply Envelope":"OE/RE/ME",
               "OE - Special":"OE/RE/ME"}
        dict2={"TOTE0250":"a",
               "MGFT0001":"b"}
        # job1=job1.set_index("Ord")
        # print(job1)
        job1a=job1.groupby(dict2,axis=0)
        for k1, group in job1.groupby(dict2,axis=0):
            print(k1)
            print(group)

        print(job1a)

    def test(self):
        df = pd.DataFrame({'month': [12, 4, 7, 10],
        'year': ["2012", "2014", "2013", "2014"],
        'sale': [55, 40, 84, 31]})
        # df.set_index('month')
        print(df)
        df.apply(self.fun1)
        #
        # df.set_index(['year', 'month'])
        # print(df)

    def fun1(self,s1):
        if s1.name=="year":
            for s in s1:
                s1
        s1=s1+1
        print(s1)
        return s1






# Pandas.Seriser()
pd1=Pandas()
# pd1.dataFram()
pd1.test()
