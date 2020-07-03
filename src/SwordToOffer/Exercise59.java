package SwordToOffer;

import java.util.*;

public class Exercise59 {
    class TreeNode {
        int val = 0;
        TreeNode left = null;
        TreeNode right = null;

        public TreeNode(int val) {
            this.val = val;
        }
    }

    public ArrayList<ArrayList<Integer>> Print(TreeNode pRoot) {
        ArrayList<ArrayList<Integer>> outer=new ArrayList();
        if(pRoot==null)
            return outer;
        ArrayDeque<TreeNode> queue=null;
        int count=0;
        while(true){
            if(queue!=null && queue.size()==0){
                outer.remove(outer.size()-1);    //最后会多出一个空的 把它删掉
                break;
            }
            ArrayList<Integer> inner=new ArrayList();
            ArrayDeque<TreeNode> temp=new ArrayDeque();
            if(queue==null){
                inner.add(pRoot.val);
                outer.add(inner);
                temp.add(pRoot);
            }
            else{
                if((count&1)==0){
                    while (!queue.isEmpty()){
                        TreeNode node=queue.pollLast();   //这块都得是从后面取 因为上一次是倒着的 这一次想正过来 就也得是从后面开始
                        if(node.left!=null){
                            inner.add(node.left.val);
                            temp.add(node.left);
                        }
                        if(node.right!=null){
                            inner.add(node.right.val);
                            temp.add(node.right);
                        }
                    }
                }
                else {
                    while (!queue.isEmpty()){
                        TreeNode node=queue.pollLast();
                        if(node.right!=null){
                            inner.add(node.right.val);
                            temp.add(node.right);
                        }
                        if(node.left!=null){
                            inner.add(node.left.val);
                            temp.add(node.left);
                        }
                    }
                }
                outer.add(inner);
            }
            queue=temp;
            count++;
        }
        return outer;
    }
}
