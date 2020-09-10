'''
题目描述:
给定一位研究者论文被引用次数的数组（被引用次数是非负整数）。编写一个方法，计算出研究者的 h 指数。
h 指数的定义: “h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （N 篇论文中）至多有 h 篇论文分别被引用了至少 h 次。
（其余的 N - h 篇论文每篇被引用次数不多于 h 次。）”
'''

def find():
    for k in range(0,len(arr)):
        time=size-k
        temp=0
        for item in arr:
            if item>time:
                temp+=1
        if temp==time:
            return temp
if __name__ == '__main__':
    arr = eval(input())
    size = len(arr)
    print(find())