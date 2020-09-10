'''
题目描述：
皮特刚刚买了一辆新车。他刚到彼得堡最著名的加油站加油，突然发现油箱上有一把密码锁！锁的刻度为360度，指针一开始指向 0：
皮特给他的汽车经销商打了个电话，他的经销商让他把锁准确地转动 n 次。第 i 次旋转应该是 ai 度，顺时针或逆时针转都可以，n 次旋转之后指针应该再次指向 0。
这让皮特有点困惑，因为他不确定哪次旋转应该顺时针，哪次应该逆时针，因为旋转锁的方法有很多。已知输入的数据是每 1 次锁应该旋转的度数，请你帮助他判断一下是否至少存在一种旋转方法，在 n 次旋转之后指针会再次指向 0。

输入描述：
第一行输入旋转次数 n (1 ≤ n ≤ 15)
接下来的 n 行里，每行包含 1 个整数 ai 表示旋转度数 (1 ≤ ai ≤ 180)

输出描述：
如果存在一种旋转方法，最后指向 0，输出 YES，否则输出 NO

测试样例：
样例1: 输入-输出
3
10
20
30

YES
样例2: 输入-输出
3
10
10
10

NO
'''

def recursion(index,angle):
    if index==n:   # 这是n不能是n-1 不然少看一个数
        return True if angle%360==0 else False
    return recursion(index+1,angle+arr[index+1]) or recursion(index+1,angle-arr[index+1])


if __name__ == '__main__':
    n=int(input())
    arr=[]
    arr.append(None)      # 为了空一个出来 使得数据index从1开始 这样recursion的两个参数才能正常
    for i in range(0,n):
        temp=int(input())
        arr.append(temp)
    if recursion(0,0):
        print("YES")
    else:
        print("NO")

































