'''
题目描述

给定一个整数数组，判断数组中是否有两个不同的索引 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值最大为 t，并且 i 和 j 之间的差的绝对值最大为 ķ。

输入描述

一个整数数组,和两个非负整数k,t。
输出描述

true或者false
测试样例

样例1: 输入-输出-解释

nums = [1,2,3,1], k = 3, t = 0
true
'''

def check():
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            num1=arr[i]
            num2=arr[j]
            if abs(i-j)<=k and abs(num1-num2)<=t:
                return "true"
    return "false"

if __name__ == '__main__':
    string = input()
    t = eval(string[-1])
    k = eval(string[-8])
    arr = eval(string[7:-14])
    print(check())