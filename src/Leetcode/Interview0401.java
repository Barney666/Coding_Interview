package Leetcode;


import java.util.*;

/**
 * 节点间通路
 *
 * */
public class Interview0401 {


    public boolean check(int start, int target, Map<Integer, ArrayList<Integer>> adjacent){   // DFS
        if(!adjacent.containsKey(start))
            return false;
        if(adjacent.get(start).contains(target))
            return true;
        for(int num: adjacent.get(start))
            if(check(num, target, adjacent))
                return true;
        return false;
    }


    public boolean findWhetherExistsPath(int n, int[][] graph, int start, int target) {
        Map<Integer, ArrayList<Integer>> adjacent = new HashMap();  // 邻接表，因为用邻接矩阵会爆内存我淦
        for(int[] tempArr: graph){
            int num = tempArr[0];
            ArrayList arrayList = adjacent.containsKey(num) ? adjacent.get(num) : new ArrayList<>();
            arrayList.add(tempArr[1]);
            adjacent.put(num,arrayList);
        }
        return check(start, target, adjacent);
//        Queue<Integer> queue = new LinkedList();
//        queue.add(start);
//        boolean[] visited = new boolean[n];
//        Arrays.fill(visited,false);
//        visited[start] = true;
//        while (!queue.isEmpty()){      // BFS 还超时 我淦
//            int num = queue.poll();
//            for(int i=0; i<n; i++){
//                if(visited[i]==false && adjacent.containsKey(num) && adjacent.get(num).contains(i)){
//                    if(i==target)
//                        return true;
//                    else
//                        queue.add(i);
//                }
//            }
//            visited[num] = true;
//        }
//        return false;
    }
}