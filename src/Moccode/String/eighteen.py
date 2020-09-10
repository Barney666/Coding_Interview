'''
题目描述

给你一个字符串 s ，请你返回满足以下条件且出现次数最大的 任意 子串的出现次数：

子串中不同字母的数目必须小于等于 maxLetters 。
子串的长度必须大于等于 minSize 且小于等于 maxSize 。
输入描述

一个字符串 s。二到四行分别是：maxLetters，minSize，maxSize
1 <= s.length <= 10^5
1 <= maxLetters <= 26
1 <= minSize <= maxSize <= min(26, s.length)
s 只包含小写英文字母。
输出描述

返回满足条件且出现次数最大的任意子串的出现次数
'''
'''
不用管maxSize，因为如果一个长串满足条件，那么他的子串也一定满足，也就是说子串的次数一定大于等于长串。因此只需要看最短的即可
'''
string=input()
maxLetters=int(input())
minSize=int(input())
maxSize=int(input())
record={}

for i in range(0,len(string)-minSize+1):
    temp=string[i:i+minSize]
    charList=[]
    for char in temp:
        if char not in charList:
            charList.append(char)
    if len(charList)<=maxLetters:
        if record.get(temp)==None:
            record[temp]=1
        else:
            record[temp]=record.get(temp)+1
try:
    print(max(record.values()))
except:
    print(0)


