package SwordToOffer;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

/**
 * 把二叉树打印成多行【从上到下】
 * 其实也没让print 就是一个BFS的过程
 * */

public class Exercise60 {

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
        Queue<TreeNode> queue=null;
        // 用队列！我一开始只能想到再开一个数组记录 然后用index递归 但那其实还是dfs 用队列就是真的bfs了
        while(true){
            if(queue!=null && queue.size()==0){
                outer.remove(outer.size()-1);    //最后会多出一个空的 把它删掉
                break;
            }
            ArrayList<Integer> inner=new ArrayList();
            Queue<TreeNode> temp=new LinkedList();
            if(queue==null){
                inner.add(pRoot.val);
                outer.add(inner);
                temp.add(pRoot);
            }
            else{
                for(TreeNode node:queue){
                    if(node.left!=null){
                        inner.add(node.left.val);
                        temp.add(node.left);
                    }
                    if(node.right!=null){
                        inner.add(node.right.val);
                        temp.add(node.right);
                    }
                }
                outer.add(inner);
            }
            queue=temp;
        }
        return outer;
    }
}