'''
题目描述:
给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。
说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。

输入描述:
给定一个大小为 n 的数组

输出描述:
找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。
'''
import math
list=eval(input())
record={}

for item in list:
    if record.get(item)==None:
        record[item]=1
    else:
        record[item]=record.get(item)+1

result=[]
for item in record:
    if record.get(item) > math.floor(len(list)/3):
        result.append(item)

print(result)