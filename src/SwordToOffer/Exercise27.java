package SwordToOffer;

import java.util.ArrayList;
import java.util.Collections;

/**
 * 字符串的排列
 *
 * 原理：
 * 以"ABC"为例：
 * 固定A不动，然后交换B与C，从而得到"ABC" 和 "ACB"
 * 同理，对于"BAC"、"BCA" 、"CAB"和"CBA"是同样道理
 * */
public class Exercise27 {

    public ArrayList<String> Recursion(StringBuilder stringBuilder){
        ArrayList<String> result=new ArrayList<>();
        if(stringBuilder.length()==1)
            result.add(stringBuilder.toString());
        else{
            for(int i=0;i<stringBuilder.length();i++){
                // 进行交换的时候需要判断进行交换的字符是否相等，如果相等就没有必要交换了。
                if(i==0 || stringBuilder.charAt(i)!=stringBuilder.charAt(0)){
                    char temp=stringBuilder.charAt(i);    // 交换二者 把要固定的放到第一个
                    stringBuilder.setCharAt(i,stringBuilder.charAt(0));
                    stringBuilder.setCharAt(0,temp);
                    // 把后面的进行递归交换
                    ArrayList<String> tempResult=Recursion(new StringBuilder(stringBuilder.substring(1)));
                    for(int j=0;j<tempResult.size();j++)
                        result.add(stringBuilder.substring(0,1)+tempResult.get(j));  // 用sub(0,1)比charAt(0)舒服
                    // 交换完要换回来 因为比如第二次交换后是"BAC"，需要回溯到"ABC"，才能进行第三次交换，才能得到"CBA"
                    stringBuilder.setCharAt(0,stringBuilder.charAt(i));
                    stringBuilder.setCharAt(i,temp);
                }
            }
        }
        Collections.sort(result);   // 排个序
        return result;
    }

    public ArrayList<String> Permutation(String str) {
        StringBuilder stringBuilder=new StringBuilder(str);
        ArrayList<String> result= Recursion(stringBuilder);
        return result;
    }
}