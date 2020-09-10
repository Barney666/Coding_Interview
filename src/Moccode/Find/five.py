'''
题目描述

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。
'''
def find():
    for i in range(0, len(arr)):
        if arr[i] == num:
            return i
        elif i==len(arr)-1:
            if arr[i]<num:
                return i+1
        elif i==0:
            if arr[i]>num:
                return 0
            elif arr[i]<num<arr[i+1]:
                return i+1
        elif arr[i]<num<arr[i+1]:
            return i+1

if __name__ == '__main__':
    arr=list(map(int,input().split(",")))
    num=eval(input())
    print(find())
