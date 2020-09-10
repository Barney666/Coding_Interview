package SwordToOffer;

/**
 * 跳台阶【只能跳1阶或2阶】
 *
 * */
public class Exercise08 {

    public int JumpFloor(int target) {
        if(target==1)
            return 1;
        if(target==2)
            return 2;
        int[] record=new int[target];
        record[0]=1;
        record[1]=2;
        for(int i=2;i<target;i++)
            record[i]=record[i-2]+record[i-1];
        return record[target-1];
    }
}