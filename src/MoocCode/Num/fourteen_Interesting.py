'''
题目描述:
给定一个整数，写一个函数来判断它是否是 3 的幂次方。
进阶：
你能不使用循环或者递归来完成本题吗？
'''
'''
方法一：一直除以3

方法二：转换位3进制判断是否只有一个前导1

方法三：算出int范围内最大的3幂次方，是3^19（方便写设为x），只要x取余n为0，则n为所求结果  ✅
但是python没有最大范围 只要内存够大 就能表示 所以让用Python写算法就nm离谱
'''
n=int(input())

hypothetic_Max=pow(3,19)

if n==0:
    print(False)
else:
    print(True if hypothetic_Max%n==0 else False)