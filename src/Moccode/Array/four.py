'''
题目描述:
传送带上的包裹必须在 D 天内从一个港口运送到另一个港口。
传送带上的第 i 个包裹的重量为 weights[i]。每一天，我们都会按给出重量的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。
返回能在 D 天内将传送带上的所有包裹送达的船的最低运载能力。

输入描述:
第一行是一个列表，包裹的重量 weights[i]。第二行是整数D 天。
1 <= D <= weights.length <= 50000
1 <= weights[i] <= 500

输出描述:
返回能在 D 天内将传送带上的所有包裹送达的船的最低运载能力。
'''
import math
list=eval(input())
requestedDay=int(input())

sum=0
biggest=list[0]
for item in list:
    sum+=item
    if item>biggest:
        biggest=item
basic=max(biggest, math.ceil(sum / requestedDay))
result=basic

for i in range(0,biggest):
    temp=0
    day=0
    for item in list:
        temp+=item
        if temp>(basic+i):
            temp=item
            day+=1
            newDay=True
        if list.index(item)==len(list)-1:
            day+=1     # 然后就直接结束了
    if day==requestedDay:
        result=basic+i
        break
print(result)