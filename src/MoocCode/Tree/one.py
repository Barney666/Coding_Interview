'''
题目描述:
输入一个二叉树的中序和后序遍历，请你输出一个叶子节点，该叶子节点到根的数值总和最小，且这个叶子是编号最小的那个。

输入描述:
您的程序将从输入文件中读取两行(直到文件结尾)。
第一行是树的中序遍历值序列,第二行是树的后序遍历值序列。所有值将不同，大于零且小于或等于10000。
二叉树的节1<=N<=10000。

输出描述:
对于每个树描述，您应该输出最小值路径的叶节点的值。存在多路径最小的情况下，您应该选择终端叶子节点上具有最小值的那条路径，且输出那个最小值的终端叶子。
'''
'''
分析：先通过后序和中序建立二叉树，在通过DFS进行搜索，找到符合题目要求的叶子节点。
中序和后序建立二叉树：
使用递归来建立，由后序确定当前递归中的分支的根节点，再在中序中找到根的位置，则中序中根左的为左子树的中序排列，根右的为右子树的中序。
设此时左子树的长度为len，则当前的后序的前len个数据是左子树的后序排列。同理进行递归即可。右子树同理。
'''
from Tree.Tree import Tree
from Tree.Tree import Node

def find(item):
    for i in range(0,len(inorder)):
        if inorder[i]==item:
            return i


def build(startIndex,endIndex,currentRoot,time):   # 后序的index  time是因为后序每一层的中间在最后 所以每往右一层都要整体往左移1个
    inorderIndex=find(currentRoot.item)

    if endIndex-startIndex<2:
        if endIndex-startIndex<=0:
            return
        if inorder[inorderIndex+1]==postorder[endIndex-1]:
            currentRoot.setrightChild(Node(postorder[endIndex-1]))
            return
        else:
            currentRoot.setLeftChild(Node(postorder[endIndex-1]))
            return
    leftStart=startIndex
    leftEnd=inorderIndex-1-time     # endIndex-(endIndex-inorderIndex)-1
    # 括号代表leftLength 这括号里的endIndex本应是中序的endIndex 但中序后序子树长度一样 所以用后序的endIndex没问题
    rightStart=inorderIndex-time    # endIndex-(endIndex-inorderIndex)
    rightEnd=endIndex-1

    leftChild=Node(postorder[leftEnd]) if leftStart<=leftEnd else None
    rightChild=Node(postorder[rightEnd]) if rightStart<=rightEnd else None
    currentRoot.setLeftChild(leftChild)
    currentRoot.setrightChild(rightChild)

    build(leftStart,leftEnd,leftChild,time) if leftChild!=None else None
    build(rightStart,rightEnd,rightChild,time+1) if rightChild!=None else None


def dfs(currentNode,sum):
    if currentNode.leftChild==None and currentNode.rightChild==None:
        return currentNode.item,sum
    else:
        leftSum=1000000
        rightSum=1000000
        if currentNode.leftChild!=None:
            tuple=dfs(currentNode.leftChild,sum+currentNode.leftChild.item)
            leftItem=tuple[0]
            leftSum=tuple[1]
        if currentNode.rightChild!=None:
            tuple = dfs(currentNode.rightChild, sum+currentNode.rightChild.item)
            rightItem = tuple[0]
            rightSum = tuple[1]
        if leftSum<rightSum:
            return leftItem,leftSum
        elif leftSum>rightSum:
            return rightItem,rightSum
        else:
            if leftItem<rightItem:
                return leftItem, leftSum
            else:
                return rightItem, rightSum

if __name__ == '__main__':
    inorder=list(map(int,input().split(" ")))    # 中序遍历
    postorder=list(map(int,input().split(" ")))  # 后序遍历
    root=Node(postorder[-1])
    build(0,len(postorder)-1,root,0)
    tree=Tree(root)
    print(dfs(root,0)[0])

