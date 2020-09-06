package SwordToOffer;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

/**
 * 二叉树中和为某一值的路径
 *
 * */
public class Exercise24 {
    class TreeNode {
        int val = 0;
        TreeNode left = null;
        TreeNode right = null;

        public TreeNode(int val) {
            this.val = val;
        }
    }

    ArrayList<ArrayList<Integer>> result=new ArrayList<>();

    public void recursion(ArrayList<Integer> arrayList, int diff, TreeNode node){
        arrayList.add(node.val);
        diff-=node.val;
        if(diff==0 && node.left==null && node.right==null)      // 还必须到叶节点 这也太简单了md
            result.add(arrayList);
        if(node.left!=null)     // 这块不知道为啥递归不能直接用arraylist，会修改别的递归中的arraylist，就离谱
            recursion((ArrayList<Integer>) arrayList.clone(),diff,node.left);
        if(node.right!=null)
            recursion((ArrayList<Integer>) arrayList.clone(),diff,node.right);
    }

    public ArrayList<ArrayList<Integer>> FindPath(TreeNode root, int target) {
        if(root==null)
            return new ArrayList<>();
        recursion(new ArrayList<>(),target,root);
        Collections.sort(result, new Comparator<ArrayList<Integer>>() {
            @Override
            public int compare(ArrayList<Integer> o1, ArrayList<Integer> o2) {
                for(int i=0;i<o1.size();i++){    // 返回正数，零，负数各代表大于，等于，小于
                    if(o1.get(i)==null && o2.get(i)!=null)
                        return -1;
                    if(o1.get(i)!=null && o2.get(i)==null)
                        return 1;
                    if(o1.get(i)<o2.get(i))
                        return -1;
                    else if(o1.get(i)>o2.get(i))
                        return 1;
                }
                return 0;
            }
        });
        return result;
    }
}
