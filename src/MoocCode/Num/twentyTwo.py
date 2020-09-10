'''
题目描述:
给定一个非空整数数组，找到使所有数组元素相等所需的最小移动数，其中每次移动可将选定的一个元素加1或减1。 您可以假设数组的长度最多为10000。
'''

arr=list(map(int,input().split(",")))
sum=0
for item in arr:
    sum+=item
average=sum/len(arr)


diff=sum
tempAverage=average
for item in arr:
    temp=abs(item-average)
    if temp<diff:
        diff=temp
        tempAverage=item
average=tempAverage


result=0
for item in arr:
    result+=abs(average-item)
print(result)