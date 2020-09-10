package SwordToOffer;

import java.util.Stack;

/**
 * 反转链表
 *
 * */
public class Exercise15 {

    class ListNode {
        int val;
        ListNode next = null;

        ListNode(int val) {
            this.val = val;
        }
    }

    public ListNode ReverseList(ListNode head) {
        if(head==null)
            return null;
        Stack<ListNode> stack=new Stack();
        ListNode temp=head;
        while (temp!=null){
            stack.push(new ListNode(temp.val));     // 注意不能直接放原来的节点，因为原来的next还存在，会死锁
            temp=temp.next;
        }
        ListNode resultRoot=stack.pop();
        temp=resultRoot;
        while (!stack.empty()){
            temp.next=stack.pop();
            temp=temp.next;
        }
        return resultRoot;
    }
}
