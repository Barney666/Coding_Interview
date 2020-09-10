'''
题目描述

您将得到一个大小为N的数组A（不同的元素）。找出两个元素之间的最大差异，其中较大的元素出现在A中较小的数字之后。

输入描述

输入的第一行包含一个整数T，表示测试用例的数量。随后是T个测试用例。每个测试用例包含两行输入。每个测试用例的第一行是N，N是数组的大小。每个测试用例的第二行包含N个由空格分隔的元素。

输出描述

对于每个测试用例，打印两个元素之间的最大差异。否则打印-1
'''

t=int(input())
for i in range(0,t):
    n=int(input())
    arr=list(map(int,input().split()))
    diff=0
    for i in range(0,n):
        for j in range(i+1,n):
            temp=arr[j]-arr[i]
            if temp>diff:
                diff=temp
    print(diff)