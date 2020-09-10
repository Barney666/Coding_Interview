'''
题目描述
给定一个正整数 N，找到并返回 N 的二进制表示中两个连续的 1 之间的最长距离。
如果没有两个连续的 1，返回 0 。
'''


n=bin(int(input()))
arr=[]
for i in range(0,len(n)):
    if n[i]=='1':
        arr.append(i)
if len(arr)==1:
    print(0)
else:
    temp=1
    for i in range(0,len(arr)-1):
        diff=arr[i+1]-arr[i]
        if diff > temp:
            temp=diff
    print(temp)





