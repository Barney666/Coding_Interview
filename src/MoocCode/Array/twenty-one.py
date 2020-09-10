'''
题目描述:
给你两个数组，arr1 和 arr2，
arr2 中的元素各不相同
arr2 中的每个元素都出现在 arr1 中
对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。
arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
arr2 中的元素 arr2[i] 各不相同
arr2 中的每个元素 arr2[i] 都出现在 arr1 中

输入描述:
两行两个数组，两个数组分别是arr1 和 arr2

输出描述:
返回排好序的数组
'''


arr1=eval(input())
arr2=eval(input())

diff=[]
result=[]

for item in arr2:
    num=arr1.count(item)
    for i in range(0,num):
        result.append(item)
for item in arr1:
    if arr2.count(item)==0:
        diff.append(item)
diff.sort()
result+=diff
print(result)