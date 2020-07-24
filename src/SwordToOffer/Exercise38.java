package SwordToOffer;
/**
 * 二叉树的深度
 * */

public class Exercise38 {
    class TreeNode {
        int val = 0;
        TreeNode left = null;
        TreeNode right = null;

        public TreeNode(int val) {
            this.val = val;
        }
    }

    public int TreeDepth(TreeNode root) {
        if(root==null)
            return 0;
        int left;
        int right;
        if(root.left==null)
            left=0;
        else
            left=TreeDepth(root.left);
        if(root.right==null)
            right=0;
        else
            right=TreeDepth(root.right);
        return Math.max(left,right)+1;
    }
}
