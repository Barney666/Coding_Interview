package SwordToOffer;

import java.util.Arrays;

/**
 * 构建乘机数组 【不能使用除法！】
 *
 * B[i] = A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]
 * 规定：B[0] = A[1] * A[2] * ... * A[n-1]  ,  B[n-1] = A[0] * A[1] * ... * A[n-2];
 *
 * 下面这个思路很重要！
 *  left[i] = A[0]*A[1]*...*A[i-1]
 *  right[i] = A[i+1]*...*A[n-1]
 *  因此
 *      left[i+1] = left[i] * A[i]
 *      right[i] = right[i+1] * A[i+1]
 *  且
 *      B[0]=right[0]
 *      B[n-1]=left[n-1]
 *
 * */
public class Exercise51 {
    public int[] multiply(int[] A) {
        int[] B=new int[A.length];
        Arrays.fill(B,1);    // 这步也很关键 使得left[1]可以直接用公式
        for(int i=1;i<B.length;i++){
            B[i]=B[i-1]*A[i-1];   // left[i]用B[i]代替
        }
        int tempRight=1;    // right[n-1]没有 就为1
        for(int i=B.length-2;i>=0;i--){
            tempRight*=A[i+1];
            B[i]*=tempRight;
        }
        return B;
    }
}
