package SwordToOffer;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;

/**
 *  滑动窗口的最大值
 *
 * 【我一开始只想到暴力解法，看了解析以后再写的】
 *
 * 解析：
 * 暴力接解法存在很多大量重复计算，比如说，对于数组，假设我们当前遍历到下标i，对于下标i+1的元素（假设i和i+1都在同一个窗口）
 * 如果arr[i+1] 已经大于了 arr[i], 那么还要arr[i]有什么用.就有点“既生瑜何生亮”的感觉。
 * 如果arr[i+1] < arr[i]呢？显然arr[i]还是需要保留的。为什么呢？
 * 因为又可以arr[i] 对于下一个arr[i+1]所在的窗口来说，arr[i]已经失效了。
 *
 * 假设这里有那么一个容器可以保留上述操作。
 *
 * 遍历数组的每一个元素，
 * 如果容器为空，则直接将当前元素加入到容器中。
 * 如果容器不为空，则让当前元素和容器的最后一个元素比较，如果大于，则将容器的最后一个元素删除，然后继续讲当前元素和容器的最后一个元素比较
 * 如果当前元素小于容器的最后一个元素，则直接将当前元素加入到容器的末尾
 * 如果容器头部的元素已经不属于当前窗口的边界，则应该将头部元素删除
 * 总结一下，首先容器中放的元素应该是单调递减的。然后还有删除容器头部元素和最后一个元素的操作。因此，这样的数据结构就是双端队列。c++中就是deque
 *
 * 如何判断队列中头部的元素是否过期呢？
 * 这里我们可以存数组的下标，根据下标的比较来判断。比如，当前遍历到下标为5的元素，窗口的大小为3， 显然显然下标为2的已经过期了。
 *
 * ArrayDeque:
 *     boolean add(E e)	在此deque的末尾插入指定的元素。
 *     void addFirst(E e)	在此deque前面插入指定的元素。
 *     void addLast(E e)	在此deque的末尾插入指定的元素。。
 *     boolean contains(Object o)	如果此deque包含指定的元素，则返回 true 。
 *     Iterator descendingIterator()	以相反的顺序返回此deque中的元素的迭代器。
 *     E getFirst()	检索，但不删除，这个deque的第一个元素。
 *     E getLast()	检索，但不删除，这个deque的最后一个元素。
 *     boolean isEmpty()	如果此deque不包含元素，则返回 true 。
 *     Iterator iterator()	返回此deque中的元素的迭代器。
 *     E peekFirst()	检索但不删除此deque的第一个元素，如果此deque为空，则返回 null 。
 *     E peekLast()	检索但不删除此deque的最后一个元素，或返回 null如果此deque为空）。
 *     E pollFirst()	检索并删除此deque的第一个元素，如果此deque为空，则返回 null 。
 *     E pollLast()	检索并删除此deque的最后一个元素，如果此deque为空，则返回 null 。
 *     boolean remove(Object o)	从此deque中删除指定元素的单个实例。
 *     boolean removeFirstOccurrence(Object o)	删除此deque中指定元素的第一个出现（从头到尾遍历deque时）。
 *     boolean removeLastOccurrence(Object o)	删除此deque中指定元素的最后一次（从头到尾遍历deque时）。
 *     int size()	返回此deque中的元素数。
 *     Object[] toArray()	以适当的顺序返回一个包含此deque中所有元素的数组（从第一个到最后一个元素）。
 *
 * BTW：
 *      queue队列
 *      deque双端队列
 *      dequeue出列
 *
 * */

public class Exercise64 {
    public ArrayList<Integer> maxInWindows(int [] num, int size){
        ArrayList<Integer> arr=new ArrayList();
        int n=num.length;
        if (n == 0 || size < 1 || n < size)     // 不要懒得写！！！真的有这种脑瘫用例
            return arr;
        ArrayDeque<Integer> arrayDeque=new ArrayDeque();    //双端队列
        for(int i=0;i<n;i++){
            while(!arrayDeque.isEmpty() && num[i]>num[arrayDeque.getLast()]){   // 把更小的都去掉
                arrayDeque.pollLast();
            }
            arrayDeque.addLast(i);
            // 判断队列的头部的下标是否过期(是否还属于当前窗口)
            if(arrayDeque.getFirst()+size<=i)
                arrayDeque.pollFirst();
            // 判断是否已经形成了一个完整窗口
            if(i+1>=size)   // 这个很屌 因为只要大于size每一次都是一个完整窗口
                arr.add(num[arrayDeque.getFirst()]);
        }
        return arr;
    }
}
