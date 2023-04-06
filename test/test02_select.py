# 导包
import pymysql

# 创建连接
conn = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="yyy1536520643",
    database="books",
    charset="utf8"
)

# 获取游标
cursor = conn.cursor()

# 查询图书表的数据（图书ID，图书名称、阅读量）
sql1 = "select id, title, `read`, `comment` from t_book;"
cursor.execute(sql1)

# 1）获取查询结果的总数
print("获取的查询结果的总数：", cursor.rowcount)

# 2）获取查询结果的第一条数据 -- 游标在第一个位置
print("获取查询结果的第一条数据：", cursor.fetchone())

# 3）获取查询结果的多条数据
print("获取查询结果的多条数据：", cursor.fetchmany(2))

# 4）获取查询结果的全部数据 -- 游标已经游动到第二个位置，则fetchall()不展示第一个位置的数据
print("获取查询结果的全部数据：", cursor.fetchall())

# sql2 = "select id, title, `read`, `comment` from t_book;"
# cursor.execute(sql2)
# print("重新获取查询结果的全部数据：", cursor.fetchall())

# cursor.scroll(-1)
# print("获取查询结果的全部数据：", cursor.fetchall())
#
# cursor.rownumber = 0
# print("获取查询结果的全部数据：", cursor.fetchall())

# 关闭游标
cursor.close()

# 关闭连接
conn.close()