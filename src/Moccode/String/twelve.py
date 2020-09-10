'''
题目描述

给定一个 24 小时制（小时:分钟）的时间列表，找出列表中任意两个时间的最小时间差并已分钟数表示。

输入描述

一个 24 小时制（小时:分钟）的时间列表
列表中时间数在 2~100 之间。
每个时间取值在 00:00~23:59 之间。
输出描述

列表中任意两个时间的最小时间差并已分钟数表示
'''

arr=eval(input())
record=[]

for i in range(0,len(arr)):
    temp=arr[i]
    arr[i]=int(temp.split(":")[0])*60+int(temp.split(":")[1])

arr.sort()

for i in range(0,len(arr)-1):
    for j in range(i+1,len(arr)):
        num1=arr[i]
        num2=arr[j]
        if num2-num1<=12*60:
            record.append(num2-num1)
        else:
            record.append(num1+24*60-num2)

print(min(record))



