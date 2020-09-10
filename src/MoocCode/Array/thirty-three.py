'''
题目描述

ZS 正在一台疯狂的计算机上敲代码，当你没有在 c 秒内打出字符时，你之前所有输入的字符都会消失。更正式地说，你在 a 秒时输入了一个字符，在 b 秒时输入了下一个字符，若 b - a > c，你在 b 秒之前输入的字符都会消失。只有当 b - a ≤ c 时，你输入的内容会得到保留。

现在给你 ZS 输入每个字符的时间序列，请你得出当 ZS 输入最后一个字符后的那一刻，有多少字符在计算机屏幕上。

输入描述

输入第一行为时间序列的长度 n 和时间限制 c (1 ≤ n ≤ 100000, 1 ≤ c ≤ 10^9)
输入第二行为输入的时间序列 (1 ≤ t1 < t2 < ... < tn ≤ 10^9)
输出描述

输入一个数，表示在 tn 时刻有多少字符在屏幕上
'''

n,c=map(int,input().split())
arr=list(map(int,input().split()))

if c==0:
    print(0)
else:
    result=1
    for i in range(0,len(arr)-1):
        if arr[i+1]-arr[i] <= c:
            result+=1
        else:
            result=1
    print(result)