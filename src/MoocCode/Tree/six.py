'''
题目描述

分别按照二叉树先序，中序和后序打印所有的节点。

输入描述

第一行输入两个整数 n 和 root，n 表示二叉树的总节点个数，root 表示二叉树的根节点。

以下 n 行每行三个整数 fa，lch，rch，表示 fa 的左儿子为 lch，右儿子为 rch。(如果 lch 为 0 则表示 fa 没有左儿子，rch同理)
输出描述

输出三行，分别表示二叉树的先序，中序和后序。
'''
from Tree.Tree import Tree
from Tree.Tree import Node

def preorder(currentNode,output):
    output+=(str(currentNode.item)+" ")
    if currentNode.leftChild!=None:
        output=preorder(currentNode.leftChild,output)
    if currentNode.rightChild!=None:
        output=preorder(currentNode.rightChild,output)
    return output

def inorder(currentNode,output):
    if currentNode.leftChild!=None:
        output=inorder(currentNode.leftChild,output)
    output+=(str(currentNode.item)+" ")
    if currentNode.rightChild!=None:
        output=inorder(currentNode.rightChild,output)
    return output

def postorder(currentNode,output):
    if currentNode.leftChild!=None:
        output=postorder(currentNode.leftChild,output)
    if currentNode.rightChild!=None:
        output=postorder(currentNode.rightChild,output)
    output+=(str(currentNode.item)+" ")
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
    print(preorder(root,"").strip())
    print(inorder(root,"").strip())
    print(postorder(root,"").strip())