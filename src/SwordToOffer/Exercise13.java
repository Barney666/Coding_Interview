package SwordToOffer;

import java.util.ArrayList;

/**
 * 调整数组顺序使奇数位于偶数前面
 *
 * */
public class Exercise13 {

    public void reOrderArray(int [] array) {
        ArrayList<Integer> resultList=new ArrayList();
        for(int num:array)
            if(num%2==1)
                resultList.add(num);
        for(int num:array)
            if(num%2==0)
                resultList.add(num);
        array=resultList.stream().mapToInt(Integer::intValue).toArray();    // ArrayList<Integer>变成int[]
    }
}