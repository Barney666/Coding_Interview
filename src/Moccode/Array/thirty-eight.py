'''
题目描述

给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

输入描述

一个未排序的整数数组
输出描述

最长连续序列的长度
'''

arr=eval(input())
arr.sort()
result=1
temp=1
for i in range(0,len(arr)-1):
    if arr[i+1]-arr[i]==1:
        temp+=1
    else:
        if result<temp:
            result=temp
        temp=1
print(result)