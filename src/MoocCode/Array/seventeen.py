'''
题目描述:
给定一个整数数组 nums，返回区间和在 [lower, upper] 之间的个数，包含 lower 和 upper。
区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。

输入描述:
第一行一个整数数组。第二行和第三行各一个数，分别表示lower 和 upper。

输出描述:
输出区间和在 [lower, upper] 之间的个数。

测试样例:
样例1: 输入-输出-解释
[-2,5,-1]
-2
2

3

3个区间分别是: [0,0], [2,2], [0,2]，它们表示的和分别为: -2, -1, 2。
'''

list=eval(input())
lower=int(input())
upper=int(input())

result=0
for i in range(0,len(list)):
    temp=0
    for j in range(i,len(list)):
        temp+=list[j]
        if lower<=temp<=upper:
            result+=1
print(result)

