'''
题目描述:
给你一个 m * n 的整数矩阵 mat ，请你将同一条对角线上的元素（从左上到右下）按升序排序后，返回排好序的矩阵。
m == mat.length
n == mat[i].length
1 <= m, n <= 100
1 <= mat[i][j] <= 100

输入描述:
一个 m * n 的整数矩阵 mat

输出描述:
返回排好序的矩阵

测试样例:
样例1: 输入-输出-解释

[[3,3,1,1],[2,2,1,2],[1,1,1,2]]

[[1,1,1,1],[1,2,2,2],[1,2,3,3]]

'''


list=eval(input())
m=len(list)
n=len(list[0])
result=[[None]*n for i in range(m)]     # m行n列的多维数组

for i in range(0,len(list)):
    temp=[]
    left=m-1-i
    right=0
    temp.append(list[left][right])
    while True:
        if left+1<=m-1 and right+1<=n-1:
            left+=1
            right+=1
            temp.append(list[left][right])
        else:
            break
    temp.sort()
    for j in range(0,len(temp)):
        tempLeft=m-1-i
        tempRight=0
        result[tempLeft+j][tempRight+j]=temp[j]

for i in range(1,n):
    temp=[]
    left=0
    right=i
    temp.append(list[left][right])
    while True:
        if left + 1 <= m - 1 and right + 1 <= n - 1:
            left += 1
            right += 1
            temp.append(list[left][right])
        else:
            break
    temp.sort()
    for j in  range(0,len(temp)):
        tempLeft=0
        tempRight=i
        result[tempLeft+j][tempRight+j]=temp[j]

print(result)










