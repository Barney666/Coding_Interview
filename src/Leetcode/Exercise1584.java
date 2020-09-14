package Leetcode;

import java.util.Arrays;

/**
 * 连接所有点的最小费用
 *【其实就是最小生成树，用Prim即可，反正我是觉得Prim比Kruskal更好用】
 *
 * */
public class Exercise1584 {
    public int minCostConnectPoints(int[][] points) {
        int n=points.length;
        int[][] cost = new int[n][n];
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(i==j)
                    cost[i][j]=0;
                else
                    cost[i][j]=Math.abs(points[i][0]-points[j][0])+Math.abs(points[i][1]-points[j][1]);
            }
        }
        int[] lowestCost = new int[n];    // 数据结构ppt上还用了个nearVex数组，不懂有啥用，一个数组就能解决的事
        int currentPointNum=1;
        Arrays.fill(lowestCost,Integer.MAX_VALUE);
        for(int i=0;i<n;i++)
            lowestCost[i]=cost[0][i];
        int result=0;
        while(currentPointNum<n){
            int tempMin=Integer.MAX_VALUE;
            int tempPos=-1;
            for(int i=0;i<n;i++){
                int tempCost=lowestCost[i];
                if(tempCost!=0 && tempCost<tempMin){
                    tempMin=tempCost;
                    tempPos=i;
                }
            }
            currentPointNum++;
            result+=tempMin;
            lowestCost[tempPos]=0;
            for(int i=0;i<n;i++){
                if(cost[tempPos][i]<lowestCost[i])
                    lowestCost[i]=cost[tempPos][i];
            }
        }
        return result;
    }
}
