class Node:
    def __init__(self, item):
        self.item = item
        self.leftChild = None
        self.rightChild = None

    def setLeftChild(self, leftChild):
        self.leftChild = leftChild

    def setrightChild(self, rightChild):
        self.rightChild = rightChild

    def __str__(self):
        return self.item

class Tree:
    def __init__(self, root):
        self.root = root

    def __str__(self):
        return self.root

class Edge:
    def __init__(self,Node1,Node2,weight):
        self.Node1=Node1
        self.Node2=Node2
        self.weight=weight

    def __str__(self):
        return self.weight



