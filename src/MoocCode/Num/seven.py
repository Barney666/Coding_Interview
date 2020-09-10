'''
题目描述：
编写一个算法来判断一个数是不是“快乐数”。
一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。
如果可以变为 1，那么这个数就是快乐数。
'''

def find(num):
    while True:
        temp=0
        for item in str(num):
            temp+=(int(item)*int(item))
        if record.count(temp)!=0:
            return False
        else:
            if temp==1:
                return True
            record.append(temp)
            num=temp

if __name__ == '__main__':
    num = int(input())
    record = []
    print(find(num))