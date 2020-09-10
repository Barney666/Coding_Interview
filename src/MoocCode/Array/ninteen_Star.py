'''
题目描述:
给定数组 A，我们可以对其进行煎饼翻转：我们选择一些正整数 k <= A.length，然后反转 A 的前 k 个元素的顺序。
我们要执行零次或多次煎饼翻转（按顺序一次接一次地进行）以完成对数组 A 的排序。
返回能使 A 排序的煎饼翻转操作所对应的 k 值序列。任何将数组排序且翻转次数在 10 * A.length 范围内的有效答案都将被判断为正确。

1 <= A.length <= 100
A[i] 是 [1, 2, ..., A.length] 的排列

输入描述:
一个数组 A

输出描述:
返回能使 A 排序的煎饼翻转操作所对应的 k 值序列。

样例1: 输入-输出-解释
[3,2,4,1]

[4,2,4,3]

我们执行 4 次煎饼翻转，k 值分别为 4，2，4，和 3。
初始状态 A = [3, 2, 4, 1]
第一次翻转后 (k=4): A = [1, 4, 2, 3]
第二次翻转后 (k=2): A = [4, 1, 2, 3]
第三次翻转后 (k=4): A = [3, 2, 1, 4]
第四次翻转后 (k=3): A = [1, 2, 3, 4]，此时已完成排序。
'''
'''
每次把未排序的最大数放在最前面 再放到最后
'''



def specialReverse(num,list):
    result.append(num)
    temp=list[0:num]
    temp.reverse()
    return temp+list[num:]

def findMaxIndex(num,list):     # num是前几个数
    temp=list[0:num]
    biggest=max(temp)
    return list.index(biggest)    # 注意这里是index
def whetherSorted(num,list):
    temp=list[0:num]
    normal=sorted(temp)
    if temp==normal:
        return True
    else:
        return False

if __name__ == '__main__':
    result = []
    import math
    list=eval(input())
    size=len(list)

    for i in range( 0, (size-1)*2) :
        x=math.floor(i/2)
        if whetherSorted(size-x,list):
            break
        else:
            index=findMaxIndex(size-x,list)
            if index==0:
                list=specialReverse(size-x,list)
            else:
                list=specialReverse(index+1,list)

    print(result)




























