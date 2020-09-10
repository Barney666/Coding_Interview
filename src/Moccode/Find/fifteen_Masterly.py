'''
题目描述:
给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。

注意:
数组长度 n 满足以下条件:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
示例:

输入:
nums = [7,2,5,10,8]
m = 2

输出:
18

解释:
一共有四种方法将nums分割为2个子数组。
其中最好的方式是将其分为[7,2,5] 和 [10,8]，
因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。
'''
'''
解题思路：
1.本题的单调关系关系比较隐蔽，单调关系是：数组和的最大值越小，分组数越大。数组和的范围是可以确定的。
2.根据单调关系，将题目转换为：当子数组的和最大为maxSum时，至少需要分多少组-->能否在最多m组的限制范围内完成分割。
3.由于是非空非负整数数组，最小值可设为1；数组和的最大值设置为nums的总和+1，+1的作用是保证结果在最小值和最大值范围内。
4.canSplit中用到了贪心策略，在子数组中尽可能多的放置元素，直到放不下，另起一组。
5.如果当前值满足分割条件，记录当前值，利用二分法，缩小子数组总和。否则扩大子数组总和，直到找到最佳答案。
'''
def check(maxSum):
    tempSum=0
    count=0
    for num in nums:
        if num>maxSum:      # 如果单个数字大于maxSum，直接根本就无法分割出和小于maxSum的一组
            return False
        if (tempSum+num)>maxSum:   # 如果和超过了maxSum，另起一组
            count+=1
            tempSum=num
        else:     # 贪心策略，一组中放的数字尽可能多
            tempSum+=num
    return (count+1)<=maxCount    # 分割完成后 sum里还有一组

if __name__ == '__main__':
    import math
    nums=list(map(int,input().split(",")))
    maxCount=eval(input())
    left=1
    right=1
    for i in range(len(nums)):
        right+=nums[i]
    result=-1
    while left<right:
        mid=math.floor((left+right)/2)
        if check(mid):
            result=mid
            right=mid
        else:
            left=mid+1
    print(result)




























