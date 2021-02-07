#include <vector>

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
    int index = 0;          // 一开始没想出左侧遍历完怎么定位右侧在voyage第几个，全局变量就行了
    vector<int> result;

    bool dfs(TreeNode* node, vector<int>& voyage){
        if(node == nullptr || index >= voyage.size())
            return true;
        if(node->val != voyage[index])
            return false;
        index++;
        if(node->left != nullptr && node->left->val != voyage[index]){      // 若先序遍历结果与预期不符，则尝试返回交换后的遍历结果
            result.push_back(node->val);
            return dfs(node->right, voyage) && dfs(node->left, voyage);
        }
        else return dfs(node->left, voyage) && dfs(node->right, voyage);
    }

    vector<int> flipMatchVoyage(TreeNode* root, vector<int>& voyage) {
        if(dfs(root, voyage))
            return result;
        else return vector<int>{-1};
    }
};