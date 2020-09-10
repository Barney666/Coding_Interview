'''
题目描述:
给定一颗二叉树，分别实现按层和 ZigZag 打印二叉树。 ZigZag遍历: 意思是第一层从左到右遍历，第二层从右到左遍历，依次类推。

输入描述:
第一行输入两个整数 n 和 root，n 表示二叉树的总节点个数，root 表示二叉树的根节点。
以下 n 行每行三个整数 fa，lch，rch，表示 fa 的左儿子为 lch，右儿子为 rch。(如果 lch 为 0 则表示 fa 没有左儿子，rch同理)
样例1:输入-输出-解释
8 1
1 2 3
2 4 0
4 0 0
3 5 6
5 7 8
6 0 0
7 0 0
8 0 0

Level 1 : 1
Level 2 : 2 3
Level 3 : 4 5 6
Level 4 : 7 8
Level 1 from left to right: 1
Level 2 from right to left: 3 2
Level 3 from left to right: 4 5 6
Level 4 from right to left: 8 7
'''
from Tree.Tree import Tree
from Tree.Tree import Node


def check(currentNode,layer):
    output[layer-1]+=(str(currentNode.item)+" ")
    if currentNode.leftChild!=None:
        check(currentNode.leftChild,layer+1)
    if currentNode.rightChild!=None:
        check(currentNode.rightChild,layer+1)


if __name__ == '__main__':
    record=[]

    line1=list(map(int,input().split()))
    n=line1[0]
    root=Node(line1[1])
    record.append(root)
    for i in range(n):
        line=list(map(int,input().split(" ")))
        father=None
        for node in record:
            if node.item==line[0]:
                father=node
        if father==None:
            father=Node(line[0])
            record.append(father)
        if line[1]!=0:
            lch = Node(line[1])
            father.setLeftChild(lch)
            record.append(lch)
        if line[2]!=0:
            rch = Node(line[2])
            father.setrightChild(rch)
            record.append(rch)
    output=["" for x in range(len(record))]
    check(root,1)   # TODO 记得Strip
    for i in range(len(output)):
        if output[i]!='':
            print("Level "+str(i+1)+" : "+output[i].strip())
        else:
            break
    for i in range(len(output)):
        if output[i]!='':
            if i%2==0:
                print("Level "+str(i+1)+" from left to right: "+output[i].strip())
            else:
                print("Level "+str(i+1)+" from right to left: "+output[i].strip()[::-1])
        else:
            break












