'''
题目描述

给定一个二进制数（没有多余前导0），可以对这个二进制数执行两种操作：

1、交换相邻数位的数字； 2、用 1 代替 11（例如 110 变成 10）。

输出执行任意操作（或者不操作）后这些二进制数中最小的二进制数。

输入描述

第一行，一个数 n，表示这个二进制数的长度；

第二行，一个二进制数 s。
输出描述

执行任意操作后最小的二进制数；
'''

n=int(input())
arr=list(input())

arr.sort(reverse=True)

index=0
if arr.count("1")>1:
    for i in range(0,len(arr)-1):
        if arr[i]=="1" and arr[i+1]=="0":
            index=i

result="".join(arr[x] for x in range(index,len(arr)))
print(result)
