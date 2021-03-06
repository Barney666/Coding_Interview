'''
题目描述

给定一个包含非负数的数组和一个目标整数 k，编写一个函数来判断该数组是否含有连续的子数组，其大小至少为 2，总和为 k 的倍数，即总和为 n*k，其中 n 也是一个整数。

示例 1:

输入: 23,2,4,6,7; k = 6
输出: True
解释: [2,4] 是一个大小为 2 的子数组，并且和为 6。
示例 2:

输入: 23,2,6,4,7; k = 6
输出: True
解释: [23,2,6,4,7]是大小为 5 的子数组，并且和为 42。
'''


def check():
    for i in range(0,len(arr)-1):
        temp=arr[i]
        for j in range(1,len(arr)-i):
            temp+=arr[i+j]
            if temp%k==0:
                return True
    return False


if __name__ == '__main__':
    arr = list(map(int, input().split(",")))
    k = eval(input())
    print(check())