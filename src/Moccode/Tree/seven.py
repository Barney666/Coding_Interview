'''
题目描述

异或是一种神奇的运算,大部分人把它总结成不进位加法.

在生活中…xor运算也很常见。比如，对于一个问题的回答，是为1，否为0.那么：

（A是否是男生 ）xor（ B是否是男生）＝A和B是否能够成为情侣

好了，现在我们来制造和处理一些复杂的情况。比如我们将给出一颗树，它很高兴自己有N个结点。树的每条边上有一个权值。我们要进行M次询问，对于每次询问，我们想知道某两点之间的路径上所有边权的异或值。

输入描述

输入文件第一行包含一个整数N，表示这颗开心的树拥有的结点数，以下有N-1行，描述这些边，每行有3个数，u,v,w,表示u和v之间有一条权值为w的边。接下来一行有一个整数M，表示询问数。之后的M行，每行两个数u,v，表示询问这两个点之间的路径上的权值异或值。
输出描述

输出M行，每行一个整数，表示异或值
测试样例

样例1:输入-输出-解释
5
1 4 9644
2 5 15004
3 1 14635
5 3 9684

3
2 4
5 4
1 1

975
14675
0
'''

from Tree.Tree import Edge

def find(now,destination,weight):


if __name__ == '__main__':
    n=eval(input())
    record=[]
    for i in range(n-1):
        temp=list(map(int,input().split(" ")))
        record.append(Edge(temp[0],temp[1],temp[2]))
    m=eval(input())
    for i in range(m):
        temp=list(map(int,input().split(" ")))
        print(find(temp[0],temp[1]))



    #异或直接十进制用^







