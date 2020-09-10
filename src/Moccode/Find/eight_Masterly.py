'''
题目描述:
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。
'''
'''
滑动窗口双指针
'''
s=eval(input())
nums=list(map(int,input().split(",")))
length=len(nums)

slow=0
fast=-1
result=length+1
sum=0
while slow<length:
    if sum<s:
        fast+=1
        if fast<length:
            sum+=nums[fast]
        else:
            break
    else:
        result=min(result,fast-slow+1)
        sum-=nums[slow]
        slow+=1
print(result if result!=length+1 else 0)

