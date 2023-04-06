# -*-coding:utf-8-*-
# 导包
import pymysql
import random

# 创建连接
conn = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="yyy1536520643",
    database="books",
    charset="utf8",
    autocommit=False  # 默认为False
)

# 创建/获取游标
cursor = conn.cursor()

# 更新语句
sql = 'update t_test set score=%s where sno=%s'
try:
    # 将sno=2的学生成绩修改为80-100之间的随机数
    cursor.execute(sql, (random.randint(80, 100), 2))
    # 提交数据
    conn.commit()
    print('修改成功')
except:
    print('修改失败')
    # 回滚
    conn.rollback()
finally:
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
