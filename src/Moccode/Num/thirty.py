'''
题目描述

罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

字符 数值 I 1 V 5 X 10 L 50 C 100 D 500 M 1000 例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做 XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。 X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。 给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

样例输入

III
样例输出

3
'''

string=input()
sum=0
arr=[]
special=["CD","CM","XL","XC","IV","IX"]
value=[400,900,40,90,4,9]
temp=""
i=0
while i<len(string)-1:
    front=string[i]
    behind=string[i+1]
    if front==behind:
        temp+=front
        if i==len(string)-2:
            arr.append(temp+behind)
        i+=1
    elif front+behind in special:
        arr.append(front+behind)
        i+=2
    else:   # 不同两个 还不是特殊的那个
        temp+=front
        arr.append(temp)
        temp=""
        i+=1

for item in arr:
    if item in special:
        index=special.index(item)
        sum+=value[index]
    else:
        for k in range(0,len(item)):
            if item[k]=="I":
                sum+=1
            elif item[k]=="V":
                sum+=5
            elif item[k]=="X":
                sum+=10
            elif item[k]=="L":
                sum+=50
            elif item[k]=="C":
                sum+=100
            elif item[k]=="D":
                sum+=500
            else:
                sum+=1000
print(sum)
'''
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
'''