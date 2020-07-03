package SwordToOffer;

import java.util.ArrayDeque;

/**
 * 对称的二叉树
 * 【二叉树和其镜像是一样的就是对称的】
 * */

public class Exercise58 {
    class TreeNode {
        int val = 0;
        TreeNode left = null;
        TreeNode right = null;

        public TreeNode(int val) {
            this.val = val;
        }
    }

    boolean isSymmetrical(TreeNode pRoot){
        ArrayDeque<TreeNode> arrayDeque=new ArrayDeque();
        if(pRoot==null || (pRoot.left==null && pRoot.right==null))
            return true;
        if(pRoot.left==null || pRoot.right==null)
            return false;
        arrayDeque.add(pRoot.left);
        arrayDeque.add(pRoot.right);
        while(!arrayDeque.isEmpty()){
            if((arrayDeque.size()&1)==1)
                return false;
            ArrayDeque<TreeNode> leftDeque=new ArrayDeque();
            ArrayDeque<TreeNode> rightDeque=new ArrayDeque();
            while(!arrayDeque.isEmpty()){
                TreeNode left=arrayDeque.pollFirst();
                TreeNode right=arrayDeque.pollLast();
                if(left.val!=right.val)
                    return false;
                if(left.left!=null)
                    leftDeque.add(left.left);
                else if(right.right!=null)   // 有一个null两个都得是null 这步很重要 不然有问题
                    return false;
                if(left.right!=null)
                    leftDeque.add(left.right);
                else if(right.left!=null)
                    return false;
                if(right.right!=null)
                    rightDeque.add(right.right);
                else if(left.left!=null)
                    return false;
                if(right.left!=null)
                    rightDeque.add(right.left);
                else if(left.right!=null)
                    return false;
            }
            while(!rightDeque.isEmpty()){
                leftDeque.add(rightDeque.pollLast());
            }
            arrayDeque=leftDeque;
        }
        return true;
    }
}
