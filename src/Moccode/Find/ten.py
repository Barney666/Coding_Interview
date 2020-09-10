'''
题目描述

给定一个只包含小写字母的有序数组letters 和一个目标字母 target，寻找有序数组里面比目标字母大的最小字母。

数组里字母的顺序是循环的。举个例子，如果目标字母target = 'z' 并且有序数组为 letters = ['a', 'b']，则答案返回 'a'。
'''
import math
def check(begin,end):
    while begin<end:
        mid=math.floor((begin+end)/2)
        if arr[mid]<=target<arr[mid+1]:
            return arr[mid+1]
        else:
            if arr[mid]<target:
                begin=mid+1
            elif arr[mid]>target:
                end=mid
    return arr[0]
    # if end==-1:
    #     return arr[0]
    # elif begin==len(arr):
    #     return arr[0]


if __name__ == '__main__':
    arr=eval(input())
    target=input()
    print(check(0,len(arr)-1))
