package SwordToOffer;

/**
 * 矩阵中的路径
 * */

/**
 * 这里先给出一个我认为比较清晰的DFS模板：
 *
 * dfs(){
 *
 *     // 第一步，检查下标是否满足条件
 *
 *     // 第二步：检查是否被访问过，或者是否满足当前匹配条件
 *
 *     // 第三步：检查是否满足返回结果条件
 *
 *     // 第四步：都没有返回，说明应该进行下一步递归
 *     // 标记
 *     dfs(下一次)
 *     // 回溯
 * }
 *
 * main() {
 *     for (对所有可能情况) {
 *         dfs()
 *     }
 * }
 * */
public class Exercise65 {

    int[][] arr;
    char[] string;

    public boolean dfs(int x,int y,boolean[][] record,int nowChar){
        if(nowChar>=string.length){
            return true;
        }
        if(x<0 || y<0 || x>=arr.length || y>=arr[0].length)
            return false;
        if(record[x][y]==true)
            return false;
        if(arr[x][y]==string[nowChar]){
            nowChar++;
            record[x][y]=true;
            return dfs(x,y+1,record,nowChar) || dfs(x+1,y,record,nowChar) ||
                    dfs(x,y-1,record,nowChar) || dfs(x-1,y,record,nowChar);
        }
        return false;

    }

    public boolean hasPath(char[] matrix, int rows, int cols, char[] str){
        arr=new int[rows][cols];
        string=str;
        for(int i=0;i<arr.length;i++){
            for(int j=0;j<arr[0].length;j++){
                arr[i][j]=matrix[i*arr[0].length+j];
            }
        }
        int x=0;
        int y=0;
        for(int i=0;i<arr.length;i++){
            for(int j=0;j<arr[0].length;j++){
                boolean[][] record=new boolean[rows][cols];    //记录是否走过
                for(int p=0;p<record.length;p++){
                    for(int q=0;q<record[0].length;q++){
                        record[p][q]=false;
                    }
                }
                if(dfs(i,j,record,0))
                    return true;
            }
        }
        return false;
    }
}

