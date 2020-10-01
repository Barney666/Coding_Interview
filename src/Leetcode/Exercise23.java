package Leetcode;

import SwordToOffer.Exercise16;

/**
 * 合并k个升序链表
 *
 * */

public class Exercise23 {
    class ListNode {
        int val;
        ListNode next;

        ListNode() {
        }

        ListNode(int val) {
            this.val = val;
        }

        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
    }

    public  ListNode merge(ListNode list1,  ListNode list2) {
        ListNode point1=list1;
        ListNode point2=list2;
        ListNode resultRoot=null;
        ListNode temp=resultRoot;
        while (point1!=null && point2!=null){
            if(point1.val<point2.val){
                if(temp==null){
                    resultRoot=new  ListNode(point1.val);
                    temp=resultRoot;
                }
                else{
                    temp.next=new  ListNode(point1.val);
                    temp=temp.next;
                }
                point1=point1.next;
            }
            else{
                if(temp==null){
                    resultRoot=new  ListNode(point2.val);
                    temp=resultRoot;
                }
                else{
                    temp.next=new  ListNode(point2.val);
                    temp=temp.next;
                }
                point2=point2.next;
            }
        }
        if(point1!=null && point2==null){
            while (point1!=null){
                if(temp==null){
                    resultRoot=new  ListNode(point1.val);
                    temp=resultRoot;
                }
                else{
                    temp.next=new  ListNode(point1.val);
                    temp=temp.next;
                }
                point1=point1.next;
            }
        }
        else if(point1==null && point2!=null){
            while (point2!=null){
                if(temp==null){
                    resultRoot=new  ListNode(point2.val);
                    temp=resultRoot;
                }
                else{
                    temp.next=new  ListNode(point2.val);
                    temp=temp.next;
                }
                point2=point2.next;
            }
        }
        return resultRoot;
    }

    public ListNode mergeKLists(ListNode[] lists) {
        if(lists.length==0)
            return null;
        if(lists.length==1)
            return lists[0];
        ListNode temp=merge(lists[0],lists[1]);
        for(int i=2;i<lists.length;i++){
            temp=merge(temp,lists[i]);
        }
        return temp;
    }
}
