package SwordToOffer;
/**
 * 把字符串转成整数
 * */
public class Exercise49 {

    // 这个最好记住
    int MAX=Integer.MAX_VALUE;      // 2 ^ 31 - 1 = 2147483647
    int MIN=Integer.MIN_VALUE;      // -2 ^ 31 = -2147483648

    public int normal(String str){
        int sum=0;
        for(int i=0;i<str.length();i++){
            int index=str.length()-i-1;
            char c=str.charAt(index);
            sum+=(c-'0')*Math.pow(10,i);
        }
        return sum;
    }

    public int StrToInt(String str) {

        if(str.length()==0)
            return 0;
        for(int i=0;i<str.length();i++){
            char c=str.charAt(i);
            if(!(('0'<=c && c<='9') || c=='-' || c=='+'))
                return 0;
        }

        if(str.charAt(0)=='-'){
            str=str.substring(1);
            if(str.compareTo(String.valueOf(MIN).substring(1))>0)    // 比MIN还小的置为MIN
                return MIN;
            else
                return -normal(str);
        }
        else{
            if(str.charAt(0)=='+')
                str=str.substring(1);
            if(str.compareTo(String.valueOf(MAX))>0)      // 比MAX还大的置为MAX
                return MAX;
            else
                return normal(str);
        }
    }
}
