package SwordToOffer;

import java.util.ArrayList;

/**
 * 顺时针打印矩形
 *
 * */
public class Exercise19 {
    public ArrayList<Integer> printMatrix(int [][] matrix) {
        int length = matrix[0].length, width = matrix.length;
        int lt_l = 0, lt_t = 0;
        int rt_r = length-1, rt_t = 0;
        int lb_l = 0, lb_b = width-1;
        int rb_r = length-1, rb_b = width-1;
        int count = 0;
        ArrayList result = new ArrayList();
        while (count < (length*width)){
            for(int i = lt_l ; i <= rt_r ; i++, count++)
                result.add(matrix[lt_t][i]);
            for(int i = rt_t+1 ; i <= rb_b ; i++, count++)
                result.add(matrix[i][rt_r]);
            if(count >= (length*width))    // 防止只有一行或一列的，因为这样在横着和竖着加完了一遍后已经全都add了
                break;
            for(int i = rb_r-1 ; i >= lb_l; i--, count++)
                result.add(matrix[rb_b][i]);
            for(int i = lb_b-1 ; i >= lt_t+1 ; i--, count++)
                result.add(matrix[i][lb_l]);
            lt_l++;
            lt_t++;
            rt_r--;
            rt_t++;
            lb_l++;
            lb_b--;
            rb_r--;
            rb_b--;
        }
        return result;
    }
}