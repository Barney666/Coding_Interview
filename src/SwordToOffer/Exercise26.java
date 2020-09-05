package SwordToOffer;

import java.util.Stack;

/**
 *  二叉搜索树与双向链表
 * 【其实本质是"非递归的中序遍历",挺重要也挺复杂的】
 *
 * */
public class Exercise26 {

    class TreeNode {
        int val = 0;
        TreeNode left = null;
        TreeNode right = null;

        public TreeNode(int val) {
            this.val = val;
        }
    }

    public TreeNode Convert(TreeNode pRootOfTree) {

        if(pRootOfTree==null)
            return null;

        Stack<TreeNode> stack=new Stack();
        TreeNode cur=pRootOfTree;

        while (cur!=null){     // 这块不能是cur.left!=null
            stack.push(cur);
            cur=cur.left;
        }
        TreeNode pre=null;

        while (!stack.empty()){
            cur=stack.pop();
            System.out.println(cur.val);
            if(pre==null)
                pre=cur;
            else{
                pre.right=cur;
                cur.left=pre;
                pre=cur;
            }
            if(cur.right!=null){
                cur=cur.right;
                while (true){     // 这块不能是cur.right!=null
                    stack.push(cur);
                    if(cur.left==null)
                        break;
                    else
                        cur=cur.left;
                }
            }
        }
        
        while (true){
            if(cur.left==null)
                break;
            else
                cur=cur.left;
        }
        return cur;
    }

}