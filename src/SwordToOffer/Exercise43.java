package SwordToOffer;

/**
 * 左移字符串
 *
 * */
public class Exercise43 {
    public String LeftRotateString(String str,int n) {
        if(str.length()==0)
            return str;
        int num=n%(str.length());
        String front=str.substring(0,num);
        return str.substring(num)+front;
    }
}
