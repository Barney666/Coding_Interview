package SwordToOffer;

/**
 * 翻转单词顺序列
 *
 * */
public class Exercise44 {
    public String ReverseSentence(String str) {
        String[] arr=str.split(" ");
        if(arr.length==0)
            return str;
        StringBuffer sb=new StringBuffer();
        if(str.length()==1)
            return str;
        for(int i=arr.length-1;i>=0;i--){
            String temp=arr[i];
            sb.append(temp);
            if(i!=0)
                sb.append(" ");
        }
        return sb.toString();
    }
}