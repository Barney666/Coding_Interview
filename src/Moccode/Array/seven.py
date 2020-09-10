'''
题目描述:
给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是 nums[i] 右侧小于 nums[i] 的元素的数量。

输入描述:
初始整数数组

输出描述:
返回的新数组
'''

list=eval(input())
result=[]

for i in range(0,len(list)-1):
    left=list[i]
    num=0
    for j in range(1,len(list)-i):
        right=list[i+j]
        if right<left:
            num+=1
    result.append(num)
result.append(0)
print(result)