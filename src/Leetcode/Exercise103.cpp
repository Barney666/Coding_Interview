#include <vector>
#include <queue>
#include <deque>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {        // 其实也可以直接BFS，最后把奇数位的反转一下就行了
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> result;
        if(root == NULL)
            return result;
        queue<TreeNode*> every_layer;           // 看每层的时候用队列
        every_layer.push(root);
        int record = 0;
        while (every_layer.size() != 0){
            deque<int> one_layer;                   // 每层最后到底怎么加，用双向队列
            int layer_size = every_layer.size();
            for(int i = 0; i < layer_size; i++){
                TreeNode* temp = every_layer.front();
                if(temp->left != NULL)
                    every_layer.push(temp->left);
                if(temp->right != NULL)
                    every_layer.push(temp->right);
                every_layer.pop();
                if(record % 2 == 0)
                    one_layer.push_back(temp->val);
                else
                    one_layer.push_front(temp->val);
            }
            result.emplace_back(vector<int>{one_layer.begin(), one_layer.end()});   // 还能这样构造vector的，我人傻了
            record++;
        }
        return result;
    }
};