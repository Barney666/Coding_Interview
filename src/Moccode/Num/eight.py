'''
题目描述
统计所有小于非负整数 n 的质数的数量。
'''
n=int(input())
result=0

for i in range(2,n):
    temp=0
    for j in range(1,i+1):
        if i%j==0:
            temp+=1
    if temp==2:
        result+=1
print(result)