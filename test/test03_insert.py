# -*-coding:utf-8-*-
# 导包
import pymysql

# 创建连接
conn = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="yyy1536520643",
    database="books",
    charset="utf8",
    autocommit=True
)

# 获取游标
cursor = conn.cursor()

# 插入数据
# 一条添加
sql1 = "insert into t_test(sno, sname, sex, age, score) values(2, 'YZQ', '女', 18, 88);"
cursor.execute(sql1)

# 批量添加
sql2 = '''
    insert into t_test(sname,sex,age,score) values(%s,%s,%s,%s)
'''
# 把数据以列表形式批量插入
add_data_list = [('王朝', 'man', 25, 94.6), ('马汉', 'man', 27, 91.1), ('张龙', 'man', 21, 88.1),
                 ('赵虎', 'man', 22, 97.1)]
cursor.executemany(sql2, add_data_list)

# 此时数据还没有提交到mysql中，需要再提交
# conn.commit()

# 关闭游标
cursor.close()

# 关闭连接
conn.close()