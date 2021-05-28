
# # 打印星号
# z = 1
# while z <= 7:
#     j = 1
#     l = 7
#     while l >= z:
#         print(" ",end="")
#         l = l -1
#     while j <= z:
#         j = j + 1
#         print("*", end="")
#         print(" ",end="")
#     print()
#     z = z + 1


# 取数
# num = int(input("请输入数字："))
# while num!=0:
#     print(num % 10)
#     num = num // 10


# 列表列表

# a = ["北京" , "上海" , "广东", "武汉" , "南宁" , "台北" , "广州" , "南宁" , "成都" , "贵阳"]
# a[1] = "广东"
# a[2] = "上海"
# print(a)
# b=[36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
# zh=b[0]+b[1]+b[2]+b[3]+b[4]+b[5]+b[6]+b[7]
# print(zh)
# print(zh/8)

#5的倍数的和

# c = [1,5,21,30,15,9,30,24]
# num = 5
# i = 0
# u = 0
# while i < 8:
#     if c[i]%num==0:
#         print (c[i])
#         u=u+c[i]
#         print("和：",u)
#
#     i = i +1

# # 数据反转
# t= [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
#
# # t = list(reversed(t))
# # print(t)
#
# i = 0
# z = 8
# while i < 9:
#     t[i] = t[i]+z
#     z = z - 2
#     i= i +1
# print(t)


# list = [1 , 4 , 7 , 5 , 8 , 2 , 1 , 3 , 4 , 5 , 9 , 7 , 6 , 1 , 10]
# f = 0
# j = 0
# while f < 15:
#     count = 0
#     j = j + 1
#     while j <= 10:
#         if list[f] == j:
#             count = count + 1
#         print(list[f], count)


# 网上抄来的最后一题
# from collections import Counter
# list = [1 , 4 , 7 , 5 , 8 , 2 , 1 , 3 , 4 , 5 , 9 , 7 , 6 , 1 , 10]
# list = Counter(list)
# print(list)
















