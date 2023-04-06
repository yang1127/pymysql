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

# 删除数据
sql = "delete from t_test where score < 90"
cursor.execute(sql)
conn.commit()

# 关闭游标
cursor.close()

# 关闭连接
conn.close()