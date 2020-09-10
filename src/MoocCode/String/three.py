'''
题目描述:
魔咒串由许多魔咒字符组成，魔咒字符可以用数字表示。例如可以将魔咒字符1、2拼凑起来形成一个魔咒串[1,2]。
一个魔咒串S的非空子串被称为魔咒串S的生成魔咒。
例如S=[1,2,1]时，它的生成魔咒有[1]、[2]、[1,2]、[2,1]、[1,2,1]五种。S=[1,1,1]时，它的生成魔咒有[1]、[1,1]、[1,1,1]三种。
最初S为空串。共进行n次操作，每次操作是在S的结尾加入一个魔咒字符。每次操作后都需要求出，当前的魔咒串S共有多少种生成魔咒。

输入描述:
第一行一个整数n。
第二行n个数，第i个数表示第i次操作加入的魔咒字符。

数据范围：
用来表示魔咒字符的数字x满足1≤x≤10^9。

输出描述:
输出n行，每行一个数。第i行的数表示第i次操作后S的生成魔咒数量。
测试样例

样例1:输入-输出-解释
7
1 2 3 3 3 1 2

1
3
6
9
12
17
22
'''

n=int(input())
arr=list(map(str,input().split()))
string=[]

for item in arr:
    record=[]
    num=0
    string.append(item)    # 这里注意string不能是个str 不然如果脑残用例每一个item不是1位 就会出错
    # string+=item
    for i in range(0,len(string)):
        for j in range(0,len(arr)-i):
            if j+i<len(string):
                # temp=string[j:j+i+1]
                temp="".join(string[x] for x in range(j,j+i+1))
                if (temp in record)==False:
                    num+=1
                    record.append(temp)
    print(num)
















