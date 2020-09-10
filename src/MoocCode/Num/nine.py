'''
题目描述

从点 (x, y) 可以转换到 (x, x+y)  或者 (x+y, y)。

给定一个起点 (sx, sy) 和一个终点 (tx, ty)，如果通过一系列的转换可以从起点到达终点，则返回 True ，否则返回 False。

示例:
输入: sx = 1, sy = 1, tx = 3, ty = 5
输出: True
解释:
可以通过以下一系列转换从起点转换到终点：
(1, 1) -> (1, 2)
(1, 2) -> (3, 2)
(3, 2) -> (3, 5)

输入: sx = 1, sy = 1, tx = 2, ty = 2
输出: False

输入: sx = 1, sy = 1, tx = 1, ty = 1
输出: True
'''


def check(a,b):
    if a==endLeft and b==endRight:
        return True
    if a>endLeft or b>endRight:
        return False
    return check(a+b,b) or check(a,a+b)


if __name__ == '__main__':
    startLeft = int(input())
    startRight = int(input())
    endLeft = int(input())
    endRight = int(input())
    if startLeft == endLeft and startRight == endRight:
        print(True)
    print(check(startLeft,startRight))












