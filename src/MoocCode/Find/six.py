'''
题目描述

给你一个整数数组 nums 和一个正整数 threshold  ，你需要选择一个正整数作为除数，然后将数组里每个数都除以它，并对除法结果求和。

请你找出能够使上述结果小于等于阈值 threshold 的除数中 最小 的那个。

每个数除以除数后都向上取整，比方说 7/3 = 3 ， 10/2 = 5 。

题目保证一定有解。
'''
import math

def check(begin,end):
    div=begin+int((end-begin)/2)
    sum=0
    for i in range(0,len(arr)):
        sum+=math.ceil(arr[i]/div)
    if begin!=end:
        if sum==threshold:
            return div
        elif sum>threshold:
            return check(div+1,end)
        elif sum<threshold:
            return min(div,check(begin,div-1))
    else:
        if sum<=threshold:
            return div
        elif sum>threshold:
            return 1000000


if __name__ == '__main__':
    arr=list(map(int,input().split(",")))
    threshold=eval(input())
    print(check(1,max(arr)))