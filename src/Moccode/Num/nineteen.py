'''
题目描述

如果一个数列至少有三个元素，并且任意两个相邻元素之差相同，则称该数列为等差数列。

例如，以下数列为等差数列:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
以下数列不是等差数列。

1, 1, 2, 5, 7


数组 A 包含 N 个数，且索引从0开始。数组 A 的一个子数组划分为数组 (P, Q)，P 与 Q 是整数且满足 0<=P<Q<N 。

如果满足以下条件，则称子数组(P, Q)为等差数组：

元素 A[P], A[p + 1], ..., A[Q - 1], A[Q] 是等差的。并且 P + 1 < Q 。

函数要返回数组 A 中所有为等差数组的子数组个数。
'''

arr=list(map(int,input().split(",")))
fit=[]
temp=0
for i in range(0,len(arr)-2):
    if arr[i+1]-arr[i] == arr[i+2]-arr[i+1]:
        if temp==0:
            temp+=3   # 只记个数 最后能算出来
        else:
            temp+=1
    else:
        fit.append(temp)
        temp=0
fit.append(temp)    # 本身就是等差数列 没经历else
# 这里的等差数组必须连着 比较简单了
result=0
for item in fit:
    for num in range(1,item-1):   # 实际上是1到item-2
        result+=num
print(result)
