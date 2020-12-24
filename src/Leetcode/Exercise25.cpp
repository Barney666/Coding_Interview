#include <utility>    // pair在这个头文件里，实在不行就include<unordered_map>
#include <tuple>      // 用tie应该是得include这个

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};


class Solution {   //链表对象可能空间复杂度不是O(1)，但链表指针应该就是O(1)了
public:
    pair<ListNode*, ListNode*> real_reverse(ListNode* head, ListNode* tail){
        ListNode* cur = head->next;
        ListNode* before = head;
        while (before != tail){
            ListNode* next = cur->next;
            cur->next = before;
            before = cur;
            cur = next;
        }
        return {tail, head};
    }

    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode* before_head = new ListNode();      // 这里如果不用new会有问题
        before_head->next = head;
        ListNode* pre_node = before_head;
        while (head){
            ListNode* tail_node = pre_node;
            for(int i = 0; i < k; i++){         // 检查是否继续翻转
                tail_node = tail_node->next;
                if(!tail_node)
                    return before_head->next;
            }
            ListNode* next_node = tail_node->next;
            tie(head, tail_node) = real_reverse(head, tail_node);     // std::tie
            pre_node->next = head;
            tail_node->next = next_node;
            pre_node = tail_node;
            head = next_node;
        }
        return before_head->next;
    }
};