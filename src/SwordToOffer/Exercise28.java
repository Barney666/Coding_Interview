package SwordToOffer;

/**
 * 数组中出现次数超过一半的数字
 *【假如数组中存在众数，那么众数一定大于数组的长度的一半；若不存在则输出0】
 *
 * 方法三：候选法（最优解）
 * 思想就是：如果两个数不相等，就消去这两个数，最坏情况下，每次消去一个众数和一个非众数，那么如果存在众数，最后留下的数肯定是众数。
 *
 * 具体做法：
 * 1.初始化：候选人cond = -1， 候选人的投票次数cnt = 0
 * 2.遍历数组，如果cnt=0， 表示没有候选人，则选取当前数为候选人，++cnt
 * 3.否则，如果cnt > 0, 表示有候选人，如果当前数=cond，则++cnt，否则--cnt
 * 4.直到数组遍历完毕，最后检查cond是否为众数
 *
 * 时间复杂度只有O(n)就很屌
 * */
public class Exercise28 {
    public int MoreThanHalfNum_Solution(int [] array) {
        int candidate=-1;
        int count=0;
        for(int num:array){
            if(count==0){
                candidate=num;
                count++;
            }
            else{
                if(num==candidate)
                    count++;
                else
                    count--;
            }
        }
        count=0;
        for(int num:array)
            if(candidate==num)
                count++;
        return (count>array.length/2 ? candidate : 0);
    }
}
