package SwordToOffer;

/**
 * 矩形覆盖
 *【这个挺离谱的，可以找到规律然后用dp】
 * 从n=3到n=4：
 *            直接在n=3的情况下，再后面中添加一个竖着的。这个很显然成立，有3种情况
 *            然后横着的显然能添加到n-2的情况上，也就是在n=2后面，添加2个横着的。有2种情况
 *
 * */
public class Exercise10 {
    public int RectCover(int target) {
        if(target==0)
            return 0;
        if(target==1)
            return 1;
        int[] result=new int[target];
        result[0]=1;
        result[1]=2;
        for(int i=2;i<target;i++)
            result[i]=result[i-2]+result[i-1];
        return result[-1];
    }
}
