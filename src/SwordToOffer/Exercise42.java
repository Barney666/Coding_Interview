package SwordToOffer;

import java.util.ArrayList;

/**
 * 和为sum的两个数
 *【题目说array是递增数列，如有多对和为sum的数字，要乘积最小的两个】
 * 双指针思路！！！
 * 而且 最外面两个一定是乘积最小的！！！（虽然我也不知道为啥）
 * 这两个点很重要！
 * */
public class Exercise42 {
    public ArrayList<Integer> FindNumbersWithSum(int [] array, int sum) {
        ArrayList<Integer> result=new ArrayList();
        int front=0;
        int behind=array.length-1;
        while(front<behind){
            int tempSum=array[front]+array[behind];
            if(tempSum==sum){
                result.add(array[front]);
                result.add(array[behind]);
                return result;
            }
            else if(tempSum<sum)
                front+=1;
            else
                behind-=1;
        }
        return result;
    }
}
