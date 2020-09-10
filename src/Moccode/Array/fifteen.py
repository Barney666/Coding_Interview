'''
题目描述：
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：
所有数字都是正整数。
解集不能包含重复的组合。

输入描述：
两个整数分别是 k 和 n

输出描述：
符合条件的所有数的组合
'''
x=input()
n=int(x.split(", ")[1])
k=int(x.split(", ")[0])

result=[]
if n<=(1+2+9):
    for i in range(1,8):  #(1,7)
        for j in range(1+i,9):   #(2,8)
            if (n-i-j)>j:
                result.append([i,j,n-i-j])
            else:
                break
print(result)


