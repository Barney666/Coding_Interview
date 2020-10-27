'''
题目描述:
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

示例 1:
输入: 3,0,1
输出: 2

示例 2:
输入: 9,6,4,2,3,5,7,0,1
输出: 8
说明:
你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?
'''

arr=list(map(int,input().split(",")))
sum=0
for item in arr:
    sum+=item
n=len(arr)
print( int( (1+n)*n/2 - sum ))
'''
遍历一遍 把所有数相加 再用等差求出本来应该是多少 一减就是少的那个
'''