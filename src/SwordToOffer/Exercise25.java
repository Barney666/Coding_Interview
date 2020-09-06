package SwordToOffer;

import java.util.HashMap;

/**
 * 复杂链表的复制
 *【注意：next有可能无法遍历完所有的结点，比如有的结点的random连接的是并没有在next链中出现的结点。 1->2->3->4->null 5->6】
 *【用map存新旧节点，而不是random的两个节点这个很重要！】
 *
 * */
public class Exercise25 {
    class RandomListNode {
        int label;
        RandomListNode next = null;
        RandomListNode random = null;

        RandomListNode(int label) {
            this.label = label;
        }
    }

    public RandomListNode Clone(RandomListNode pHead){
        RandomListNode cur=pHead;

        HashMap<RandomListNode,RandomListNode> hashMap=new HashMap<>();
        while (cur!=null){
            hashMap.put(cur,new RandomListNode(cur.label));
            cur=cur.next;
        }

        cur=pHead;

        while (cur!=null){
            if(cur.next!=null)
                hashMap.get(cur).next=hashMap.get(cur.next);
            if(cur.random!=null)
                hashMap.get(cur).random=hashMap.get(cur.random);
            cur=cur.next;
        }
        return hashMap.get(pHead);
    }
}