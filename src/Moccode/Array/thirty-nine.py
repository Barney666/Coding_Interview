'''
题目描述

给定一个由N个正整数组成的数组A []。任务是找出受A [i] <= A [j]约束的j-i的最大值。

输入描述

第一行包含一个整数T，表示测试用例的总数。然后是T测试用例。每个测试用例的第一行包含一个整数N，它表示数组的大小。下一行包含N个以空格分隔的整数，表示数组的元素。

输出描述

在分开的行中打印索引i和j的最大差。
'''

t=int(input())
num=int(input())
arr=list(map(int,input().split()))
temp=[]
for i in range(0,len(arr)):
    left=arr[i]
    dis=0
    while True:
        if i==len(arr)-1-dis:
            temp.append(0)
            break
        right=arr[len(arr)-1-dis]
        if left<right:
            temp.append(len(arr)-1-dis-i)
            break
        else:
            dis+=1
print(max(temp))
