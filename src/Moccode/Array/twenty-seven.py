'''
题目描述:
Polycarp 正在做编程训练，第一天做了 1 题，第二天做了 2 题，总之第 k 天他做了 k 题。
Polycarp 准备参加 n 个竞赛，第 i 个竞赛有 ai 道题。
每天他都选择一个没参加过的竞赛参加，在第 k 天做 k 道题，如果题目数量少于 k，则 Polycarp 不再进行训练。
如果 Polycarp 最优化选择竞赛，最多可以训练多少天？

输入描述:
第一行为竞赛的数量 n (1<=n<=2*10^5)
第二行包含 n 个整数 ai（1<=ai<=2*10^5) 表示第 i 个竞赛的题目数量

输出描述:
输出一个整数表示 Polycarp 最多可以训练的天数

测试样例:
样例1: 输入-输出
4
3 1 4 1

3

样例2: 输入-输出
3
1 1 1

1
'''

n=int(input())
ai=list(map(int,input().split()))

day=1
while len(ai)>0:
    smallest=min(ai)
    if smallest==day:
        ai.remove(smallest)
        day+=1
    elif smallest<day:
        ai.remove(smallest)
    else:
        ai.remove(smallest)
        day+=1
print(day-1)
















