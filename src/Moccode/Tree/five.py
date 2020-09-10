'''
题目描述

二叉树中一个节点的后继节点指的是，二叉树的中序遍历的序列中的下一个节点。

输入描述

第一行输入两个整数 n 和 root，n 表示二叉树的总节点个数，root 表示二叉树的根节点。

以下 n 行每行四个整数 fa，lch，rch，表示 fa 的左儿子为 lch，右儿子为 rch。(如果 lch 为 0 则表示 fa 没有左儿子，rch同理)

最后一行输入要询问的节点 node。
输出描述

输出一个整数表示答案。(如果 node 是最后一个节点，则输出 0 )
测试样例

样例1:输入-输出-解释

10 6
6 3 9
3 1 4
1 0 2
2 0 0
4 0 5
5 0 0
9 8 10
10 0 0
8 7 0
7 0 0
10

0
'''
from Tree.Tree import Tree
from Tree.Tree import Node

def inorder(currentNode,output):
    if currentNode.leftChild!=None:
        output=inorder(currentNode.leftChild,output)
    output.append(currentNode.item)
    if currentNode.rightChild!=None:
        output=inorder(currentNode.rightChild,output)
    return output

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
    quest=eval(input())
    outputArr=inorder(root,[])
    for i in range(len(outputArr)):
        if outputArr[i]==quest:
            if i==len(outputArr)-1:
                print(0)
            else:
                print(outputArr[i+1])
