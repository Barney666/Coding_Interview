'''
题目描述
一个已排序好的表 A，其包含 1 和其他一些素数. 当列表中的每一个 p<q 时，我们可以构造一个分数 p/q 。
那么第 k 个最小的分数是多少呢? 以整数数组的形式返回你的答案, 这里 answer[0] = p 且 answer[1] = q.
'''
'''
和第9题一样 都是二分mid 
'''

def check():
    begin=0
    end=1
    while True:
        mid=(begin+end)/2

        sum=0
        p=0
        q=-1
        for i in range(0,len(arr)):
            temp=0
            for j in range(len(arr)-1,-1,-1):
                up=arr[i]
                down=arr[j]
                if up/down<=mid:
                    temp+=1
                    if up/down>p/q:
                        p=up
                        q=down
                else:
                    sum+=temp
                    break
        if sum==k:
            return [p,q]
        elif sum<k:
            begin=mid
        else:
            end=mid
if __name__ == '__main__':
    arr=eval(input())
    k=eval(input())
    print(check())
