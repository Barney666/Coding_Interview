package SwordToOffer;

import java.util.Arrays;

/**
 * 剪绳子
 * */
public class Exercise67 {
    public class Solution {
        int[] arr;     // 我想到了递归 但还可以优化 开一个数组保留已经计算过的数 这样会节省很多时间

        public int recursion(int num){
            switch(num){
                case 4:
                    return 4;
                case 3:
                    return 3;
                case 2:
                    return 2;
                case 1:
                    return 1;
                default:
                    int max=-1;
                    for(int i=1;i<num/2+1;i++){
                        int anotherMax;
                        if(arr[num-i]==-1){
                            anotherMax=recursion(num-i);
                            arr[num-i]=anotherMax;
                        }
                        else
                            anotherMax=arr[num-i];
                        int tempResult=anotherMax*i;
                        if(tempResult > max)
                            max=tempResult;
                    }
                    return max;
            }
        }

        public int cutRope(int target) {
            arr=new int[target];
            Arrays.fill(arr,-1);
            int result=recursion(target);
            return result;
        }
    }
}
