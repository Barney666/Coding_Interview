package SwordToOffer;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

/**
 * 重建二叉树
 *
 * */
public class Exercise04 {

    class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    public TreeNode recursion(List<Integer> preArr, List<Integer> inArr){   // 我爱递归，根本不需要脑子就能写出来
        if(preArr.size()==0 || inArr.size()==0)
            return null;
        int tempRootVal=preArr.get(0);
        for(int i=0;i<inArr.size();i++){
            if(inArr.get(i)==tempRootVal){
                TreeNode tempRoot=new TreeNode(tempRootVal);
                tempRoot.left=recursion(preArr.subList(1,i+1),inArr.subList(0,i));
                tempRoot.right=recursion(preArr.subList(i+1,preArr.size()),inArr.subList(i+1,inArr.size()));
                return tempRoot;
            }
        }
        return null;
    }

    public TreeNode reConstructBinaryTree(int [] pre,int [] in) {
        List preArr = Arrays.stream(pre).boxed().collect(Collectors.toList());
        List inArr = Arrays.stream(in).boxed().collect(Collectors.toList());
        return recursion(preArr,inArr);
    }

}