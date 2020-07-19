package SwordToOffer;

/**
 * 求1+2+...+n
 * 要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句
 *
 * ！！！！！有、东西
 * 把递归方法中判断递归结束的if(n == 1) return n; 换成别的，就可以了。
 * 也就是说如果n==1,需要终止递归，所以我们想到了逻辑与&&连接符。
 * A&&B，表示如果A成立则执行B，否则如果A不成立，不用执行B
 * 因此我们可以这样。在n>1的时候，执行递归函数。
 * */
public class Exercise47 {
    public int Sum_Solution(int n) {
        boolean x = n>1 && (n+=Sum_Solution(n-1))>1;     // 重点在 n>1 && (n+=Sum_Solution(n-1) 剩下的都是为了不报错
        return n;
    }
}
