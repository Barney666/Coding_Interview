'''
题目描述
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
'''

n=int(input())
if n<=0:
    print(False)
else:
    while True:
        if n==1:
            print(True)
            break
        if n%2==0:
            n/=2
        else:
            print(False)
            break