'''
题目描述:
给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
'''

arr=list(map(int,input().split(",")))
arr.sort()
lastIndex=len(arr)-1
print(arr[lastIndex]*arr[lastIndex-1]*arr[lastIndex-2])