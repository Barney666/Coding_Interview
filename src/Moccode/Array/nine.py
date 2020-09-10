'''
题目描述:
给定一个大小为N的数组A，构造一个乘积数组P（大小相同），使得P等于除A [i]以外的所有元素的乘积。

输入描述:
输入的第一行包含一个整数T，表示测试用例的数量。随后是T个测试用例。每个测试用例包含两行输入。第一行是N。第二行包含N个由空格分隔的元素。

输出描述:
对于每个测试用例，打印乘积数组P。
'''
line1=int(input())
for i in range(0,line1):
    num=input()
    arr=eval("["+input().replace(" ",",")+"]")
    result=""
    for i in range(0,len(arr)):
        temp=1
        for j in range(0,len(arr)):
            if j!=i:
                temp*=arr[j]
        if result=="":
            result+=str(temp)
        else:
            result=result+" "+str(temp)
    print(result)




