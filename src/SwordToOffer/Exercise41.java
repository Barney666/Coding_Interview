package SwordToOffer;

import java.util.ArrayList;

/**
 * 和为sum的连续正序列
 *【就是滑动窗口没有错】
 * */
public class Exercise41 {
    public ArrayList<ArrayList<Integer>> FindContinuousSequence(int sum) {
        ArrayList<ArrayList<Integer>> result=new ArrayList<>();
        int left=1;
        int right=1;
        int temp=0;
        while (left<=sum/2){     // 因为要连续序列，所以至少两个数，因此在left到达sum一半的时候就可以停了
            if(temp<sum){
                temp+=right;    // 注意窗口是左闭右开的！！！
                right+=1;
            }
            else if(temp>sum){
                temp-=left;
                left+=1;
            }
            else{
                ArrayList<Integer> arrayList=new ArrayList<>();
                for(int i=left;i<right;i++)
                    arrayList.add(i);
                result.add(arrayList);
                temp-=left;
                left+=1;
                temp+=right;
                right+=1;
            }
        }
        return result;
    }
}