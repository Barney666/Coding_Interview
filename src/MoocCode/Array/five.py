'''
题目描述:
给出一个无重叠的 ，按照区间起始端点排序的区间列表。
在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

输入描述:
第一行是按照区间起始端点排序的区间列表，第二行是一个新的区间

输出描述:
新的合并后的区间列表
'''

# 以list合并区间
def merge(intervals):
    result = []
    if len(intervals) == 0:
        return []
    if len(intervals) == 1:
        return intervals

    # 先排序,降低复杂度
    intervals = sorted(intervals, key=lambda x: x[0])

    left = intervals[0][0]  # 记录字区间左边界
    right = intervals[0][1]  # 用于记录子区间的右边界

    for i in range(1, len(intervals)):
        if right >= intervals[i][0]:
            right = max(intervals[i][1], right)  # 取当前右边区间和之前记录的right右区间的值谁#大,取较大值
        else:
            result.append([left, right])
            left = intervals[i][0]
            right = intervals[i][1]
    result.append([left, right])

    return result


arr=eval(input())
intervals=eval(input())
arr.append(intervals)
print(merge(arr))
