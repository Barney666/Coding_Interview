package SwordToOffer;

/**
 * 特殊二维数组的查找
 *
 * 矩阵是有序的，从左下角来看，向上数字递减，向右数字递增，因此从左下角开始查找，
 * 当要查找数字比左下角数字大时，右移。要查找数字比左下角数字小时，上移。
 *
 * 这思路真的nm巧
 * */
public class Exercise01 {
    public boolean Find(int target, int [][] array) {
        int i=array.length-1;
        int j=0;
        while (i>=0 && j<array[0].length){
            int num=array[i][j];
            if(target<num)
                i--;
            else if(target>num)
                j++;
            else
                return true;
        }
        return false;
    }
}
