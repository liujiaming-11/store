# dict = {"k1":"v1","k2":"v2","k3":"v3"}
# #1、请循环遍历出所有的key
# keys = dict.keys()
# values = dict.values()
# for key in keys:
#     print(key)
# #2、请循环遍历出所有的value
# for value in values:
#     print(value)
# # 3、请在字典中增加一个键值对,"k4":"v4"
# dict["k4"] = "v4"
# print(dict)


# 小明，小刚去超市里购买水果
# 小明购买了苹果，草莓，香蕉，小刚购买了葡萄，橘子，樱桃，请从下面的描述的字典中，计算每个人花费的金额，并写入到money字段里。
# 以姓名做key，value仍然是字典
# Friuts = {
#         "苹果":12.3,
#         "草莓":4.5,
#         "香蕉":6.3,
#         "葡萄": 5.8,
#         "橘子":6.4,
#         "樱桃":15.8
# }
#
# info = {
#     '小明': {
#         'ts': {'苹果':4, '草莓':13, '香蕉':10},
#         'money':0
#     },
#     '小刚': {
#         'ts': {'葡萄':19, '橘子':12, '樱桃':30},
#         'money': 0
#     }
# }
# for key in info :   # key是字典中的人名
#     for key1 in info[key]['ts'] :   # key1是对应人名所购买的水果名
#         # for key2 in Friuts :    # key2是商城中的水果名
#             # if key1 == key2 :
#         if key1 in Friuts :
#             info[key]['money'] = info[key].get('money') + info[key]['ts'].get(key1) * Friuts.get(key1)
# print(info)

# 编写一个函数，传入一个列表，并统计每个数字出现的次数。
# list1 = [3,8,9,6,2,3,8,9,6,5]
# list2 = []
# iii = {}
# for i in list1:
#     if i not in list2:
#         list2.append(i)
# for i in list2:
#     count = 0
#     for p in list1:
#         if i == p:
#             count = count + 1
#     print(i,"出现",count,"次")

# list = [3,8,9,6,2,3,8,9,6,5]
# list2 = []
# iii = {}
# for i in list:
#     if i not in list2:
#         list2.append(i)
# for i in list2:
#     count = 0
#     for p in list:
#         if i == p:
#             count = count + 1
#     print(i,"出现",count,"次")
#     iii [i] = count
# print(iii)

students = [
    {'name':'张三','age':23,'score':88,'tel':'23423532','gender':'男'},
    {'name':'李四','age':26,'score':80,'tel':'12533453','gender':'女'},
    {'name':'王五','age':15,'score':58,'tel':'56453453','gender':'男'},
    {'name':'赵六','age':16,'score':57,'tel':'86786785','gender':'保密'},
    {'name':'小明','age':18,'score':98,'tel':'23434656','gender':'女'},
    {'name':'小红','age':23,'score':72,'tel':'67867868','gender':'女'},
]
s1 = []
ii = []
iii = {}
iiii = {}
i1 = []
# 1) 统计不及格学生的个数
count = 0
for i in students:
    if i["score"]<60:
        s1.append(i["name"])
        count = count +1
print("不及格的学生为：",count,"个")
# 2) 打印不及格学生的名字和对应的成绩
for i in students:
    if i["score"] < 60:
        ii.append(i["score"])
        iii[i["name"]] = i["score"]
print(iii)
# print(s1,ii)
# 3) 统计未成年学生的个数
for i in students:
    if i["age"]<18:
        iiii[i["name"]] = i["age"]
print(iiii)
# 打印手机尾号是8的学生的名字
for i in students:
    i["tel"] = int(i["tel"])
    i["tel"] = i["tel"]%10
    if i["tel"] == 8:
        print(i["name"])
# 5) 打印最高分和对应的学生的名字
# for i in students:
#     for j in students:
#         if i["score"]<j["score"]:
#             if j["score"] not in i1:
#                 i1.append(j["score"])
#                 # print(i1)
#                 for i in students:
#                     for j in students:
#                         if i["score"]==j["score"] and j["score"] not in i1:
#                             i1.append(i["score"])
#                             print(i1)
#
# 6) 将列表按学生成绩从大到小排序
# for i in range(0,len(students)) :   # 遍历数组
#     for j in range(i,len(students)) :   # 遍历i后面的所有元素
#         if students[i]["score"] < students[j]["score"] :      # 对两个数比较，大的往前放
#             a = students[i]
#             students[i] = students[j]
#             students[j] = a
# print(students)
# # 5) 打印最高分和对应的学生的名字
# print("最高分为：",students[0]["score"],"分。","是学生：",students[0]["name"])
#7) 删除性别保密的所有学生
for i in students:
    i2 = {}
    i2 = students[3]
    del i2["gender"]
    i2 = students[3]
    print(students)











