package SwordToOffer;

/**
 *
 * */
public class Exercise16 {

    class ListNode {
        int val;
        ListNode next = null;

        ListNode(int val) {
            this.val = val;
        }
    }

    public ListNode Merge(ListNode list1,ListNode list2) {
        ListNode point1=list1;
        ListNode point2=list2;
        ListNode resultRoot=null;
        ListNode temp=resultRoot;
        while (point1!=null && point2!=null){
            if(point1.val<point2.val){
                if(temp==null){
                    resultRoot=new ListNode(point1.val);
                    temp=resultRoot;
                }
                else{
                    temp.next=new ListNode(point1.val);
                    temp=temp.next;
                }
                point1=point1.next;
            }
            else{
                if(temp==null){
                    resultRoot=new ListNode(point2.val);
                    temp=resultRoot;
                }
                else{
                    temp.next=new ListNode(point2.val);
                    temp=temp.next;
                }
                point2=point2.next;
            }
        }
        if(point1!=null && point2==null){
            while (point1!=null){
                if(temp==null){
                    resultRoot=new ListNode(point1.val);
                    temp=resultRoot;
                }
                else{
                    temp.next=new ListNode(point1.val);
                    temp=temp.next;
                }
                point1=point1.next;
            }
        }
        else if(point1==null && point2!=null){
            while (point2!=null){
                if(temp==null){
                    resultRoot=new ListNode(point2.val);
                    temp=resultRoot;
                }
                else{
                    temp.next=new ListNode(point2.val);
                    temp=temp.next;
                }
                point2=point2.next;
            }
        }
        return resultRoot;
    }
}