'''
题目描述:
给定一个正整数数组A。您的任务是对它们进行排序，以使数组的第一部分包含以降序排列的奇数，其余部分包含以升序排序的偶数。

输入描述:
输入的第一行包含一个整数T，表示测试用例的数量。然后是T测试用例。每个测试用例都包含一个整数N，它表示数组的大小。下一行包含N个以空格分隔的数组值。

输出描述:
对于换行中的每个测试用例，请打印修改后的数组的空格分隔值。
'''
t=int(input())
for i in range(0,t):
    n=int(input())
    arr=list(map(int,input().split()))
    odd=[]
    even=[]
    for item in arr:
        if item%2==0:
            even.append(item)
        else:
            odd.append(item)
    odd.sort(reverse=True)
    even.sort()
    result=odd+even
    string="".join(str(x)+" " for x in result)
    print(string.strip())
