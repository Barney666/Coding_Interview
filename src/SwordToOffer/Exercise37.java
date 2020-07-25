package SwordToOffer;

/**
 * 数字在排序数组中出现的次数
 * */
public class Exercise37 {
    public int GetNumberOfK(int [] array , int k) {
        if(array.length==0)
            return 0;
        if(array.length==1)
            return array[0]==k ? 1 : 0;
        int left=0;
        int right=array.length-1;
        int result=0;
        while(left<right){    // 好久不写二分法了 注意一下细节 这里没有等号
            int mid=left+(right-left)/2;     // 这里要用加差值的方法 不能直接(left+right)/2
            int num=array[mid];
            if(num<k)
                left=mid+1;
            else if(num>k)
                right=mid;
            else{
                result++;
                for(int i=mid-1;i>=0;i--){
                    if(array[i]==k)
                        result++;
                }
                for(int i=mid+1;i<array.length;i++){
                    if(array[i]==k)
                        result++;
                }
                break;
            }
        }
        return result;
    }
}