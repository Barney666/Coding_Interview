package SwordToOffer;

/**
 * 二叉搜索树的第k个结点
 * */
public class Exercise62 {

    class TreeNode {
        int val = 0;
        TreeNode left = null;
        TreeNode right = null;

        public TreeNode(int val) {
            this.val = val;
        }
    }

    int find;
    int current=0;

    // 二叉搜索树的中序遍历就是树节点值的递增排列！！！
    public TreeNode inorder(TreeNode node){
        if(node.left!=null){
            TreeNode back=inorder(node.left);
            if(back!=null)
                return back;
        }
        current++;
        if(current==find)
            return node;
        if(node.right!=null){
            TreeNode back=inorder(node.right);
            if(back!=null)
                return back;
        }
        return null;
    }

    TreeNode KthNode(TreeNode pRoot, int k){
        find=k;
        if(pRoot == null || k <= 0){    //记得写！！！
            return null;
        }
        return inorder(pRoot);
    }
}