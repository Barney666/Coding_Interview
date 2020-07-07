package SwordToOffer;

/**
 * 链表中环的入口结点
 *【思路挺巧的 就不用再开一个数组或者map了 降低了空间复杂度】
 *
 * 1. 初始化：快指针fast指向头结点， 慢指针slow指向头结点
 * 2. 让fast一次走两步， slow一次走一步，第一次相遇停止
 * 3. 然后让fast指向头结点，slow原地不动，让后fast，slow每次走一步，❗️当再次相遇，就是入口结点❗️
 * */
public class Exercise55 {
    class ListNode {
        int val;
        ListNode next = null;

        ListNode(int val) {
            this.val = val;
        }
    }

    public ListNode EntryNodeOfLoop(ListNode pHead){
        ListNode fast=pHead;
        ListNode slow=pHead;
        while(true){
            if(slow.next==null || fast.next.next==null)
                return null;
            fast=fast.next.next;
            slow=slow.next;
            if(fast.val==slow.val)
                break;
        }
        fast=pHead;
        while(fast.val!=slow.val){
            fast=fast.next;
            slow=slow.next;
        }
        return fast;
    }
}
