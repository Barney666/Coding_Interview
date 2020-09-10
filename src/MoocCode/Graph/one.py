'''
题目描述:
大中锋正在一个游乐场里玩耍。游乐场里有很多娱乐设施，娱乐设施之间相互有道路相连，经过每一条路都需要花费一定的时间。为了方便游客，每一个娱乐设施旁都会配有一个小卖部，一部分小卖部会销售可乐，另一部分会销售汉堡。
由于大中锋十分贪吃，所以每当他走到一个娱乐设施，他都会先去购买一杯可乐或一个汉堡，并把它们吃掉。但如果大中锋吃掉的汉堡数量比他喝掉的可乐数量多于k，那他就会感到很渴；如果喝掉的可乐数量比吃掉的汉堡数量多于k，那他就会感到很饿。
现在大中锋正在第a个娱乐设施，他想前往第b个娱乐设施，但在他前进的路途中他不希望自己很渴或很饿。大中锋想知道自己在路上最少花费多少时间。但由于大中锋很懒惰，他不想思考这个问题。你能帮助他解决这个问题吗？
注意：大中锋非常贪吃，所以他到达每个点的第一件事是去吃（或者喝），才考虑其他的事情，所以在起始点和终点他都会去买汉堡（可乐），你也需要保证在这两个点他不会感到很饿或者很渴。

输入描述:
多样例输入，第一行输入一个正整数T表示样例数。
对于每一个样例：
第一行三个数字n,m,k，n代表游乐场一共有多少个娱乐设施，m代表游乐场一共有多少条道路，k的意义如题面中所述。
接下来有一行n个数字，第i个数字代表第i个小卖部销售的是什么，1代表可乐，2代表汉堡。
接下来有m行输入，每行三个数字p,q,t，代表从第p个娱乐设施到第q个娱乐设施有一条道路，通过这条道路需要花费t单位时间。
最后一行有两个整数a,b，代表大中锋想从娱乐设施a前往娱乐设施b。

输出描述:
每一组样例输出一行整数t，代表大中锋在路上既不会感到很渴也不会感到很饿的情况下，从娱乐设施a到娱乐设施b花费的最少时间，如果无法达到，输出-1。
测试样例

样例1:输入-输出-解释
1
2 1 1
1 1
1 2 1
1 2

-1
'''
'''
正常若没有可乐汉堡，就是一个Dijkstra最短路径问题，路的权值就是时间t，
有的话，就单独整一个变量，初始为0，喝可乐+1，吃汉堡-1，变量绝对值不能大于k即可 
'''
def dijkstra():
    if k<=1:
        return -1
    else:
        dist=[[None]*(n-1) for z in range(n)]   # n行n-1列
        path=[[None]*(n-1) for z in range(n)]
        isDone=[]    # 记录已经定下来的点

        dijkstraFrom=fromWhere    # Dijkstra是一个特定节点到其他节点 所以初始化节点应该是fromwhere 课件上那个图是从0开始的
        for toCurrent in range(n):   # 初始化第一列
            if wayTime[dijkstraFrom][toCurrent]!=None:
                dist[toCurrent][dijkstraFrom]=wayTime[dijkstraFrom][toCurrent]
                path[toCurrent][dijkstraFrom]=0
        isDone.append(dijkstraFrom)

        count=0
        while count<n-2:   # 共n-1列 count从0开始 而且后面用的count和count+1
            fromCurrent=min(dist[x][count] for x in range(n) and (x not in isDone) and dist[x][count]!=None)
            for toCurrent in range(n) and toCurrent not in isDone:
                dist[toCurrent][count+1]=dist[toCurrent][count]  # 先变成和上一次一样的 如果可以变 下面会再改
                if toCurrent!=fromCurrent and wayTime[fromCurrent][toCurrent]!=None:
                    if dist[toCurrent][count]==None or (dist[fromCurrent][count]+wayTime[fromCurrent][toCurrent])<dist[toCurrent][count]:
                        dist[toCurrent][count+1]=dist[fromCurrent][count]+wayTime[fromCurrent][toCurrent]
                        path[toCurrent][count+1]=fromCurrent
            count+=1

        # 然后正常就直接dist[toWhere][n-2]就行了 但这个题还要根据path算可乐汉堡的问题 如果不行还要回看n-3,n-4...
        index=n-2
        while index>=0:
            sum=0
            pathArr=[toWhere]
            isOK=True
            while pathArr[0]!=fromWhere:
                pathArr.insert(0,path[pathArr[0]][index])
            for saleNum in pathArr:
                if sale[saleNum]==1:
                    sum+=1
                else:
                    sum-=1
                if abs(sum)>k:
                    isOK=False
                    break
            if isOK:
                return dist[toWhere][index]
            index-=1
        return -1




if __name__ == '__main__':
    time=eval(input())
    for w in range(time):
        tempArr=input().split(" ")
        n=eval(tempArr[0])
        m=eval(tempArr[1])
        k=eval(tempArr[2])
        sale=list(map(int,input().split(" ")))
        wayTime=[[None]*n for z in range(n)]
        for z in range(m):
            tempArr=list(map(int,input().split(" ")))
            wayTime[tempArr[0]-1][tempArr[1]-1]=tempArr[2]    # 输入给的是1 2,这里应该用0 1
        tempArr=input().split(" ")
        fromWhere=eval(tempArr[0])-1    # 同样减1，方便访问数组
        toWhere=eval(tempArr[1])-1
        print(dijkstra())



















