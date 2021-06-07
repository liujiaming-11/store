import pymysql

# con = pymysql.connect(host="localhost" , user="root" , password="" , database="销售数据库")
#
# cursor = con.cursor()
#
# sql = "insert into css values(%s,%s,%s,%s,%s)"
# param = ['30号', "风衣", 96.8, 335, 78]
# cursor.execute(sql , param)
#
# con.commit()
#
# cursor.close()
# con.close()
#


# con = pymysql.connect(host="localhost" , user="root" , password="" , database="人员表")
# cursor = con.cursor()
# sql = "insert into name values(%s,%s,%s,%s,%s)"
# param = ['张三', "admin", 23, "男", "沙河北大桥桥底下"]
# cursor.execute(sql , param)
# con.commit()
# cursor.close()
# con.close()

con = pymysql.connect(host="localhost" , user="root" , password="" , database="工商银行账户管理系统")
cursor = con.cursor()
sql = "insert into yh values(%s,%s,%s,%s,%s,%s,%s,%s,%s);"   # 严格区分中英文字符，每句sql指令以;号结尾
param = ['张三', "111111mc", "230000", 233433, 'cn', 'cn', 'cn', 'cn', "中国工商银行昌平支行"]
cursor.execute(sql, param)
con.commit()
cursor.close()
con.close()





