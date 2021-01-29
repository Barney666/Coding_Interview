#include <vector>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

// 用快慢指针的方式，慢指针一边遍历一遍翻转，当快指针遍历到末尾的时候，慢指针刚好遍历到一半，然后向前和向后对比就能判断是否为回文。

class Solution {
public:
    bool isPalindrome(ListNode* head) {
        if(head == NULL || head->next == NULL)
            return true;        // 没有或单个也是回文
        ListNode* slow = head;
        ListNode* fast = head;
        ListNode* pre = nullptr;
        ListNode* next = nullptr;
        while (fast != NULL && fast->next != NULL){
            fast = fast->next->next;
            next = slow->next;      // 注意这里得有个记录next的，容易漏
            slow->next = pre;
            pre = slow;
            slow = next;
        }
        if(fast != NULL)        // 奇数情况
            slow = slow->next;
        while (pre != NULL && slow != NULL){
            if(pre->val != slow->val)
                return false;
            pre = pre->next;
            slow = slow->next;
        }
        return true;
    }
};