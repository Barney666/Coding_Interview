package SwordToOffer;

import java.util.Arrays;

/**
 * 数组中只出现一次的数字
 *
 * */
public class Exercise40 {
    public void FindNumsAppearOnce(int [] array,int num1[] , int num2[]) {
        Arrays.sort(array);
        for(int i=0;i<array.length;i++){
            if(i==array.length-1 || array[i]!=array[i+1]){
                if(num1[0]==0)     // 注意整数数组都会初始化为0，所以不能用num1.length==0
                    num1[0]=array[i];
                else
                    num2[0]=array[i];
            }
            else
                i++;   // 也就是i+=2
        }
    }
}