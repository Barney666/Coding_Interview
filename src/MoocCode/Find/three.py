'''
题目描述

给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。
'''


def check(begin,end):
    index = begin+int((end - begin) / 2)

    if begin==end:
        if nums[index]==target:
            result.append(index)
    elif begin==end-1:
        if nums[begin]==target:
            result.append(begin)
        if nums[end]==target:
            result.append(end)
    else:
        if nums[index] < target:
            check(index+1,end)
        elif nums[index] > target:
            check(begin,index-1)
        elif nums[index]==target:

            check(begin,index-1)
            check(index,end)



if __name__ == '__main__':
    nums=list(map(int,input().split(",")))
    target=eval(input())
    result=[]
    check(0,len(nums)-1)
    if(len(result)==0):
        result=[-1,-1]
    elif len(result)==1:
        result.append(result[0])
    print(result)

