#include <iostream>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int result = INT_MIN;       // 注意是INT_MIN，不能是0

    int maxPathSum(TreeNode* root) {
        recursion(root);
        return result;
    }

    int recursion(TreeNode* node){
        if(node == nullptr)
            return 0;
        int left_sum = max(recursion(node->left), 0);       // 只有子节点贡献值大于0时才选用
        int right_sum = max(recursion(node->right), 0);
        int cur_sum = node->val + left_sum + right_sum;
        result = max(result, cur_sum);
        return node->val + max(left_sum, right_sum);        // 对于上层节点来说只能选择一条路
    }
};