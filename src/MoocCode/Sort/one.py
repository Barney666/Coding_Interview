'''
数组arr是[0, 1, ..., arr.length - 1]的一种排列，我们将这个数组分割成几个“块”，并将这些块分别进行排序。
之后再连接起来，使得连接的结果和按升序排序后的原数组相同。
我们最多能将数组分成多少块？
'''

def check(index):
    for j in range(0, index + 1):
        if dict[arr[j]]>index:
            return False
    for j in range(index+1,len(arr)):
        if dict[arr[j]]<=index:
            return False
    return True



if __name__ == '__main__':
    arr = eval(input())
    dict = {}
    for i in range(0, len(arr)):
        dict[arr[i]] = i
    arr.sort()
    result = 1
    for i in range(0, len(arr)-1):     # 最后一个不用检查 后面没有了 而且result初始值就是1
         temp=check(i)
         if temp:
             result+=1
    print(result)
