#include <vector>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

// 注意反转两个链表只是pre和next变了，不是调换位置那样！总想错！

class Solution {
public:
    ListNode* reverseList(ListNode* head) {         // 迭代方式：从头到尾双指针，这题很简单的，不要想太多
        if(head == NULL)
            return NULL;
        ListNode* pre = NULL;
        ListNode* cur = head;
        while (true){
            ListNode* next = cur->next;
            cur->next = pre;
            if(next != NULL){
                pre = cur;
                cur = next;
            }
            else return cur;
        }
    }

};

class Solution2 {
public:

    ListNode* return_node;

    ListNode* recursion(ListNode* node){
        // 递归到链表的最后一个结点，该结点就是反转后的头结点，然后让每次递归返回后的节点的next为当前节点，当前节点的next为NULL
        if(node->next != NULL){
            ListNode* origin_next = recursion(node->next);
            origin_next->next = node;
            node->next = NULL;
        }
        else
            return_node = node;
        return node;
    }

    ListNode* reverseList(ListNode* head) {         // 递归方式【leetcode中用递归比迭代快】
        if(head == NULL)
            return NULL;
        recursion(head);
        return return_node;
    }

};