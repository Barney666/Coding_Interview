'''
题目描述:
给定一个未经排序的整数数组，找到最长且连续的的递增序列。

输入描述:
一个未经排序的整数数组
数组长度不会超过1000。

输出描述:
找到最长且连续的的递增序列
'''

list=eval(input())
result=0
temp=1
for i in range(0,len(list)-1):
    if list[i]<list[i+1]:
        temp+=1
    else:
        if temp>result:
            result=temp
print(result)