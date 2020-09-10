package SwordToOffer;

/**
 * 变态跳台阶【这名字就nm离谱】
 *【可以跳任意阶】
 * */
public class Exercise9 {
    public int JumpFloorII(int target) {
        return (int)Math.pow(2,target-1);   // target-1的情况每个都+1，即一直乘2
    }
}