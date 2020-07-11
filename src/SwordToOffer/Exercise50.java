package SwordToOffer;

/**
 * 找出数组中重复的数字
 *【in-place算法！很巧！比哈希+Set节省空间！】
 *
 * 用哈希中时有一个条件我们没有用到，也就是数据的范围是0-n-1。
 * 所以我们可以这么做：
 *
 * 设置一个指针i指向开头0，对于arr[i]进行判断，如果arr[i] == i， 说明下标为i的数据正确的放在了该位置上，让i++
 * 如果arr[i] != i, 说明没有正确放在位置上，那么我们就把arr[i]放在正确的位置上，也就是交换
 * arr[i] 和arr[arr[i]]。交换之后，如果arr[i] ！= i, 继续交换。
 * 如果交换的过程中，arr[i] == arr[arr[i]]，说明遇到了重复值，返回即可
 *
 * 我之前肯定是在哪看见过这个算法 但忘记是哪了 淦
 * 我清楚的记得说这个每次一定会有一个数字被放到正确位置 所以我for用的length/2
 *
 * */

public class Exercise50 {
    public boolean duplicate(int numbers[],int length,int [] duplication) {
        if(length==0)
            return false;
        for(int i=0;i<length/2;i++){    // 每一次至少有一个成功放置
            while(numbers[i]!=i){
                if(numbers[numbers[i]]==numbers[i]){
                    duplication[0]=numbers[i];
                    return true;
                }
                int temp=numbers[numbers[i]];
                numbers[numbers[i]]=numbers[i];
                numbers[i]=temp;
            }
        }
        return false;
    }
}
