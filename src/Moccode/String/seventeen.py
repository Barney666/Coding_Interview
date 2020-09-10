'''
题目描述

给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：

每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词。
说明:

如果不存在这样的转换序列，返回一个空列表。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
输入描述

两个单词（beginWord 和 endWord）和一个字典 wordList
输出描述

所有从 beginWord 到 endWord 的最短转换序列
'''

def init():
    copy=arr.copy()
    record={}

    for item in arr:
        if item==end:
            break
        for word in copy:
            if item==word:
                continue
            diff=0
            list1=list(item)
            list2=list(word)
            for char in list1:
                if list2.count(char)==0:
                    diff+=1
            if diff==1:
                if record.get(item)==None:
                    record[item]=[word]
                else:
                    record[item].append(word)
    return record

def find():
    word=begin
    tempList=[]
    tempList.append(word)
    while word!=end:
        value=record.get(word)
        if len(value)==1:
            tempList.append(value[0])
        else:      # len(value)>1
            if end in value:
                tempList.append(end)
                break
            tempValue=value.copy()
            for x in value:
                if x in tempList:
                    tempValue.remove(x)
            value=tempValue.copy()

            hasEnd = False
            hasEndList = []
            for x in value:
                if end in record.get(x):
                    hasEnd = True
                    hasEndList.append(x)
            if hasEnd:
                value=hasEndList

            for item in value:
                repetition = False
                if result==[]:
                    tempList.append(item)
                    break
                else:
                    for arr in result:
                        if len(tempList)>1 and arr[len(tempList)-1]==tempList[-1] and  arr[len(tempList)]==item:
                            repetition=True
                            break
                    if repetition==False:
                        tempList.append(item)
                        break
                    else:
                        if value.index(item)==len(value)-1:
                            return None
        if word not in tempList:
            word=tempList[-1]
        else:
            return None
    return tempList

if __name__ == '__main__':
    begin = input()
    end = input()
    arr = eval(input())
    arr.insert(0,begin)
    result=[]
    record=init()

    while True:
        temp=find()
        if temp!=None:
            result.append(temp)
        else:
            break
    print(result)
















