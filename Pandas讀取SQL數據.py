# import pandas as pd
# import pymssql as sql
#
#
# con = sql.connect(server='10.2.81.30', user='beginer', password='@fly314', database='HMPSQL01')
# # con = pymssql.connect(server='use-et-aiml-cloudforte-aiops- db.database.windows.net',user='login_username',password='login_password',database='database_name')
# cursor = con.cursor()
#
# query = "SELECT TOP (100) * FROM [HMPSQL01].[dbo].[V_finishedSize]"
# cursor.execute(query)
# df = pd.read_sql(query, con)
# con.close()
# df


import concurrent.futures
import pandas as pd
import sqlalchemy

# 创建数据库引擎
engine = sqlalchemy.create_engine('mssql+pymssql://HMP-RH\ITProg02:Huangxumin01@10.2.81.30/HMPSQL01')

# 定义每批次的大小
batch_size = 100000

# 计算总行数
total_rows = pd.read_sql_query("SELECT COUNT(*) FROM V_finishedSize", engine).iloc[0, 0]
print(total_rows)
for start in range(0, total_rows, batch_size):
    end = start + batch_size
    # query = f"SELECT * FROM V_finishedSize LIMIT {batch_size} OFFSET {start}"
    query = f"SELECT TOP (100000) * FROM V_finishedSize"
    df = pd.read_sql_query(query, engine)
    # 处理数据
    print(df)
