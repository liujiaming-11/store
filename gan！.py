
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
# for i in list:
#     count = 0
#     for p in list:
#         if i == p:
#             count = count + 1
#     print(i,"出现",count,"次")


list = [1 , 4 , 7 , 5 , 8 , 2 , 1 , 3 , 4 , 5 , 9 , 7 , 6 , 1 , 10]
list2 = []
for i in list:
    if i not in list2:
        list2.append(i)
for i in list2:
    count = 0
    for p in list:
        if i == p:
            count = count + 1
    print(i,"出现",count,"次")

#遍历表1，如果表1的数不在表2里，则把表一的数加进表2里。如果数在表2里，计数器等于0，表1的数和表2的循环对比，表2的数每在表1出现一次，计数器+1.
#打印列表2中每个角标，出现了count次。




















