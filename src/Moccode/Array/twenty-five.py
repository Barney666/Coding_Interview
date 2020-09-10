'''
题目描述:
比亚莱钦斯克国正在进行选举，有 n 名候选人。这个国家由 m 个城市组成。我们知道每个城市有多少人投票给每个候选人。这个国家的选举制度很不寻常。
在选举的第一阶段，每一个城市的选票都是计票的：获得票数最多的将成为候选人，如果几个候选人获得了最多票数，那么胜者是 index 最小的那位
在第二阶段的选举中，同第一阶段类似：选举的获胜者是在最多城市中获胜的候选者，而在那些获得最大城市数量的候选人中，胜者是 index 最小的那位
请确定谁将赢得选举。

输入描述:
第一行为候选人的人数 n 和城市数 m (1 ≤ n, m ≤ 100)
接下来 m 行，每行为 n 个数表示这 n 个候选者的票数 aj (0 ≤ aj ≤ 10^9)

输出描述:
输出一个数表示获得选举的人的 index（从 1 开始）
'''

n,m=map(int,input().split())
arr=[0]*n
for i in range(0,m):
    temp=list(map(int,input().split()))
    for j in range(0,n):
        arr[j]+=temp[j]
biggest=max(arr)
for item in arr:
    if item==biggest:
        print(arr.index(item)+1)
        break