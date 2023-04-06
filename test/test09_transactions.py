# -*-coding:utf-8-*-
# 导包
import pymysql

# 初始化
conn = None
cursor = None

# 业务处理
try:
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

    # 执行sql
    sql = "insert into t_book(id, title, pub_date) values(4, '西游记', '1986- 01-01');"
    cursor.execute(sql)
    print(cursor.rowcount)
    print("-" * 200)

    # 主动抛出异常
    raise Exception("程序出错啦～～")

    # 新增一条英雄人物数据（name:孙悟空 gender:1 book_id:4）
    sql = "insert into t_hero(name,gender,book_id) values('孙悟空', 1, 4)"
    cursor.execute(sql)
    print(cursor.rowcount)

    # 提交事务
    conn.commit()

except Exception as e:
    # 回滚数据
    conn.rollback()
    # 打印异常信息
    print(e)

finally:
    # 关闭游标
    if cursor:
        cursor.close()
    # 关闭连接
    if conn:
        conn.close()