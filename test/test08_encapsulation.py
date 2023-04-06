# -*-coding:utf-8-*-
# 导包
import pymysql


# 创建工具类
class DBUtil():
    # 初始化
    __conn = None
    __cursor = None


    # 创建连接
    @classmethod
    def __get_conn(cls):
        # 没有连接对象，创建连接对象
        if cls.__conn is None:
            cls.__conn = pymysql.connect(
                host="127.0.0.1",
                port=3306,
                user="root",
                password="yyy1536520643",
                database="books",
                charset="utf8"
        )
        return cls.__conn


    # 获取游标
    @classmethod
    def __get_cursor(cls):
        # 没有游标，创建游标
        if cls.__cursor is None:
            cls.__cursor = cls.__get_conn().cursor()
        return cls.__cursor


    # 执行sql
    @classmethod
    def exe_sql(cls, sql):
        try:
            # 获取游标对象
            cursor = cls.__get_cursor()
            # 调用游标对象的execute方法，执行sql
            cursor.execute(sql)
            # 如果是查询 -- 判断第一个单词是否为"select"
            if sql.split()[0].lower() == "select":
                # 返回所有数据
                return cursor.fetchall()
            else:
                # 提交事务
                cls.__conn.commit()
                # 返回受影响的行数
                return cursor.rowcount
        except Exception as e:
            # 事务回滚
            cls.__conn.rollback()
            # 打印异常信息
            print(e)
        finally:
            # 关闭游标
            cls.__close_cursor()
            # 关闭连接
            cls.__close_conn()


    # 关闭游标
    @classmethod
    def __close_cursor(cls):
        # 游标存在，关闭、置初始值None
        if cls.__cursor:
            cls.__cursor.close()
            cls.__cursor = None


    # 关闭连接
    @classmethod
    def __close_conn(cls):
        # 连接没有关闭，关闭、置初始值None
        if cls.__conn:
            cls.__conn.close()
            cls.__conn = None