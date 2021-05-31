
#该死的报名学习班
语文 = ['小明','小张','小黄','小杨']
数学 = ['小黄','小李','小王','小杨','小周']
英语 = ['小杨','小张','小吴','小冯','小周']
list = []
list1 = []
list2 = []
list3 = []
# for i in 语文:
#     if i not in list:
#         list.append(i)
#         for i in 数学:
#             if i not in list:
#                 list.append(i)
#         for i in 英语:
#             if i not in list:
#                 list.append(i)
# # print("一共有",len(list),"人选修课程。")
# for i in list:
#     count = 0
#     for l in 语文:
#         if i == l:
#             count = count +1
#     for l in 数学:
#         if i == l:
#             count = count +1
#     for l in 英语:
#         if i == l:
#             count = count +1
#     if count == 1:
#         list1.append(i)
# print("选择一门学科的一共有",list1.__len__(),"人,分别是",list1)
# for i in 语文:
#     if i not in list2:
#         list2.append(i)
#         for i in 英语:
#             if i not in list2:
#                 list2.append(i)
# for i in list2:
#     count = 0
#     for l in 语文:
#         if i == l:
#             count = count +1
#     for l in 英语:
#         if i == l:
#             count = count +1
#     if count == 2:
#         list3.append(i)
# print("选择语文和英语的一共有",list3.__len__(),"人,分别是",list3)


#倒立打印乘法表



# i = 1
# while i<=9:
#     j = 9
#     while j>=i:
#         print(i,"x",j,"=",(j*i),"  ",end="")
#         j = j - 1
#     print()
#     i = i + 1



# i = 9
# while i>0:
#     j = 1
#     while j<=i:
#         print(j,"x",i,"=",(j*i),"  ",end="")
#         j = j + 1
#     print()
#     i = i - 1



# li = [1,3,2,6,5,4,8,7,9]
# for index, value in enumerate(li):
#     for index1, value1 in enumerate(li):
#         # a = value
#         if value > value1:
#             li[index],li[index1]=li[index1],li[index]
#             value1 = a
# print(li)
# for  i  in range(len(li)):
#     for j in range(i,len(li)):
#         if li[i] > li[j]:
#             li[i],li[j] = li[j],li[i]
# print(li)



















