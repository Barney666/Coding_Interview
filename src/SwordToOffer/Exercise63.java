package SwordToOffer;

import java.util.Comparator;
import java.util.PriorityQueue;

/**
 * 数据流中的中位数
 *
 * 如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
 * 如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
 * 我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。
 *
 * 解析: 【一开始没想到】
 * 中位数是指：有序数组中中间的那个数。则根据中位数可以把数组分为如下三段:
 * [0 ... median - 1], [median], [median ... arr.size() - 1]，即[中位数的左边，中位数，中位数的右边]
 *
 * 那么，如果我有个数据结构保留[0...median-1]的数据，并且可以O(1)时间取出最大值，即arr[0...median-1]中的最大值
 * 相对应的，如果我有个数据结构可以保留[median + 1 ... arr.size() - 1] 的数据， 并且可以O(1)时间取出最小值，即
 * arr[median + 1 ... arr.size() - 1] 中的最小值。
 * 然后，我们把[median]即中位数，随便放到哪个都可以。
 *
 * 假设[0 ... median - 1]的长度为l_len, [median + 1 ... arr.sise() - 1]的长度为 r_len.
 * 1.如果l_len == r_len + 1, 说明，中位数是左边数据结构的最大值
 * 2.如果l_len + 1 == r_len, 说明，中位数是右边数据结构的最小值
 * 3.如果l_len == r_len, 说明，中位数是左边数据结构的最大值与右边数据结构的最小值的平均值。
 *
 * 说了这么多，一个数据结构可以O(1)返回最小值的，其实就是小根堆，O(1)返回最大值的，其实就是大根堆。并且每次插入到堆中的时间复杂度为O(logn)
 * */
public class Exercise63 {
    int record=0;
    PriorityQueue<Integer> left=new PriorityQueue(new Comparator<Integer>() {    // 重写compare实现大顶堆
        @Override
        public int compare(Integer o1, Integer o2) {
            return o2-o1;
        }
    });
    PriorityQueue<Integer> right=new PriorityQueue();    // 优先队列<-->小顶堆

    public void Insert(Integer num) {
        if((record&1)==0){   // 用&应该是比%要快
            left.add(num);  // 这里其实包括堆空的情况 都一样
            right.add(left.poll());   // 平衡两个堆
        }
        else{
            right.add(num);
            left.add(right.poll());
        }
        record++;
    }

    public Double GetMedian() {
        if((record&1)==0){
            return (left.peek()+right.peek())/2.0;
        }
        else{
            return (double)right.peek();   // 注意别写成Double 对象间没法变
        }
    }
}
