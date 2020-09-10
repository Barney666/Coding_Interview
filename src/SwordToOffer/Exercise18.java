package SwordToOffer;

/**
 * 二叉树的镜像
 *
 * */
public class Exercise18 {
    class TreeNode {
        int val = 0;
        TreeNode left = null;
        TreeNode right = null;

        public TreeNode(int val) {
            this.val = val;
        }
    }

    public void Mirror(TreeNode root) {
        if(root==null)
            return;
        TreeNode tempLeft=root.left;     // 因为不知道left和right是不是null，我还不想写太多if-else，就都保存了。
        TreeNode tempRight=root.right;
        root.left=tempRight;
        root.right=tempLeft;
        Mirror(root.left);
        Mirror(root.right);
    }
}
