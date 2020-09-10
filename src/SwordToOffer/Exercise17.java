package SwordToOffer;

import java.util.ArrayList;

/**
 * 树的子结构
 *
 * */
public class Exercise17 {
    class TreeNode {
        int val = 0;
        TreeNode left = null;
        TreeNode right = null;

        public TreeNode(int val) {
            this.val = val;
        }
    }

    public ArrayList<TreeNode> FindExistence(TreeNode node, int findValue){
        ArrayList<TreeNode> result=new ArrayList<>();
        if(node.val==findValue)
            result.add(node);
        if(node.left!=null){
            ArrayList leftResult=FindExistence(node.left,findValue);
            result.addAll(leftResult);
        }
        if(node.right!=null){
            ArrayList rightResult=FindExistence(node.right,findValue);
            result.addAll(rightResult);
        }
        return result;
    }

    public boolean checkReal(TreeNode real, TreeNode maybeReal){
        if(real==null && maybeReal!=null)
            return false;
        if(real.val==maybeReal.val){
            boolean leftBool=true;
            boolean rightBool=true;
            if(maybeReal.left!=null)       // 因为子结构即可，所以real下面可能还有树，但不用看。
                leftBool = checkReal(real.left,maybeReal.left);
            if(maybeReal.right!=null)
                rightBool = checkReal(real.right,maybeReal.right);
            return leftBool && rightBool;
        }
        else return false;
    }

    public boolean HasSubtree(TreeNode root1,TreeNode root2) {
        if(root2==null)
            return false;
        if(root1==null && root2!=null)
            return false;
        ArrayList<TreeNode> maybeRealRoot2Arr=FindExistence(root1,root2.val);
        if(maybeRealRoot2Arr.size()==0)
            return false;
        for(TreeNode maybeRealRoot2:maybeRealRoot2Arr)
            if(checkReal(maybeRealRoot2,root2))
                return true;
        return false;
    }
}