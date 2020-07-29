package SwordToOffer;

/**
 * 从小到大第N个丑数（只包含质因子2、3和5的数）
 *【思路挺巧的，复习时候可以看一哈】
 * */
public class Exercise33 {
    public int GetUglyNumber_Solution(int index) {
        if(index==0)    // 这什么脑瘫用例 就硬恶心人
            return 0;
        int[] result=new int[index];
        result[0]=1;
        // 3个指针只负责用来乘2/3/5，这一步很关键
        int p_2=0;
        int p_3=0;
        int p_5=0;
        for(int i=1;i<result.length;i++){
            int temp_2=result[p_2]*2;
            int temp_3=result[p_3]*3;
            int temp_5=result[p_5]*5;
            result[i]=Math.min(temp_2, Math.min(temp_3, temp_5) );      // Math.min()只能两个数
            // 三个都要走一遍 防止有重复的
            if(result[i]==temp_2)
                p_2++;
            if(result[i]==temp_3)
                p_3++;
            if(result[i]==temp_5)
                p_5++;
        }
        return result[index-1];
    }
}
