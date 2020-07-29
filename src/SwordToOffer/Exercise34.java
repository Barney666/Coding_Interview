package SwordToOffer;

/**
 * 第一个只出现一次的字符
 * */
public class Exercise34 {
    public int FirstNotRepeatingChar(String str) {
        if(str==null || str.length()==0)
            return -1;
        int[] arr=new int[128];
        for(int i=0;i<str.length();i++)
            arr[str.charAt(i)]++;
        for(int i=0;i<str.length();i++)
            if(arr[str.charAt(i)]==1)     // 这一步很屌 不是从头看arr 而是再从头看str 这样就能找到第一个出现的了
                return i;
        return -1;
    }
}
