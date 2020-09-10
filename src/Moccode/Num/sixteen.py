'''
题目描述

给定一个长度为 n 的整数数组 A 。

假设 Bk 是数组 A 顺时针旋转 k 个位置后的数组，我们定义 A 的“旋转函数” F 为：

F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1]。

计算F(0), F(1), ..., F(n-1)中的最大值。

注意:
可以认为 n 的值小于 105。
'''

arr=list(map(int,input().split(",")))
size=len(arr)

f=[]
for k in range(0,size):
    num=0
    for i in range(0,size):
        num+=i*arr[-k+i]
    f.append(num)
print(max(f))