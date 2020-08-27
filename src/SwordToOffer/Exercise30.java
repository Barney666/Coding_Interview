package SwordToOffer;

/**
 *  连续子数组的最大和
 *
 *  dp[i] = max(array[i], dp[i-1]+array[i])
 *
 * */
public class Exercise30 {
    public int FindGreatestSumOfSubArray(int[] array) {
        int result=Integer.MIN_VALUE;
        int[] dp=new int[array.length];
        dp[0]=array[0];
        for(int i=1;i<array.length;i++){
            dp[i]=Math.max(array[i],dp[i-1]+array[i]);
            if(dp[i]>result)
                result=dp[i];
        }
        return result;
    }
}
