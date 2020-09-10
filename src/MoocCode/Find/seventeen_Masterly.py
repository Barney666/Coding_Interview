'''
题目描述

给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。

为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。

例如:

输入:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

输出:
2

解释:
两个元组如下:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
'''
'''
HashMap存前两个数组能组成的数字及其组成的次数，再遍历后两个数组，查看HashMap中是否存在两数和的相反数，如果存在，则记录出现次数，累加即为结果。
'''
arr=[]
for i in range(4):
    arr.append(list(map(int,input().split(","))))
record=[]
for i in range(len(arr[0])):
    num1=arr[0][i]
    for j in range(len(arr[1])):
        num2=arr[1][j]
        sum=num1+num2
        # if sum not in record:     有重复的算两个 因此这不用
        record.append(sum)
result=0
for i in range(len(arr[2])):
    num1=arr[2][i]
    for j in range(len(arr[3])):
        num2=arr[3][j]
        sum=num1+num2
        for item in record:
            if item==-sum:
                result+=1
print(result)

