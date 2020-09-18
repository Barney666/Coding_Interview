package Leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

/**
 * 全排列
 *
 * */
public class Exercise46 {

    List<List<Integer>> result = new ArrayList<>();

    public void recursion(ArrayList<Integer> cur, ArrayList<Integer> left){
        if(left.size()==0)
            result.add(cur);
        else{
            for(int i=0;i<left.size();i++){
                ArrayList<Integer> copyLeft=(ArrayList<Integer>)left.clone();
                ArrayList<Integer> copycur=(ArrayList<Integer>)cur.clone();
                copycur.add(left.get(i));
                copyLeft.remove(i);    // 他怎么知道是index还是object？？？万一index也有object也有呢
                recursion(copycur,copyLeft);
            }
        }
    }

    public List<List<Integer>> permute(int[] nums) {
        recursion(new ArrayList<Integer>(), (ArrayList<Integer>) Arrays.stream(nums).boxed().collect(Collectors.toList()));
        return result;
    }
}