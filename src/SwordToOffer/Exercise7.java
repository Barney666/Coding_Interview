package SwordToOffer;

/**
 * 斐波那契数列
 *
 * */
public class Exercise7 {
    public int Fibonacci(int n) {
        if(n==0)
            return 0;
        if(n==1)
            return 1;
        int[] record=new int[n+1];
        record[0]=0;
        record[1]=1;
        for(int i=2;i<n+1;i++)
            record[i]=record[i-1]+record[i-2];
        return record[n];
    }
}