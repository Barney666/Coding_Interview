package SwordToOffer;

import java.util.Arrays;

/**
 * 扑克牌顺子
 *
 * */
public class Exercise45 {
    public boolean isContinuous(int [] numbers) {
        if(numbers.length==0) return false;
        Arrays.sort(numbers);     // java也有！用的是快排
        int replace=0;
        int first=-1;
        int firstIndex=-1;
        for(int i=0;i<numbers.length;i++){
            int num=numbers[i];
            if(num==0)
                replace+=1;
            else{
                if(first==-1){
                    first=num;
                    firstIndex=i;
                }
                else{
                    if(num==numbers[i-1]) return false;   // 只要有重复的肯定就不行了
                    if(i-firstIndex!=num-first)
                        if(replace>0)
                            replace-=(num-numbers[i-1]-1);   // 减去和前一个数字相差的大小
                        else
                            return false;
                }
            }
        }
        return replace<0 ? false : true;
    }
}