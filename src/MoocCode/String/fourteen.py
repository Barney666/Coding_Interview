'''
题目描述

有了防护伞，并不能完全避免 2012 的灾难。地球防卫小队决定去求助外星种族的帮助。经过很长时间的努力，小队终于收到了外星生命的回信。
但是外星人发过来的却是一 串密码。只有解开密码，才能知道外星人给的准确回复。
解开密码的第一道工序就是解压 缩密码，外星人对于连续的若干个相同的子串“X”会压缩为“[DX]”的形式（D 是一个整 数且 1≤D≤99），
比如说字符串“CBCBCBCB”就压缩为“[4CB]”或者“[2[2CB]]”，类似于后面这种压缩之后再压缩的称为二重压缩。如果是“[2[2[2CB]]]”则是三重的。
现 在我们给你外星人发送的密码，请你对其进行解压缩。

输入描述

第一行：一个字符串
输出描述

第一行：一个字符串
'''

def decompress(string):
    result=""
    temp=""
    num=""
    i=0
    while i<len(string):
        item=string[i]
        if item != '[' and item != ']':
            if '0'<=item<='9':
                num+=item    # 因为num有可能是两位数
            else:
                temp += item
            i+=1
        else:
            if item=='[':
                comeback=decompress(string[i + 1:])
                temp+=comeback[0]
                i+=comeback[1]
            else:
                if num == "":
                    num = "1"  # 说明没有多个 就变回1
                for x in range(0, int(num)):
                    result += temp
                i+=1
                return result,i+1
    if num == "":
        num = "1"  # 说明没有多个 就变回1
    for x in range(0, int(num)):
        result += temp
    return result,i+1

if __name__ == '__main__':
    string=input()
    print(decompress(string)[0])

#[3[7AB[2PIK]][10O]]