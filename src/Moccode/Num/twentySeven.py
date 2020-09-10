'''
题目描述:
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
'''

def check():
    for i in range(0,int(len(string)/2)+1):
        if string[i]!=string[len(string)-i-1]:
            return False
    return True
if __name__ == '__main__':
    string = input()
    print(check())