package SwordToOffer;

/**
 * 二叉树的序列化与反序列化  [ #表示空节点  !表示一个结点值的结束（即value!） ]
 *
 * */

public class Exercise61 {

    class TreeNode {
        int val = 0;
        TreeNode left = null;
        TreeNode right = null;

        public TreeNode(int val) {
            this.val = val;
        }
    }

    String string;

    void preOrder(TreeNode node){
        string +=String.valueOf(node.val);
        string +="!";
        if(node.left!=null)
            preOrder(node.left);
        else
            string+="#";
        if(node.right!=null)
            preOrder(node.right);
        else
            string+="#";
    }

    String Serialize(TreeNode root) {
        string="";
        if(root==null)
            return "#";
        preOrder(root);
        return string;
    }


    TreeNode Deserialize(String str) {
        string=str;
        if(str.equals("#") || str.equals(""))
            return null;
        return dePreOrder();
    }

    // 反序列化这里 由于Java不能引用传递 不能把每一次的node变成参数然后递归 只能将node变成返回值！
    TreeNode dePreOrder(){
        if(string.charAt(0)!='#'){
            int index=string.indexOf('!');
            int val=Integer.valueOf(string.substring(0,index));
            TreeNode node=new TreeNode(val);
            string=string.substring(index+1);
            node.left=dePreOrder();
            node.right=dePreOrder();
            return node;
        }
        else{
            string=string.substring(1);
            return null;
        }
    }
}