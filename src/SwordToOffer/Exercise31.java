package SwordToOffer;

/**
 * 整数中1出现的次数
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
