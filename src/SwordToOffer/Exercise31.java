package SwordToOffer;

/**
 * 整数中1出现的次数
 * https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof/solution/mian-shi-ti-43-1n-zheng-shu-zhong-1-chu-xian-de-2/】
 * 很牛逼的解法 不会真的有人不看答案也能想到吧
 * */
public class Exercise31 {
    public int NumberOf1Between1AndN_Solution(int n) {
        int digit = 1, result = 0;
        int high = n / 10, cur = n % 10, low = 0;
        while (high!=0 || cur!=0){
            switch (cur){
                case 0:
                    result+=(high*digit);
                    break;
                case 1:
                    result+=(high*digit+low+1);
                    break;
                default:
                    result+=(high+1)*digit;
                    break;
            }
            low+=(cur*digit);
            cur=high%10;
            high/=10;
            digit*=10;
        }
        return result;
    }
}
