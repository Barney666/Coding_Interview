'''
题目描述

您将获得一个大小为N的数组A。您需要找到该数组中所有总和为数字K的对。如果不存在这样的对，则输出将为-1。数组的元素是不同的，并且按排序顺序排列。 注意：（a，b）和（b，a）被认为是相同的。另外，元素不能与自身配对，即（a，a）无效。

输入描述

输入的第一行是T，表示测试用例的数量。随后是T个测试用例。每个测试用例包含三行输入。第一行是数组N的大小。第二行包含N个由空格分隔的元素。第三行包含总和K。

输出描述

对于每个测试用例，打印所有对，使总和等于K
'''

t=int(input())
for i in range(0,t):
    n=int(input())
    arr=list(map(int,input().split()))
    sum=int(input())
    result=[]
    for i in range(0,n):
        basis=arr[i]
        for j in range(i+1,n):
            behind=arr[j]
            if basis+behind==sum:
                result.append(str(basis)+" "+str(behind))
    if len(result)==0:
        print(-1)
    else:
        for item in result:
            print(item,end="")
            print(" "+str(sum))