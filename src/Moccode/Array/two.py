'''
题目描述:
学校有 n 个小组外出游玩，第 i 个小组有 si (1 ≤ si ≤ 4) 个人，同学们想要打出租，每辆车最多坐4个人，同个小组必须坐在同一辆车上
求最少需要多少辆车才能让同学们都坐上出租车

输入描述:
第一行为小组数 n (1 ≤ n ≤ 1e5)
第二行为 n 个数表示每个小组的人数 si (1 ≤ si ≤ 4)

输出描述:
输出一个整数表示至少需要的出租车数
'''


import math

num=input()   #5
input=input()    #1 2 4 3 3

list=input.split(" ")

result=0
for item in list:
    result+=int(item)

result=math.ceil(result/4)       # 直接加起来 除4 向上取整
# 但 3人组数量比1人组数量 每多出来4个 会出现一次错误 车的数量需要加1 不足4个不会出错

one=list.count("1")
three=list.count("3")
add=0
if three>=one+4:
    diff=three-one
    add=math.floor(diff/4)

print(result+add)


'''
1 1 1 1   //4辆车
2 2 2 2 2 2 2 2 2 2 2 2     //12个2    即6辆车
3 3 3 3 3 3 3 3 3 3
4 4 4 4 4 4 4 4 4 4 4 4 4 4    //14个（辆）
'''



