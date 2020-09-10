package SwordToOffer;

import java.util.Stack;

/**
 * 用两个栈实现队列
 *
 * */
public class Exercise5 {
    Stack<Integer> stack1 = new Stack<Integer>();
    Stack<Integer> stack2 = new Stack<Integer>();

    public void push(int node) {
        stack1.push(node);
    }

    public int pop() {
        while (true){
            int num=stack1.pop();
            if(stack1.empty()){
                while (!stack2.empty())
                    stack1.push(stack2.pop());
                return num;
            }
            else stack2.push(num);
        }
    }
}
