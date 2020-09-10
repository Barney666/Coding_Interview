'''
题目描述:
给定一个机票的字符串二维数组 [from, to]，子数组中的两个成员分别表示飞机出发和降落的机场地点，对该行程进行重新规划排序。
所有这些机票都属于一个从JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 出发。
1.如果存在多种有效的行程，你可以按字符自然排序返回最小的行程组合。例如，行程 ["JFK", "LGA"] 与 ["JFK", "LGB"] 相比就更小，排序更靠前
2.所有的机场都用三个大写字母表示（机场代码）。
3.假定所有机票至少存在一种合理的行程。
'''

string=input()

dict={}         # 处理输入 放进map
tempArr=[]
tempStr=""
start=False
for c in string:
    if c=='[':
        start=True
    elif c==']':
        if tempStr!="":
            tempArr.append(tempStr)
            if dict.get(tempArr[0])==None:
                dict[tempArr[0]]=[tempArr[1]]
            else:    # 处理排序
                tempList=dict[tempArr[0]]
                tempList.append(tempArr[1])
                for i in range(len(tempList)-1):
                    str1=tempList[i]
                    str2=tempList[i+1]
                    for j in range(len(str1)):   #都是三个字母
                        if str1[j]<str2[j]:
                            break
                        elif str1[j]>str2[j]:
                            temp=tempList[i]
                            tempList[i]=tempList[i+1]
                            tempList[i+1]=temp
            tempArr=[]
            tempStr=""
        start=False
    else:
        if start:
            if c!=',':
                if c!='"' and c!=' ':
                    tempStr+=c
            else:
                tempArr.append(tempStr)
                tempStr=""

result=["JFK"]
while True:
    try:
        destination=dict[result[-1]][0]
        dict[result[-1]].pop(0)
        result.append(destination)
    except:
        break
print(result)















