package Leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

/**
 * 全排列2
 *
 * */
public class Exercise47 {
    List<List<Integer>> result = new ArrayList<>();

    public void recursion(ArrayList<Integer> cur, ArrayList<Integer> left){
        if(left.size()==0)
            result.add(cur);
        else{
            ArrayList<Integer> record=new ArrayList<>();
            for(int i=0;i<left.size();i++){
                int num=left.get(i);
                if(record.indexOf(num)==-1){
                    ArrayList<Integer> copyLeft=(ArrayList<Integer>)left.clone();
                    ArrayList<Integer> copycur=(ArrayList<Integer>)cur.clone();
                    record.add(num);
                    copycur.add(num);
                    copyLeft.remove(i);
                    recursion(copycur,copyLeft);
                }
            }
        }
    }

    public List<List<Integer>> permuteUnique(int[] nums) {
        ArrayList<Integer> arrayList=(ArrayList<Integer>) Arrays.stream(nums).boxed().collect(Collectors.toList());
        Collections.sort(arrayList);
        recursion(new ArrayList<Integer>(), arrayList);
        return result;
    }
}
