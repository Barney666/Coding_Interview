'''
题目描述：
现在你总共有 n 门课需要选，记为 0 到 n-1。
在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
给定课程总量以及它们的先决条件，返回你为了学完所有课程所安排的学习顺序。
可能会有多个正确的顺序，你只要返回一种就可以了。如果不可能完成所有课程，返回一个空数组。
输入的先决条件是由边缘列表表示的图形，而不是邻接矩阵。你可以假定输入的先决条件中没有重复的边。
这个问题相当于查找一个循环是否存在于有向图中。如果存在循环，则不存在拓扑排序，因此不可能选取所有课程进行学习。

输入描述：
第一行一个整数，表示总共有 n 门课。第二行表示先修课程之间的关系。
输出描述：
返回学完所有课程所安排的学习顺序。
测试样例：
样例1: 输入-输出-解释
4
[[1,0],[2,0],[3,1],[3,2]]
[0,1,2,3]
总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。
因此，一个正确的课程顺序是 [0,1,2,3] 。另一个正确的排序是 [0,2,1,3] 。
'''


num=eval(input())
input=eval(input())
matrix=[[0] * num for x in range(num)]
inDegree=[0]*num
for arr in input:
    fromNum=arr[1]
    toNum=arr[0]
    if matrix[fromNum][toNum]==0:   # 这个if好像没必要
        inDegree[toNum]+=1
    matrix[fromNum][toNum]=1
result=[]
from queue import Queue
q=Queue()
for i in range(num):
    if inDegree[i]==0:
        q.put(i)   # 放入入度为0的节点
while not q.empty():
    fromNum=q.get()
    result.append(fromNum)
    for i in range(num):
        if matrix[fromNum][i]!=0:     # 节点 i 与该节点相连
            inDegree[i]-=1   # 与刚出队的节点相连的节点，入度减一
            if inDegree[i]==0:  # 如果为0，说明没有前驱，可以访问
                q.put(i)
print(result if len(result)==num else [])   # 如果所有节点都访问了，是说明成功了
