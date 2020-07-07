package SwordToOffer;

import java.util.ArrayList;

/**
 *  字符流中第一个不重复的字符
 * */

public class Exercise54 {

    ArrayList<Integer> count=new ArrayList();
    ArrayList<Character> arr=new ArrayList();

    //Insert one char from stringstream
    public void Insert(char ch){
        if(arr.size()==0 || !arr.contains(ch) ){
            arr.add(ch);
            count.add(1);
        }
        else{
            int index=arr.indexOf(ch);
            count.set(index,count.get(index)+1);
        }
    }
    //return the first appearence once char in current stringstream
    public char FirstAppearingOnce(){
        for(int i=0;i<arr.size();i++){
            if(count.get(i)==1)
                return arr.get(i).charValue();
        }
        return '#';
    }
}
