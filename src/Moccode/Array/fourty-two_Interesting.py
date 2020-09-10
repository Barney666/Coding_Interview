'''
题目描述：
给定一个数组arr []和一个数字K（其中K小于数组的大小），任务是在给定数组中找到第K个最小的元素。假定所有数组元素都是不同的。 预期时间复杂度：O（n）

输入描述：
输入的第一行包含一个整数T，表示测试用例的数量。然后是T测试用例。每个测试用例包含三行。
每个测试用例的第一行包含一个整数N，表示数组的大小。第二行包含N个以空格分隔的表示数组元素的整数。测试用例的第三行包含一个整数K。

输出描述：
对应每个测试用例，在新行中打印第k个最小的元素。
'''
'''
若先排一遍序 再直接取arr[k-1] 平均时间复杂度o(n*logn)
若用堆排 先建最小堆 然后删k次 不断调整 最后栈顶元素就是第k小个数 
此时堆的高度至多为logk，建立堆的时间为k*logk；而调整的次数为k，每次调整的时间为logk，所以调整的时间为k*logk，所以总的时间复杂度为k*logk 
这里用快排 最坏的时间复杂度是o(k*n)也就是o(n) 平均的时间复杂度o(k*logk) 【注意是k不是n】 
'''
def qucikSort(start,end):
    left=start
    right=end
    basis=arr[left]
    while left<right:
        while left<right and arr[right]>=basis:
            right-=1
        arr[left]=arr[right]
        while left<right and arr[left]<basis:
            left+=1
        arr[right]=arr[left]
    arr[left]=basis
    return left

def find(start,end,k):
    if start==end:
        return
    else:
        if start<end:
            num=qucikSort(start,end)
        if num==k:
            return
        elif num>k:
            find(start,num-1,k)
        else:
            find(num+1,end,k)

if __name__ == '__main__':
    t=int(input())
    for i in range(0,t):
        n=int(input())
        arr=list(map(int,input().split()))
        k=int(input())
        find(0,n-1,k)
        print(arr[k-1])    # 这时候第k小个数已经排好了 但index是k-1



