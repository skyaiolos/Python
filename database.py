# coding=utf8
import sqlite3

# 把数据存储在数据库。
#     1. 创建数据库

# 链接。
conn = sqlite3.connect(r'db\course_db.db')
# 数据连接的游标。
c = conn.cursor()
# 关系型数据库知识。用游标执行。
sql = """
    CREATE TABLE Course
    (
      url TEXT,
      Title TEXT,
      Number INTEGER,
      Organization TEXT
    )
"""
c.execute(sql)
conn.commit()
conn.close()

if __name__ == '__main__':
    pass
