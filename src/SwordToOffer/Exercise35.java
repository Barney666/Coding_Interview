package SwordToOffer;

/**
 * 数组中逆序对
 *【用归并排序！！！很屌】
 * 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
 * 输入一个数组,求出这个数组中的逆序对的总数P，并将P对1000000007取模的结果输出
 *
 * punchline：
 *     合并时候当left元素大于right元素时，由于此时left和right都是增序排列的，所以left剩余元素也一定都大于right的这个元素
 * */
public class Exercise35 {

    int mod=1000000007;
    int result=0;

    public int InversePairs(int [] array) {
        mergeSort(array,0,array.length-1);
        return result;

    }

    public void mergeSort(int[] array, int left, int right){   // 归并排序
        if(left>=right)
            return;
        int mid=(left+right)/2;      // 用>>1更加装杯
        // 先分解
        mergeSort(array,left,mid);
        mergeSort(array,mid+1,right);
        // 合并
        combine(array,left,mid,right);
    }

    // 虽然java只有值传递，但对于引用类型只要不改变形参指向，形参还是会影响实参的，放心用
    public void combine(int[] array, int left, int mid, int right){
        int leftTemp=left;     // 要合并两个数组左侧那个的index
        int rightTemp=mid+1;   // 要合并两个数组右侧那个的index

        int[] tempResult=new int[right-left+1];
        int index=0;     // tempResult的index

        while (leftTemp<=mid && rightTemp<=right){  // 每次取两个合并数组中更小的一个
            if(array[leftTemp]>array[rightTemp]){
                result+=(mid-leftTemp+1);    // 这道题用归并排序的punchline
                result%=mod;     // 一定要每一次都mod，不能加完最后一起mod，这样数多的时候会溢出！
                tempResult[index++]=array[rightTemp++];
            }
            else
                tempResult[index++]=array[leftTemp++];
        }
        while (leftTemp<=mid){    // 另一个完事了，但这个还没完事的话，都加进去
            tempResult[index++]=array[leftTemp++];  // 因为是递归的，所以单独某一个数组内部肯定是已经排好序的，不用担心
        }
        while (rightTemp<=right){    // 同理
            tempResult[index++]=array[rightTemp++];
        }

        for(int i=0;i<tempResult.length;i++)
            array[left+i]=tempResult[i];
    }

}