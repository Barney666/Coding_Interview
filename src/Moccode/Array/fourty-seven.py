'''
题目描述

现在有一组 n 个数 a1, a2, ..., an，每一步你可以选择一个数加上或减去 1。现在想要让 a⋅a2⋅...⋅an=1 即这些数的乘积为 1，请问至少需要多少步？

输入描述

第一行为数组的长度 n (1≤n≤10^5)
第二行为这 n 个数 (−10^9≤ai≤10^9)
输出描述

输出一个数表示让这些数乘积为 1 的最少步数
'''

n=int(input())
arr=list(map(int,input().split()))
negative=[]
positive=[]
zero=[]
result=0
for x in arr:
    if x<0:
        negative.append(x)
    elif x>0:
        positive.append(x)
    else:
        zero.append(x)
if (len(negative)%2==0) or (len(negative)%2==1 and len(zero)!=0):
    for item in negative:
        result+=(-1-item)
    for item in positive:
        result+=(item-1)
    for item in zero:
        result+=1
else:
    negative.sort()
    for i in range(0,len(negative)):
        if i==len(negative)-1:
            result+=(1-negative[i])
        else:
            result+=(-1-negative[i])
    for item in positive:
        result+=(item-1)

print(result)