'''
题目描述:
给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。
如果数组元素个数小于 2，则返回 0。

输入描述:
一个无序的数组

输出描述:
如果元素大于等于2，则输出排序之后，相邻元素之间最大的差值；否则输出0
'''

list=eval(input())
list=sorted(list)

diff=0
for i in range(0,len(list)-1):
    temp=abs(list[i]-list[i+1])
    if temp>diff:
        diff=temp
print(diff)

