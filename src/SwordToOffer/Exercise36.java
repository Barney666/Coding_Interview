package SwordToOffer;

/**
 * 两个链表的第一个公共结点
 *【让长的先走这个思路很关键！！！】
 *
 * 可以先遍历两个链表得到他们的长度，就能知道哪个链表比较长，以及长的链表比短的链表多几个结点。
 * 在第二次遍历的时候，在较长的链表上先走若干步，接着同时在两个链表上遍历，找到的第一个相同的结点就是他们的第一个公共结点。
 * 时间复杂度为O(m+n)
 * */
public class Exercise36 {
     class ListNode {
        int val;
        ListNode next = null;

        ListNode(int val) {
            this.val = val;
        }
    }

    public ListNode FindFirstCommonNode(ListNode pHead1, ListNode pHead2) {
        if(pHead1==null || pHead2==null)
            return null;

        int length1=1;
        int length2=1;

        ListNode temp=pHead1;
        while (temp.next!=null){
            temp=temp.next;
            length1++;
        }
        temp=pHead2;
        while (temp.next!=null){
            temp=temp.next;
            length2++;
        }

        ListNode temp1=pHead1;
        ListNode temp2=pHead2;

        if(length1>length2)
            for (int i=length1-length2;i>0;i--)
                temp1=temp1.next;
        else
            for (int i=length2-length1;i>0;i--)
                temp2=temp2.next;

        while (temp1.val!=temp2.val){
            temp1=temp1.next;
            temp2=temp2.next;
            if(temp1==null || temp2==null)    // 防止没有公共结点的
                return null;
        }

        return temp1;
    }
}