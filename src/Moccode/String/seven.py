'''
题目描述

小明在沙盘上写了这样一些字符串：

A1 = “A”

A2 = “ABA”

A3 = “ABACABA”

A4 = “ABACABADABACABA”

… …

你能找出其中的规律并写所有的数列AN吗？

输入描述

仅有一个数：N  ≤  26。
输出描述

请输出相应的字符串AN，以一个换行符结束。输出中不得含有多余的空格或换行、回车符。
'''

n=int(input())
result="A"

for i in range(1,n):
    temp="".join(reversed(result))
    temp=chr(65+i)+temp
    result+=temp
print(result)



















