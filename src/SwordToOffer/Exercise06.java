package SwordToOffer;


/**
 * 旋转数组的最小数字【不能用暴力方法，用二分法】
 *【这里二分法去和谁比较很有讲究，挺坑的这题】
 *
 * */
public class Exercise06 {
    public int minNumberInRotateArray(int [] array) {
        int low=0, high=array.length-1;
        int mid;
        while (low<high){
            mid=(low+high)/2;
            if(array[low]<array[high])    // 坑点10111。因为数组是非递减的因此这样可以写
                return array[low];
            else{
                if(array[low]<array[mid])
                    low=mid+1;
                else if(array[mid]<array[high])
                    high=mid;   // 如果是mid-1，则可能会错过最小值，因为找的就是最小值
                else low++;
            }
        }
        return array[low];
    }
}