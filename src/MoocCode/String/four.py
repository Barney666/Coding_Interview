'''
题目描述

你需要开发一款文字处理软件。最开始时输入一个字符串（不超过 100 个字符）作为初始文档。可以认为文档开头是第 0 个字符。需要支持以下操作：

1 str：后接插入，在文档后面插入字符串 str，并输出文档的字符串。

2 a b：截取文档部分，只保留文档中从第 a 个字符起 b 个字符，并输出文档的字符串。

3 a str：插入片段，在文档中第 a 个字符前面插入字符串 str，并输出文档的字符串。

4 str：查找子串，查找字符串 str 在文档中最先的位置并输出；如果找不到输出 -1。

为了简化问题，规定初始的文档和每次操作中的 str 都不含有空格或换行。最多会有 q(q≤100) 次操作。

测试样例

输入

4
ILove
1 Luogu
2 5 5
3 3 guGugu
4 gu
输出

ILoveLuogu
Luogu
LuoguGugugu
3
'''

n=int(input())
basis=input()
for i in range(0,n):
    temp=input().split()
    if temp[0]=='1':
        basis+=temp[1]
        print(basis)
    elif temp[0]=='2':
        a=int(temp[1])
        b=int(temp[2])
        basis=basis[a:a+b]
        print(basis)
    elif temp[0]=='3':
        index = int(temp[1])
        string = temp[2]
        front=basis[0:index]
        behind=basis[index:]
        basis=front+string+behind
        print(basis)
    else:
        print(basis.index(temp[1]))









