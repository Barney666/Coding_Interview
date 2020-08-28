package SwordToOffer;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

/**
 * 最小的k个数
 *
 * */
public class Exercise29 {

    List<Integer> list;

    public void QuickSort(int begin,int end){
        if(begin<end){
            int pivot=list.get(begin);
            int frontPoint=begin;   // 不是begin+1
            int behindPoint=end;
            boolean isRight=true;   // 判断这次是看右边还是左边
            while (frontPoint<behindPoint){
                int front=list.get(frontPoint);
                int behind=list.get(behindPoint);
                if(isRight){
                    if(behind<pivot){
                        list.set(frontPoint,behind);
                        isRight=false;
                    }
                    else
                        behindPoint--;     // 只有不交换才移动
                }
                else{
                    if(front>pivot){
                        list.set(behindPoint,front);
                        isRight=true;
                    }
                    else
                        frontPoint++;     // 只有不交换才移动
                }
            }
            list.set(frontPoint,pivot);    // 这里左右指针重合
            QuickSort(begin,frontPoint-1);
            QuickSort(frontPoint+1,end);
        }
    }

    public ArrayList<Integer> GetLeastNumbers_Solution(int [] input, int k) {
        if(k>input.length)
            return new ArrayList<>();
        list = Arrays.stream(input).boxed().collect(Collectors.toList());  // int[]变成list
        QuickSort(0,list.size()-1);
        ArrayList<Integer> result=new ArrayList<>(k);
        for(int i=0;i<k;i++)
            result.add(list.get(i));
        return result;
    }
}
