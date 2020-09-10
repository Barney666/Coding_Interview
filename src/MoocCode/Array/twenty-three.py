'''
题目描述:
在Berland，有一个非常著名的纸牌游戏。这个纸牌游戏遵循以下的规则：如果在游戏的最后，只有一个选手获得了最高分，那么这个选手就是胜者。但是很多时候，情况往往比这个要复杂，最高分的选手可能不止一个。每局比赛中，每个选手都会得到或者失去一定的分数。每局比赛选手的名字和分数都会以“名字 分数”的形式列出来，分数是一个整数，但是有可能是负的。如果到了最后，有不止一个选手的分数是最高分（我们设最高分为 m），那么在这些人中，在比赛的过程中，第一个得到大于等于 m 分的人获胜。初始的时候，每个人的分数都是0分。

输入描述:
第一行是正整数 n 表示比赛的局数。（1<=n<=1000）
接下里 n 行，每行都是以“名字 分数“的形式，表示选手的名字和每局的得分，按照时间的先后顺序。
名字由小写字母 a 到 z 组成的，最多不超过 32 个字符，分数是一个整数，范围是 -1000 到 1000。
数据保证到最后至少有一个选手的分数是正的。

输出描述:
输出获胜选手的名字
'''
dict={}
record={}    # 最后一次的成绩是在第几次
time=int(input())
for i in range(0,time):
    string=input()
    name=string.split(" ")[0]
    score=int(string.split(" ")[1])
    num=dict.get(name)
    if num==None:
        dict[name]=score
        record[name]=[str(score)+"&"+str(i)]
    else:
        dict[name]=num+score
        record[name].append(str(score)+"&"+str(i))


most=max(dict.values())
arr=list(filter(lambda x:dict[x] == most, dict))
array=[]
if len(arr)==1:
    print(arr[0])
else:
    for item in arr:
        tempList=record.get(item)
        sum=0
        for num in tempList:
            sum+=int(num.split("&")[0])
            if sum>=most:
                array.append(int(num.split("&")[1]))
                break
smallest=min(array)
index=array.index(smallest)
print(arr[index])




# 15
# aawtvezfntstrcpgbzjbf 681
# zhahpvqiptvksnbjkdvmknb -74
# aawtvezfntstrcpgbzjbf 661
# jpdwmyke 474
# aawtvezfntstrcpgbzjbf -547
# aawtvezfntstrcpgbzjbf 600
# zhahpvqiptvksnbjkdvmknb -11
# jpdwmyke 711
# bjmj 652
# aawtvezfntstrcpgbzjbf -1000
# aawtvezfntstrcpgbzjbf -171
# bjmj -302
# aawtvezfntstrcpgbzjbf 961
# zhahpvqiptvksnbjkdvmknb 848
# bjmj -735



