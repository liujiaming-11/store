shop1=[
    ["古灵冷火",100000],
    ["南明离火",200000],
    ["搬山力士傀儡符",100],
    ["生生不息造化丹",100],
    ["郭德纲相声选",100],
    ["Ak30000",500],
    ["10000万吨当量核弹",9800],
    ["邪王真眼",10000000000000]
]
shop2=[["百年苦修",5],
    ["破镜丹",10],
    ["诛仙剑阵",50],
    ["应龙蛋",100],
    ["青鸾蛋",80],
    ["德玛西亚的大宝剑",2],
    ["小哥，苹果要不？",200]]


mycart = []
mycart1 = []

import random
print("==========天上地下啥都能买，特牛逼的神秘商店出现了==========")
print("道友，选择商城把：1：神秘神秘神神秘秘商城，2：神神秘秘积分商城")
ls = int(input("道友，带了多少灵石啊？："))
jf = int(input("道友，带了多少积分啊？："))
dzls5 = 0
while True:
    num = input("选择商城呗：")
    dzls = ls
    if num == "1":
        print("嘿嘿嘿，欢迎进入神秘黑——啊，不是，是神秘良心商店。")
        dz = random.randint(1,9)
        dz1 = random.randint(7, 10)
        dz2 = random.randint(8,10)
        print("恭喜获得",dz,"全场打折券*1")
        print("恭喜获得", dz1, "生生不息造化丹专属打折券*1")
        print("恭喜获得",dz2,"搬山力士傀儡符专属打折券*1")
        count = 0
        count1 = 0
        while True:
            for index, value in enumerate(shop1):
                print(index,"", value)
            num1=input("选择宝贝把！：")
            if num1.isdigit():
                num1 = int(num1)
                if num1 > len(shop1):
                    print("别激动，看好了选。")
                else :
                    if ls<shop1[num1][1]:
                        print("滚去搬砖攒灵石，别胡闹！")
                        break
                    if num1 == int(num1):
                        mycart.append(shop1[num1])
                        ls = ls - shop1[num1][1]
                        print("添加到乾坤袋成功！道友剩余灵石为：", ls)
                    elif num1 == 3 :
                        count = count +1
                    #     # mycart.append(shop1[num1])
                    #     # ls = ls - shop1[num1][1]
                    #     # print("添加到乾坤袋成功！道友剩余灵石为：", ls)
                    #     # dzls2 = (count*shop1[3][1])*(1-dz1*0.1)
                    elif num1 == 2:
                        count1 = count1+1
                    #     # mycart.append(shop1[num1])
                    #     # ls = ls - shop1[num1][1]
                    #     # print("添加到乾坤袋成功！道友剩余灵石为：", ls)
                    #     # dzls3 = (count1*shop1[2][1])*(1-dz2*0.1)
                    #     break

            elif num1 == "q" or num1 == "Q":
                print("不买拉？那下次再来八。")
                break
        for index1,value1 in mycart:
            ls1 = ls+(dzls-ls)*(dz*0.1)+(count*shop1[3][1])*(dz1*0.1)+(count1*shop1[2][1])*(dz2*0.1)
            count = 0
            count1 = 0
            print("此次购买宝贝有",index1,value1,"道友剩余灵石为",ls1)
            break
    if num == "2":
        print("欢迎来到神秘积分商店！")
        while True:
            for index2,value2 in enumerate(shop2):
                print(index2,"",value2)
                num2 = input("选择宝贝八！：")
                if num2.isdigit():
                    num2 = int(num2)
                    if num2>len(shop2):
                        print("别激动。")
                    elif jf <shop2[num2][1]:
                            print("积分不足，臭弟弟。")
                    else:
                        mycart1.append(shop2[num2])
                        jf = jf - shop2[num2][1]
                        print("添加乾坤袋成功！剩余积分为：",jf)
                elif num2 == "q" or num2 == "Q":
                    print("不买拉？那下次再来八。")
                    break
            for index3,value3 in mycart1:
                print("此次购买宝贝有",index3,value3)
            print("剩余积分还有：",jf)
    elif num !="2" or num != "3":
        print("就俩商店，你这脑子修个屁仙。")
        break