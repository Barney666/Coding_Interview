'''
题目描述

给定的整数数组 A ，我们要将 A数组 中的每个元素移动到 B数组 或者 C数组中。（B数组和C数组在开始的时候都为空）

返回True ，当且仅当在我们的完成这样的移动后，可使得B数组的平均值和C数组的平均值相等，并且B数组和C数组都不为空。

示例:
输入:
1,2,3,4,5,6,7,8
输出: True
解释: 我们可以将数组分割为 [1,4,5,8] 和 [2,3,6,7], 他们的平均值都是4.5。
'''
'''
计算出A的平均数avg, 若B的元素总和为 i*avg  (0<i<=n/2) , (B和C必定有一方的元素个数大于等于另一方, 我们取B为元素个数较少的那一方)， 
那么B和C的平均数一定相等

于是问题转化为， 迭代i， 对A中元素回溯， 看看是否能够挑出i个元素， 使得元素之和为 i * avg
'''
def check():
    for i in range(1,int(size/2)+1):
        goal=i*averageB
        index=-1
        for k in range(0,size-1):
            if arr[k]<=goal/2 and goal/2<=arr[k+1]:    # 若两个数加起来是goal 这两个数必在goal/2的两侧
                index=k
                break
        for diff in range(0,min(index,size-index)):   # 看左右两边哪个小
            left=arr[index]
            right=arr[index+1]
            if left+right==goal:
                return True
    return False


if __name__ == '__main__':
    arr = list(map(int, input().split(",")))
    arr.sort()
    size = len(arr)
    average = 0
    for item in arr:
        average += item
    average /= size
    # B和C的要乘2
    averageB = average * 2
    print(check())

