'''
题目描述:
给定一个未排序的整数数组，找出其中没有出现的最小的正整数。
'''
arr=eval(input())
arr.sort()
num=arr[0]
if num>1:
    print(1)
else:
    for i in range(1,len(arr)+2):
        if i not in arr:
            print(i)
            break