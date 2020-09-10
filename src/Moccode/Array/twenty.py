'''
题目描述:
Rahul和Ankit是Royal Restaurant中仅有的两个服务员。今天，这家餐厅收到了N份订单。
当小费由不同的服务员处理时，小费的数量可能会有所不同，如果拉胡尔接受第i个订单，则小费为Ai卢比；如果安奇接受这笔订单，则小费为Bi卢比。
为了最大化小费总额，他们决定在他们之间分配订单。一个订单只能由一个人处理。
同样，由于时间限制，Rahul不能接受超过X的订单，Ankit不能接受超过Y的订单。
确保X + Y大于或等于N，这意味着所有订单都可以由Rahul或Ankit处理。处理所有订单后找出小费总额的最大可能金额。

输入描述:
第一行包含一个整数，测试用例数。
第二行包含三个整数N，X，Y。
第三行包含N个整数。第i个整数表示Ai。
第四行包含N个整数。第i个整数表示Bi。
'''

time=int(input())

for i in range(0,time):
    N, X, Y = map(int, input().split())     # 类型转换
    A = list(map(int, input().split()))    # 类型转换
    B = list(map(int, input().split()))    # 类型转换

    diff = []
    index = [i for i in range(N)]
    for i in range(N):
        diff.append((abs(A[i] - B[i]), index[i]))  # 求各个订单小费差，并合并序号
    diff.sort(reverse=True)  # 按小费差从大到小排序
    z = [i for x, i in diff]  # 获得排序后的订单序号
    sum = 0
    for i in z:
        if A[i] >= B[i]:
            if X > 0:  # 优先A接单
                sum += A[i]
                X -= 1
            else:
                sum += B[i]
                Y -= 1
        else:
            if Y > 0:  # 优先接单
                sum += B[i]
                Y -= 1
            else:
                sum += A[i]
                X -= 1
    print(sum)
