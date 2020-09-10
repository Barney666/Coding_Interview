'''
题目描述:
给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。
说明：不要使用任何内置的库函数，如  sqrt。
'''


num=int(input())
for i in range(0,num):
    if i*i==num:
        print(True)
        break
    elif i*i>num:
        print(False)
        break