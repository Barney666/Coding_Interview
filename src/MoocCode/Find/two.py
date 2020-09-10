'''
题目描述

假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。
'''

def check(begin,end):
    index = begin+int((end - begin) / 2)

    if begin==end:
        if nums[index]==target:
            return index
        else:
            return -1
    if begin==end-1:
        if nums[begin]==target:
            return begin
        elif nums[end]==target:
            return end
        else:
            return -1
    else:
        if nums[index - 1] < nums[index] < nums[index + 1]:
            if nums[index] < target:
                return check(index+1,end)
            elif nums[index] > target:
                return check(begin,index-1)
            elif nums[index]==target:
                return index
            else:
                return -1
        elif nums[index + 1] < nums[index - 1] < nums[index]:
            if nums[index]!=target:
                return max(check(begin, index - 1), check(index + 1, end))
            else:
                return index
        else:      # nums[index]<nums[index+1]<nums[index-1]
            if nums[index]!=target:
                return max(check(begin, index - 1), check(index + 1, end))
            else:
                return index


if __name__ == '__main__':
    nums=list(map(int,input().split(",")))
    target=eval(input())
    print(check(0, len(nums) - 1))


