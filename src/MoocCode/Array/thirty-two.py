'''
题目描述

小女孩谭雅在爬楼梯。谭雅每次爬楼梯时，她都会开始数从 1 到爬上楼梯的步数。她大声说出每一个数字。例如，如果她爬两个楼梯，第一个楼梯有三个台阶，第二个楼梯有四个台阶，她会念数字 1，2，3，1，2，3，4。

你得到了谭雅发音的所有数字，请问她爬了多少楼梯？同时，输出每个楼梯的台阶数。

输入描述

输入第一行为谭雅说出的数字个数 n (1≤n≤1000)
第二行为谭雅说出的 n 个数字 (1≤a≤1000)（假设谭雅每次都能正确说出自己爬的楼梯）
输出描述

第一行输出为一个整数表示谭雅爬的楼梯的个数 t
第二行输出 t 个数，表示每个楼梯的台阶数
'''

n=int(input())
arr=list(map(int,input().split()))
t=arr.count(1)
result=[]
for i in range(0,len(arr)-1):
    front=arr[i]
    behind=arr[i+1]
    if front==1 and behind==1:
        result.append(1)
    if front!=1 and behind==1:
        if i+1==len(arr)-1:
            result.append(front)
            result.append(1)
        else:
            result.append(front)
    elif i+1==len(arr)-1:
        result.append(behind)
print(t)
string="".join([str(x)+" " for x in result])
print(string.strip())

