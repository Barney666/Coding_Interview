package Leetcode;

import java.util.HashSet;
import java.util.Set;

/**
 * 最长连续序列
 *【思路好牛逼orz】
 *
 * */

public class Exercise128 {

    public int find(int num, Set<Integer> set){
        return set.contains(num) ? find(num+1,set) : num;
    }

    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet();   // 先用一下set是为了去重
        for(int num: nums)
            set.add(num);
        int count=0;
        for(int num: nums){
            if(!set.contains(num-1)){  // 若有更小的不用看，因为遍历一次肯定会轮到它
                count = Math.max(count, find(num+1, set) - num);
                // 这里正常看有几个数应该find()-num+1的，但find返回的时候已经是存在的最大数+1了，所以这里就不用+1了
            }
        }
        return count;
    }

}
