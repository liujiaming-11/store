id1 = 1
name1 = "羽绒服"
price1 = 253.6
num1 = 500
everyday1 = 10

id2 = 2
name2 = "牛仔裤"
price2 = 86.3
num2 = 600
everyday2 = 60

id3 = 3
name3 = "风衣"
price3 = 96.8
num3 = 335
everyday3 = 43

id4 = 4
name4 = "皮草"
price4 = 135.9
num4 = 855
everyday4 = 63

id5 = 5
name5 = "T恤"
price5 = 65.8
num5 = 632
everyday5 = 63

id6 = 6
name6 = "衬衫"
price6 = 49.3
num6 = 562
everyday6 = 120

id7 = 7
name7 = "牛仔裤"
price7 = 86.3
num7 = 600
everyday7 = 72

money = price1*num1+price2*num2+price3*num3+price4*num4+price5*num5+price6*num6+price7*num7

A = 56
B = 78






print("=======小刘黑心服装店圈钱记录表========")
print("日期      名称      价格/件     库存     销售量/日")
print(id1,"    ",name1,"    ",price1,"     ",num1,"    ",everyday1,)
print(id2,"    ",name2,"    ",price2,"     ",num2,"    ",everyday2,)
print(id3,"    ",name3,"    ",price3,"     ",num3,"    ",everyday3,)
print(id4,"    ",name4,"    ",price4,"     ",num4,"    ",everyday4,)
print(id5,"    ",name5,"    ",price5,"     ",num5,"    ",everyday5,)
print(id6,"    ",name6,"    ",price6,"     ",num6,"    ",everyday6,)
print(id7,"    ",name7,"    ",price7,"     ",num7,"    ",everyday7,)
print("总金额：￥",(price1*num1+price2*num2+price3*num3+price4*num4+price5*num5+price6*num6+price7*num7))
print("羽绒服金额占比:",( round(price1*num1/money*100,2)),"%")
print("羽绒服每件占比：",(round(price1/money*100,2)),"%")



print("A=",(A+B-A))
print("B=",(B+A-B))