'''
题目描述

给定两个数组，编写一个函数来计算它们的交集。
'''

arr1=eval(input())
arr2=eval(input())
if len(arr1)<len(arr2):
    x=arr1
    y=arr2
else:
    x=arr2
    y=arr1
result=[]
for item in x:
    if item in y and item not in result:
        result.append(item)
result.sort()
print(result)

