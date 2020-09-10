'''
题目描述:
给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第k小的元素。
请注意，它是排序后的第k小元素，而不是第k个元素。
'''
'''
思路非常简单：
1.找出二维矩阵中最小的数left，最大的数right，那么第k小的数必定在left~right之间
2.mid=(left+right) / 2；在二维矩阵中寻找小于等于mid的元素个数count
3.若这个count小于k，表明第k小的数在右半部分且不包含mid，即left=mid+1, right=right，又保证了第k小的数在left~right之间
4.若这个count大于k，表明第k小的数在左半部分且可能包含mid，即left=left, right=mid，又保证了第k小的数在left~right之间
5.因为每次循环中都保证了第k小的数在left~right之间，当left==right时，第k小的数即被找出，等于right！！！！！！！！！！

这个思路查找算法里的题用的很多了 9,11也很用这个方法的 这里用文字总结一下 [11都是小数所以没用floor]
[这题和第9题比较像 都是有重复数字的 所以temp==k也不能break 必须直到left>=right才行]
'''

n=eval(input())
matrix=[[None]*n for i in range(n)]
for i in range(n):
    matrix[i]=list(map(int,input().split(",")))
k=eval(input())
left=matrix[0][0]
right=matrix[n-1][n-1]
import math

while left<right:
    mid=math.floor((left+right)/2)   # 这是个数 不是索引   但mid不一定在matrix里啊
    temp=0
    for i in range(n):
        for j in range(n):
            num=matrix[i][j]
            if num<=mid:
                temp+=1
            elif j==0:
                break     # 若某行的第一个数字都比要mid大 那么这行及下面的行的数字都会比mid大了
    if temp<k:
        left=mid+1
    elif temp>=k:
        right=mid

print(right)