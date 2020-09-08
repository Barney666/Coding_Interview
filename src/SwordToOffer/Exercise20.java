package SwordToOffer;

import java.util.ArrayList;
import java.util.Stack;

/**
 * 定义一个包含min函数的栈【min函数时间复杂度为o(1)】
 *【双栈法，有点屌】
 *
 * */
public class Exercise20 {

    Stack<Integer> stack=new Stack();
    Stack<Integer> minStack=new Stack();

    public void push(int node) {
        stack.push(node);
        if(minStack.empty())
            minStack.push(node);
        else{
            int min=minStack.peek();
            if(node<=min)
                minStack.push(node);
            else{
                ArrayList<Integer> temp=new ArrayList();
                int count=0;
                while (true){
                    if(node>minStack.peek())
                        temp.add(minStack.pop());
                    else
                        break;
                    count++;
                    if(count>=temp.size())
                        break;
                }
                minStack.push(node);
                for(int i=temp.size()-1;i>=0;i--)
                    minStack.push(temp.get(i));
            }
        }
    }

    public void pop() {
        int top=stack.pop();
        ArrayList<Integer> temp=new ArrayList();
        while (!minStack.empty()){
            if(minStack.peek()<top)
                temp.add(minStack.pop());
            if(minStack.peek()==top){
                minStack.pop();
                for(int i=temp.size()-1;i>=0;i--)
                    minStack.push(temp.get(i));
                break;
            }
        }
    }

    public int top() {
        return stack.peek();
    }

    public int min() {
        return minStack.peek();
    }
}