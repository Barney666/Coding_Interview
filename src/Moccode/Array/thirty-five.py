'''
题目描述

给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

你找到的子数组应是最短的，请输出它的长度。

输入描述

一个整数数组，输入的数组可能包含重复元素 ，所以升序的意思是<=。
输出描述

寻找到的连续的子数组。
'''
arr=eval(input())
start=0
end=0
startDone=False
endDone=False
for i in range(0,len(arr)):
    smallest=min(arr[i:])
    smallestIndex=arr.index(smallest)
    biggest=max(arr[:len(arr)-i])
    biggestIndex=arr.index(biggest)
    if startDone==False:
        if smallestIndex!=i:
            start=i
            startDone=True
    if endDone==False:
        if biggestIndex!=len(arr)-1-i:
            end=len(arr)-1-i
            endDone=True
print(end-start+1)





