package SwordToOffer;

/**
 *  二叉搜索树的后序遍历序列
 *
 * */
public class Exercise23 {



    public boolean VerifySquenceOfBST(int [] sequence) {
        if(sequence.length==1)    // 记得写结束递归的条件
            return true;
        if(sequence.length==0)
            return false;
        int mid=sequence[sequence.length-1];
        int leftEnd=0;
        for(int i=0;i<sequence.length-1;i++){
            if(sequence[i]>mid){
                leftEnd=i-1;
                break;
            }
            if(i==sequence.length-2)
                leftEnd=sequence.length-2;
        }
        for(int i=leftEnd+1;i<sequence.length-1;i++)    // left不用检查了，因为上面就是这么得到的leftEnd，-1是为了避开mid
            if(sequence[i]<mid)
                return false;
        int[] leftArr=new int[leftEnd+1];
        int[] rightArr=new int[sequence.length-1-leftEnd-1];
        System.arraycopy(sequence,0,leftArr,0,leftEnd+1);     //java.lang 好像不用导包
        System.arraycopy(sequence,leftEnd+1,rightArr,0,sequence.length-1-leftEnd-1);
        boolean leftBool=(leftEnd+1>0 ? VerifySquenceOfBST(leftArr) : true);
        boolean rightBool = (sequence.length-1-leftEnd-1>0 ? VerifySquenceOfBST(rightArr):true);
        return leftBool && rightBool;
    }
}