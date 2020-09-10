'''
题目描述

你打算利用空闲时间来做兼职工作赚些零花钱。

这里有 n 份兼职工作，每份工作预计从 startTime[i] 开始到 endTime[i] 结束，报酬为 profit[i]。

给你一份兼职工作表，包含开始时间 startTime，结束时间 endTime 和预计报酬 profit 三个数组，请你计算并返回可以获得的最大报酬。

注意，时间上出现重叠的 2 份工作不能同时进行。

如果你选择的工作在时间 X 结束，那么你可以立刻进行在时间 X 开始的下一份工作。

1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4

1 <= startTime[i] < endTime[i] <= 10^9

1 <= profit[i] <= 10^4

输入描述

三个数组分布在三行，开始时间 startTime，结束时间 endTime 和预计报酬 profit
输出描述

返回可以获得的最大报酬。
'''
'''
也是用DP 按startTime排序后 从前往后记录每一位的最大profit 这块用dp思想【max(前面的)+这次的】
'''
def exchange(index):
    arrList=[startArr,endArr,profitArr]
    for arr in arrList:
        temp=arr[index]
        arr[index]=arr[index+1]
        arr[index+1]=temp
if __name__ == '__main__':
    startArr=eval(input())
    endArr=eval(input())
    profitArr=eval(input())

    for i in range(len(startArr)-1):
        for j in range(len(startArr)-i-1):
            start1=startArr[j]
            start2=startArr[j+1]
            if start1>start2:
                exchange(j)

    record=[]
    for i in range(len(startArr)):
        start=startArr[i]
        profit=profitArr[i]
        for j in range(0,i):
            end=endArr[j]
            if end<=start and record[j]+profitArr[i]>profit:
                profit=record[j]+profitArr[i]
        record.append(profit)

    print(max(record))

















