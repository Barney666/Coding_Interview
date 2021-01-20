#include <vector>
#include <queue>

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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> result;
        if(root != nullptr){
            queue<TreeNode*> queue;
            queue.push(root);
            TreeNode* temp_node;
            while(!queue.empty()){
                int size = queue.size();
                for(int i = 0; i < size; i++){
                    temp_node = queue.front();
                    queue.pop();
                    if(temp_node->left != nullptr)
                        queue.push(temp_node->left);
                    if(temp_node->right != nullptr)
                        queue.push(temp_node->right);
                }
                result.push_back(temp_node->val);
            }
        }
        return result;
    }
};