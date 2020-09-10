'''
题目描述

给定所有到达火车站的火车的到达和离开时间。您的任务是找到火车站所需的最少平台数量，以便没有火车等待。 注意：请考虑所有火车在同一天到达并且在同一天离开。此外，一列火车的到达和离开时间将不同，但是我们可以让一列火车的到达时间等于另一列火车的离开时间。

在这种情况下，我们需要不同的平台，即在任何给定的时间实例中，不能将同一平台用于火车的出发和另一火车的到达。

输入描述

输入的第一行包含T，即测试用例的数量。对于每个测试用例，第一行将包含一个整数N，即列车数量。接下来的两行将由N个间隔的时间间隔组成，分别表示到达时间和离开时间。 注意：时间间隔为HHMM的24小时格式（hhmm），其中前两个字符表示小时（00到23之间），后两个字符表示分钟（00到59之间）。

输出描述

对于每个测试用例，请打印火车安全抵达和离开所需的最少平台数量。
'''

t=int(input())
for i in range(0,t):
    length=int(input())
    arrive=list(map(str,input().split()))
    leave=list(map(str,input().split()))
    plat=[]
    plat.append([arrive[0]+"&"+leave[0]])
    for i in range(1,length):
        arriveTime=arrive[i]
        leaveTime=leave[i]
        for tempList in plat:
            conflict=False
            for time in tempList:
                otherArriveTime=time.split("&")[0]
                otherLeaveTime=time.split("&")[1]
                if otherArriveTime<=arriveTime<=otherLeaveTime or otherArriveTime<=leaveTime<=otherLeaveTime:
                    conflict=True
                    break
            if conflict==False:
                tempList.append(arriveTime+"&"+leaveTime)
                break
            else:
                if plat.index(tempList)==len(plat)-1:
                    plat.append([arriveTime+"&"+leaveTime])
                    break
                else:
                    continue
    print(len(plat))












