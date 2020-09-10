'''
题目描述
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
'''
'''
根据题目的意思，字母异位词是指由相同的字母按照不同的顺序组成的单词，
根据此含义，那么这两个单词的长度也一定相等，所以我们就可以先将两个单词按照字母的大小进行排序，然后比较两个单词对应位置上的字母是否相等。
'''

def check(s,t):
    if len(s)!=len(t):
        return "false"
    else:
        arr = list(s)
        arr.sort()
        s = "".join(arr)
        arr = list(t)
        arr.sort()
        t = "".join(arr)
        for i in range(0, len(s)):
            if s[i]!=t[i]:
                return "false"
        return "true"


if __name__ == '__main__':
    string=input()
    s=eval(string.split(",")[0].split("=")[1].strip())
    t=eval(string.split(",")[1].split("=")[1].strip())
    print(check(s,t))