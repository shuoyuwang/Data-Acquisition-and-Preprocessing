# mysql2.py
import pymysql.cursors
# 连接数据库
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='bank',
    charset='utf8'
)
# 获取游标
cursor = connect.cursor()
# 如果表存在，则先删除
cursor.execute("DROP TABLE IF EXISTS student")
# 设定SQL语句
sql1 = """
select * from receipt  where purchase_amt=109000
"""
# 执行SQL语句
cursor.execute(sql1)
# 打印执行结果
rs=cursor.fetchall()
for r in rs:
    print(r)

sql2 = """
select * from trans_detail_ms  where payment_receipt_account_name=-109000
"""
cursor.execute(sql2)
# 打印执行结果
rs=cursor.fetchall()
for r in rs:
    print(r)

# 关闭数据库连接
connect.close()
