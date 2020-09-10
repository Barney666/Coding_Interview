'''
题目描述

给出一个32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
'''

num=int(input())
result=""
if num >= 0:
    num=str(num)
    result="".join(num[i] for i in range(len(num)-1,-1,-1))
    result=result.strip("0")
else:
    num=str(num)[1:]
    result+="-"
    result+="".join(num[i] for i in range(len(num)-1,-1,-1))
    result=result.strip("0")

print(result)
