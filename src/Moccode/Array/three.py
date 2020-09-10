'''
题目描述:
给定一个排序好的数组，两个整数 k 和 x，从数组中找到最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。
如果有两个数与 x 的差值一样，优先选择数值较小的那个数。
k 的值为正数，且总是小于给定排序数组的长度。
数组不为空，且长度不超过 104
数组里的每个元素与 x 的绝对值不超过 104

输入描述:
第一行给定一个排序好的数组，第二行和第三行分别是两个整数 k 和 x

输出描述:
最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。如果有两个数与 x 的差值一样，优先选择数值较小的那个数。
'''

list=eval(input())
k=int(input())
x=int(input())
diff=[]
result=[]

for item in list:
    diff.append(abs(item-x))
diff.sort()

for i in range(0,k):   #(0,k-1)
    try:
        index=list.index(x-diff[i])
    except:
        index=list.index(x+diff[i])
    result.append(list[index])
    list.pop(index)
result.sort()
print(result)
