'''
题目描述

小明忘了登录网站的密码。虽然忘记密码，但他还记得密码是由一个字符串组成。密码是由原文字符串（由不超过 50 个小写字母组成）中每个字母向后移动 n 位形成的。z 的下一个字母是 a，如此循环。他现在找到了移动前的原文字符串及 n，请你求出密码。

输入描述

第一行：n。第二行：未移动前的一串字母
输出描述

一行，为密码
'''

n=int(input())
string=input().strip()
result=""

for item in string:
    temp=chr(ord(item)+n if ord('A')<=ord(item)+n<=ord('Z') or ord('a')<=ord(item)+n<=ord('z') else ord(item)+n-26)

    result+=temp


print(result,end="")