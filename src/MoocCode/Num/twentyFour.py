'''
题目描述:
对于一个 正整数，如果它和除了它自身以外的所有正因子之和相等，我们称它为“完美数”。
给定一个 整数 n， 如果他是完美数，返回 True，否则返回 False
'''
import math
n=int(input())
record=[]
for i in range(1,int(math.sqrt(n))+1):
    num=n/i
    if num==int(num):
        if i!=n:    # n是1 这abnormal用例
            record.append(i)
        if num!=n:
            record.append(num)
temp=0
for item in record:
    temp+=item
if temp==n:
    print(True)
else:
    print(False)
