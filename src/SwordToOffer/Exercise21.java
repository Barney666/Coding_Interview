package SwordToOffer;

import java.util.Stack;

/**
 *  栈的压入、弹出序列
 * 【非常屌的思路：新建一个栈，将数组A压入栈中，当栈顶元素等于数组B时，就将其出栈，当循环结束时，判断栈是否为空，若为空则返回true】
 * */
public class Exercise21 {
    
    public boolean IsPopOrder(int [] pushA,int [] popA) {
        int popPoint=0;
        Stack<Integer> stack=new Stack();
        for(int i=0;i<pushA.length;i++){
            stack.push(pushA[i]);
            if(pushA[i]==popA[popPoint]){
                stack.pop();
                popPoint++;
            }
        }
        for(;popPoint<popA.length;popPoint++){
            if(stack.peek()==popA[popPoint])
                stack.pop();
            else
                return false;
        }
        if(stack.empty())
            return true;
        else
            return false;
    }
}