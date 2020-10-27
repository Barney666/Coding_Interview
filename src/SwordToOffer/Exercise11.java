package SwordToOffer;

/**
 * 32bits二进制中1的个数
 *
 *【除2取模：对于-2147483648,二进制为1000...000，输出0，实际上为1，因此不行】
 *【二进制移位法：对于负数>>移位最高位会补1，因此还是有问题】
 *
 *【因此，让一个数0x01从右向左与val的每一位进行&操作来判断】
 *【但此时有一个无用操作是，如果当前位是0，还是会做判断，然后一位一位的移动，
 * 所以用n&(n-1)，一下可以对从右向左的第一位1直接判断，效率更快
 * Eg:  val 1101000，val-1 1100111，那么val &（val-1） 1100000，这样一个1就没了，count++ 】
 *
 * */
public class Exercise11 {
    public int NumberOf1(int n) {
        int count=0;
        while (n!=0){
            count++;
            n = n & (n-1);
        }
        return count;
    }
}