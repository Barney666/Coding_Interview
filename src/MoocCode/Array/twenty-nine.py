'''
题目描述

给定一个非负整数数组 A，返回一个数组，在该数组中， A 的所有偶数元素之后跟着所有奇数元素。

你可以返回满足此条件的任何数组作为答案。

输入描述

一个非负整数数组 A。
1 <= A.length <= 5000
0 <= A[i] <= 5000
输出描述

排好序的数组
'''

arr=eval(input())
odd=[]
even=[]
for item in arr:
    if item%2==0:
        even.append(item)
    else:
        odd.append(item)
print(even+odd)