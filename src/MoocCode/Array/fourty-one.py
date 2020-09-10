'''
题目描述

马哈茂德有 n 条线段，其中第 i 条线段的长度为 ai。埃哈布向他提出挑战，要求他用 3 条直线段组成一个非退化三角形（其实就是普通三角形）。

马哈茂德只有确信自己能赢时才接受挑战，所以他让你告诉他是否应该接受挑战。

输入描述

第一行为线段数 n (3 ≤ n ≤ 10^5)
第二行包含 n 个整数 (1 ≤ ai ≤ 10^9) 表示线段的长度
输出描述

如果能够组成三角形，输出 YES 否则输出 NO
'''

n=int(input())
arr=list(map(int,input().split()))
arr.sort()
x1=arr[-3]
x2=arr[-2]
x3=arr[-1]

if x1+x2>x3 and x2+x3>x1 and x1+x3>x2 and x1-x2<x3 and x1-x3<x2 and x2-x1<x3 and x2-x3<x1 and x3-x1<x2 and x3-x2<x1:
    print("YES")
else:
    print("NO")