package SwordToOffer;

import java.util.ArrayList;
import java.util.Stack;

/**
 * 从尾到头打印链表
 *
 * */
public class Exercise03 {

    class ListNode {
        int val;
        ListNode next = null;
        ListNode(int val) {
          this.val = val;
        }
    }

    public ArrayList<Integer> printListFromTailToHead(ListNode listNode) {
        if(listNode==null)
            return new ArrayList<>();
        Stack<Integer> stack=new Stack<>();
        ListNode temp=listNode;
        while (true){
            stack.push(temp.val);
            temp=temp.next;
            if(temp==null)
                break;
        }
        ArrayList<Integer> result=new ArrayList<>();
        while (!stack.empty())
            result.add(stack.pop());
        return result;
    }
}
