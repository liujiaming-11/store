import pymysql
con = pymysql.connect(host="localhost",user="root",password="root",database="工商银行账户管理系统")
cursor = con.cursor()
def update(sql,param):
    cursor.execute(sql,param)
    con.commit()
def select(sql,param,mode="all",size=0):
    cursor.execute(sql,param)

    if mode == "all":
        return cursor.fetchall()
    elif mode == "one":
        return cursor.fetchone()
    elif mode == "many":
        return cursor.fetchmany(size)
def  relaseConnect():
    cursor.close()
    con.close()
from eee import update
sql = "insert into yh values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
param = ['张三', "111111mc", "230000", 233433, 'cn', 'cn', 'cn', 'cn', "中国工商银行昌平支行"]
sql1 = "select  * from yh"
param1 = []
data = select(sql1,param1,mode="many",size=3)
print(data)
