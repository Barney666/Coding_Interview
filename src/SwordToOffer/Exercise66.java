package SwordToOffer;

import java.util.Arrays;

/**
 * 机器人的运动范围
 * */

//要记住走过的 这才是最终结束的判断条件：前后左右都走过了
public class Exercise66 {

    int[][] arr;
    int result;

    public boolean check(int row,int col,int limit){
        //走过的false
        if(row>=arr.length || col>=arr[0].length || row<0 || col<0)
            return false;
        if(arr[row][col]!=-1)
            return false;
        //超过限制的false
        int temp=0;
        String rowStr=String.valueOf(row);
        String colStr=String.valueOf(col);
        for(int i=0;i<rowStr.length();i++){
            char c=rowStr.charAt(i);
            temp+=(c-'0');
        }
        for(int i=0;i<colStr.length();i++){
            char c=colStr.charAt(i);
            temp+=(c-'0');
        }
        if(temp>limit)
            return false;
        else{
            //增加result && 改变arr
            result+=1;
            arr[row][col]=temp;
            return true;
        }
    }

    public void dfs(int row,int col,int limit){
        if(row==0 && col==0 && limit>=0){
            result+=1;
            arr[0][0]=0;
        }
        if(check(row,col+1,limit)){
            dfs(row,col+1,limit);
        }
        if(check(row+1,col,limit)){
            dfs(row+1,col,limit);
        }
        if(check(row,col-1,limit)){
            dfs(row,col-1,limit);
        }
        if(check(row-1,col,limit)){
            dfs(row-1,col,limit);
        }
    }

    public int movingCount(int threshold, int rows, int cols){
        arr=new int[rows][cols];    //因为有0的存在 多出来一行一列
        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                arr[i][j]=-1;
            }
        }
        result=0;
        dfs(0,0,threshold);
        System.out.println(result);
        return result;
    }
}
