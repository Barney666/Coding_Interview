'''
题目描述

自除数 是指可以被它包含的每一位数除尽的数。

例如，128 是一个自除数，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。

还有，自除数不允许包含 0 。

给定上边界和下边界数字，输出一个列表，列表的元素是边界（含边界）内所有的自除数。
'''

front=int(input())
behind=int(input())
result=[]
for num in range(front, behind+1):
    allDone=True
    for item in str(num):
        try:
            if num%(int(item))!=0:
                allDone=False
                break
        except:    # 10 20之类的
            allDone=False
            break
    if allDone:
        result.append(num)
print(result)
