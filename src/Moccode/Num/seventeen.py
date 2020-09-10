'''
题目描述

给定一个正整数 n，你可以做如下操作：

1. 如果 n 是偶数，则用 n / 2替换 n。
2. 如果 n 是奇数，则可以用 n + 1或n - 1替换 n。
n 变为 1 所需的最小替换次数是多少？
'''
def change(num, time):
    if num==1:
        return time
    elif num%2==0:
        return change(num/2,time+1)
    else:
        return min( change(num+1,time+1) , change(num-1,time+1) )



if __name__ == '__main__':
    n=int(input())
    print(change(n,0))