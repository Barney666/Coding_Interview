package SwordToOffer;

import java.util.Stack;

/**
 * 链表中倒数第k个节点
 *
 * */
public class Exercise14 {

    class ListNode {
        int val;
        ListNode next = null;

        ListNode(int val) {
            this.val = val;
        }
    }

    public ListNode FindKthToTail(ListNode head,int k) {
        if(head==null || k==0)
            return null;
        Stack<ListNode> stack=new Stack();
        ListNode temp=head;
        while (temp!=null){
            stack.push(temp);
            temp=temp.next;
        }
        if(k>stack.size())
            return null;
        for(int i=0;i<k-1;i++)
            stack.pop();
        return stack.peek();
    }
}
