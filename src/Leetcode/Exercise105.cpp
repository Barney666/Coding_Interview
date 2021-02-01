#include <vector>
#include <algorithm>

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
    // 前序遍历 preorder = [3,9,20,15,7]
    // 中序遍历 inorder = [9,3,15,20,7]

    // 左闭右开
    TreeNode* recursion(vector<int>& pre_order, vector<int>& in_order, int pre_left, int pre_right, int in_left, int in_right){
        if(pre_left == pre_right || in_left == in_right)            // 这里也得做处理，在vector元素小于3的时候会出现这样的情况，其他正常的在下面那个return已经避免了
            return nullptr;
        TreeNode* node = new TreeNode(pre_order[pre_left]);
        if(pre_left + 1 == pre_right || in_left + 1 == in_right)
            return node;
        auto iterator = find(in_order.begin() + in_left, in_order.begin() + in_right, node->val);       // vector查找元素，记得#include <algorithm>
        int left_num = iterator - in_order.begin() - in_left;       // 这块容易漏减in_left
        node->left = recursion(pre_order, in_order, pre_left + 1, pre_left + 1 + left_num, in_left, in_left + left_num);
        node->right = recursion(pre_order, in_order, pre_left + 1 + left_num, pre_right, in_left + 1 + left_num, in_right);
        return node;
    }

    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if(preorder.size() == 0)
            return NULL;
        return recursion(preorder, inorder, 0, preorder.size(), 0, inorder.size());
    }
};
