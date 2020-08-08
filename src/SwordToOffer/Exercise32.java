package SwordToOffer;

/**
 * 把数组排成最小的数
 *
 * 先排序，然后串起来，排序的关键：
 * 比较两个字符串s1, s2大小的时候，先将它们拼接起来，比较s1+s2,和s2+s1那个大，
 * 如果s1+s2大，那说明s2应该放前面，所以按这个规则，s2就应该排在s1前面。
 */

public class Exercise32 {

    public boolean compare(String str1,String str2){
        Integer num1=Integer.valueOf(str1+str2);
        Integer num2=Integer.valueOf(str2+str1);
        return num1<num2 ? true : false;
//        return num1<num2 ? str1 : str2;
    }

    public String PrintMinNumber(int [] numbers) {
        for(int i=0;i<numbers.length;i++){
            for(int j=i+1;j<numbers.length;j++){
                if(compare(String.valueOf(numbers[i]),String.valueOf(numbers[j]))==false){
                    int temp=numbers[i];
                    numbers[i]=numbers[j];
                    numbers[j]=temp;
                }
            }
        }
        String result="";
        for(int num:numbers)
            result+=String.valueOf(num);
        return result;
    }
}
