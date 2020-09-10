'''
题目描述:
给定两个分别为大小M和N的排序数组A和B以及元素k。我们的任务是找到位于最终排序数组第k个位置的元素。

输入描述:
第一行由每一次的测试用例个数组成。
每个测试用例的第一行由3个整数M，N和K组成，分别表示A中的元素数M，B中的元素数N和第k个位置元素。
每个测试用例的第二行和第三行分别由A和B元素组成。

输出描述:
将元素打印在第K个位置。
'''

line1=input()
result=""
for i in range(0,int(line1)):
    line2=input()
    line3=input()
    line4=input()
    num=int(line1)
    m=line2.split(" ")[0]
    n=line2.split(" ")[1]
    k=line2.split(" ")[2]
    a=eval("["+line3.replace(" ",",")+"]")
    b=eval("["+line4.replace(" ",",")+"]")
    a+=b
    a.sort()
    print(a[int(k)-1])