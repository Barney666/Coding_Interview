'''
题目描述:
几乎每一个人都用 乘法表。但是你能在乘法表中快速找到第k小的数字吗？
给定高度m 、宽度n 的一张 m * n的乘法表，以及正整数k，你需要返回表中第k 小的数字。
'''
'''
如果我们需要在第i行中寻找大于num的个数，我们只要min(num / i, n)，
其中（i是这一行的行号，n是矩阵的列数）num / i代表的是如果num也在第i行，它存在的列数，所以只要取最小值就是第i行不大于num的个数。
（比如例题1中，我们需要知道第2行，不大于4的个数，min(4 / 2, 3) == 2个（就是2， 4））

那么如果我们需要确定这个乘法表中不大于num的个数就非常简单了，我们只要将每一行不大于num的个数累加即可。
（比如例题1中，我们需要知道乘法表中不大于4的个数，第一行3个、第二行2个，第三行1个）

现在我们就可以使用二分搜索了，初始化left = 1， right = n * m + 1，mid = （left + right） / 2，在m，n的乘法表中寻找不超过mid的个数。
直到这个个数等于k
'''
import math
def calculate(num):
    temp=0
    for i in range(1,m+1):
        temp+=(min(math.floor(num/i),n))    # 就用floor！
        # temp+=(min(math.ceil(num/i),n) if num/i>=1 else 0)    # 若>=1即说明会出现在这一行 得用向上取整 若<1则不会出现 就得用0
        # 若check用下面那种方法 这种加的temp也不对
    return temp

def check(begin,end):
    # while True:          因为乘法表里有重复的所以不能用这种方法
    #     mid=int(math.ceil((begin+end)/2))
    #     num=calculate(mid)
    #     if num==k:
    #         return mid
    #     elif num<k:
    #         begin=mid+1
    #     elif num>k:
    #         end=mid-1

    while begin<end:
        mid=math.floor((begin+end)/2)
        num=calculate(mid)
        if num<k:
            begin=mid+1
        elif num>=k:
            end=mid    # 不是mid-1！
    return begin
if __name__ == '__main__':
    m=eval(input())
    n=eval(input())
    k=eval(input())
    print(check(1,n*m+1))
