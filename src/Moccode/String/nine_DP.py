'''
题目描述:
折叠的定义如下：
1.一个字符串可以看成它自身的折叠。记作S = S
2.X(S)是X(X>1)个S连接在一起的串的折叠。记作X(S) = SSSS…S(X个S)。
3.如果A = A’, B = B’，则AB = A’B’ 例如，因为3(A) = AAA, 2(B) = BB，所以3(A)C2(B) = AAACBB，而2(3(A)C)2(B) = AAACAAACBB 给一个字符串，求它的最短折叠。例如AAAAAAAAAABABABCCD的最短折叠为：9(A)3(AB)CCD。

输入描述:
仅一行，即字符串S，长度保证不超过100。

输出描述:
仅一行，即最短的折叠长度。
'''
def check(a,b,c,d):
    frontSize = b-a+1
    if (d-c+1)%frontSize != 0:
        return False
    else:
        for i in range(c,d+1):   # 这里是c到d 因此要变成d+1
            if string[i]!=string[i-frontSize]:
                return False
        return True

if __name__ == '__main__':
    string=input()
    size=len(string)
    dp=[[0 if i!=j else 1 for i in range(0,size)] for j in range(0,size)]    # size*size的二维数组 对角线是1
    for i in range(size-2,-1,-1):    # 从后往前 i初始值是倒数第二个数 直到list[-1]也就是列表最前面的数
        for j in range(i+1,size):
            length=j-i+1
            dp[i][j]=length
            for k in range(i,j):
                if check(i,k,k+1,j):     # 是有可折叠的
                    dp[i][j]=min(dp[i][j],dp[i][k]+2+len(str(int(length/(k-i+1)))))   # 2是()的长度 后面是计算折叠个数的长度
                else:
                    dp[i][j]=min(dp[i][j],dp[i][k]+dp[k+1][j])
    print(dp[0][size-1])


