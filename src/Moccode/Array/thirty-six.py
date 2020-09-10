'''
题目描述

给定一个长度为 n 的整数序列，求这个序列当中最大的非完全平方数。

输入描述

第一行为序列的长度 n（1≤n≤1000）
第二行为 n 个整数表示这个序列（-10^6≤ai≤10^6），至少存在一个非完全平方数
输出描述

输出这个序列中最大的非完全平方数
'''


import math
n=int(input())
arr=list(map(int,input().split()))

arr.sort(reverse=True)

for item in arr:
    if item<0:
        print(item)
        break
    elif math.sqrt(item).is_integer()==False:
        print(item)
        break