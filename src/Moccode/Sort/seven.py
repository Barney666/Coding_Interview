'''
题目描述

在 2016 年，佳媛姐姐喜欢上了数字序列。因而他经常研究关于序列的一些奇奇怪怪的问题，现在他在研究一个难题，需要你来帮助他。

这个难题是这样子的：给出一个1到n的全排列，现在对这个全排列序列进行m次局部排序，排序分为两种：

1.(0,l,r)表示将区间[l,r]的数字升序排序

2.(1,l,r)表示将区间[l,r]的数字降序排序

排序后询问第q位置上的数字。

输入描述

输入数据的第一行为两个整数 n和m。n表示序列的长度, m表示局部排序的次数(1≤n,m≤10^5)。
第二行为n个整数,表示1到n的一个全排列。
接下来输入m行，每一行有三个整数op,l,r, op 为0代表升序排序，op为1代表降序排序, l, r表示排序的区间。
最后输入一个整数q，q表示排序完之后询问的位置，1≤q≤n。
输出描述

输出数据仅有一行，一个整数，表示按照顺序将全部的部分排序结束后第q位置上的数字。
测试样例

样例1:输入-输出-解释

6 3
1 6 2 5 3 4
0 1 4
1 3 6
0 2 4
3

5
'''

line1=input()
n=eval(line1.split()[0])
m=eval(line1.split()[1])
arr=list(map(int,input().split()))
operate=[]
for i in range(0,m):
    operate.append(input())
q=eval(input())

for string in operate:
    op=int(string.split()[0])
    l=int(string.split()[1])-1
    r=int(string.split()[2])-1
    temp=arr[l:r+1]
    temp.sort(reverse=True if op==1 else False)
    arr[l:r+1]=temp.copy()

print(arr[q-1])




















