'''
题目描述

假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

注意数组中可能存在重复的元素。
'''

def check(begin,end):
    index = begin+int((end - begin) / 2)

    if begin==end-1 or begin==end:
        if nums[begin]<=nums[end]:
            if begin==0:
                return nums[begin]
            else:
                return 1000000
        else:
            if end==len(nums)-1:
                return nums[end]
            else:
                return 1000000
    else:
        if nums[index-1]<=nums[index]<=nums[index+1]:
            return min(check(begin,index-1),check(index+1,end))
        elif nums[index + 1] < nums[index - 1] <= nums[index]:
            return nums[index+1]
        elif nums[index]<nums[index+1]<=nums[index-1]:
            return nums[index]

if __name__ == '__main__':
    nums=list(map(int,input().split(",")))
    print(check(0, len(nums) - 1))