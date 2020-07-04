package SwordToOffer;

/**
 *  二叉树的下一个结点
 * 【就这么几种情况 记住就得了】
 * */
public class Exercise57 {
    public class TreeLinkNode {
        int val;
        TreeLinkNode left = null;
        TreeLinkNode right = null;
        TreeLinkNode next = null;      //这他妈真是父节点 叫next我属实是吐了

        TreeLinkNode(int val) {
            this.val = val;
        }
    }

    public TreeLinkNode GetNext(TreeLinkNode pNode){
        if(pNode.right==null){
            if(pNode.next==null)   // {5,4,#,3,#,2,#},5
                return null;
            TreeLinkNode father=pNode.next;
            if(father.left==pNode)   // {8,6,10,5,7,9,11},5
                return father;
            else
                if(father.next.left==father)    // {8,6,10,5,7,9,11},7
                    return father.next;
                else
                    return null;    // {8,6,10,5,7,9,11},11
        }
        TreeLinkNode cur=pNode.right;
        while(cur.left!=null){
            cur=cur.left;
        }
        return cur;     // {8,6,10,5,7,9,11},8
    }
}
