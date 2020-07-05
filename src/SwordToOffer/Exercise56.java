package SwordToOffer;

/**
 * 删除链表中重复的结点
 *【已经排序好的链表 重复的结点不保留】
 *【小问题挺多的 复习时好好看一下】
 * */

public class Exercise56 {
     class ListNode {
        int val;
        ListNode next = null;

        ListNode(int val) {
            this.val = val;
        }
    }

    public ListNode deleteDuplication(ListNode pHead){
        if(pHead == null || pHead.next == null){
            return pHead;
        }
        // 借助辅助头结点，可避免单独讨论头结点的情况。如{1,1,1,1,2}
        ListNode head = new ListNode(Integer.MIN_VALUE);
        head.next = pHead;
        // 设置两个结点pre和cur，当cur和cur.next值相等，cur一直向前走，直到不等退出循环，
        // 这时候 cur 指的值还是重复值，调整cur和pre的指针再次判断
        ListNode pre = head;
        ListNode cur = head.next;
        while(cur!=null){
            if(cur.next != null && cur.next.val == cur.val){
                // 相同结点一直前进
                while(cur.next != null && cur.next.val == cur.val){
                    cur = cur.next;
                }
                // 退出循环时，cur 指向重复值，也需要删除，而 cur.next 指向第一个不重复的值
                // cur 继续前进
                cur = cur.next;
                // pre 连接新结点 【⚠️注意这块是不动pre的 只是改变pre.next 所以即使{1,2,3,3,4,4,4,5}也不会出现4 】
                pre.next = cur;
            }else{
                pre = cur;
                cur = cur.next;
            }
        }
        return head.next;
    }
}
