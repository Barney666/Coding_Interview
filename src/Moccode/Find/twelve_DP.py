'''
题目描述：
给定一个无序的整数数组，找到其中最长上升子序列的长度。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
'''
'''
https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-by-leetcode-soluti/
'''
import math

def check():
    index=0
    record=[]
    maxLength=0
    while index<len(arr):
        temp=0
        for i in range(0,index):
            if arr[i]<arr[index]:
                temp=max(temp,record[i])   # !!!这个很容易直接用temp=1然后if里temp+=1就有问题
        record.append(temp+1)
        maxLength=max(maxLength,record[index])
        index+=1
    return maxLength

if __name__ == '__main__':
    arr=list(map(int,input().split(",")))
    print(check())