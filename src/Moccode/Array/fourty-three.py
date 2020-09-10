'''
题目描述：
给定大小为N的数组arr []。任务是在整数数组中找到第一个重复元素，即出现多次且第一次出现的索引最小的元素。

输入描述：
第一行包含一个整数T，表示测试用例的总数。在每个测试案例中，第一行是数组N中元素的数量，其第二是其值。

输出描述：
在每行中打印第一个重复元素的索引，如果没有任何重复元素，则打印“ -1”（不带引号）。使用1开始的索引。
'''
t=int(input())
for i in range(0,t):
    n=int(input())
    arr=list(map(int,input().split()))
    for item in arr:
        if arr.count(item)>1:
            print(arr.index(item)+1)
            break
        else:
            if arr.index(item)==len(arr)-1:
                print("-1")