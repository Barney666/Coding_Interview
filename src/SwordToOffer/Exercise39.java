package SwordToOffer;

/**
 * 判断是否为平衡二叉树
 *【无需考虑是否为排序二叉树】
 * */
public class Exercise39 {
    class TreeNode {
        int val = 0;
        TreeNode left = null;
        TreeNode right = null;

        public TreeNode(int val) {
            this.val = val;
        }
    }

    public int check(TreeNode node){
        int left;
        int right;
        if(node.left==null)
            left=0;
        else
            left=check(node.left);
        if(node.right==null)
            right=0;
        else
            right=check(node.right);
        if(left==-1 || right==-1)
            return -1;
        if(Math.abs(left-right)>1)
            return -1;
        return Math.max(left,right)+1;     // 注意子节点回给父节点的时候是取两者较大的+1，不是left+right+1
    }

    public boolean IsBalanced_Solution(TreeNode root) {
        if(root==null)
            return true;
        return check(root)==-1 ? false : true;
    }
}
