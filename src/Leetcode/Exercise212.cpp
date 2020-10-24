#include <string>
#include <vector>
#include <set>
//#include "Exercise208.cpp"

using namespace std;

class TrieNode{
public:
    string word = "";
    vector<TrieNode*> children;
    TrieNode():children(26, 0){}     // 初始化列表
};

class Solution {
public:
    int length;
    int width;
    vector<string> result;

    void dfs(int i, int j, TrieNode* node, vector<vector<char>>& board){
        char c = board[i][j];
        if(c == ' ' || node->children[c-'a']==0)        // 一个char只能用一次
            return;
        node = node->children[c-'a'];
        if(node->word != ""){
            result.push_back(node->word);
            node->word = "";     // 这个单词已经发现了，删掉，防止重复！
        }
        // 这里不能用else，因为可能出现一个单词是另一个单词的前缀情况，不能提前结束递归。
        board[i][j] = ' ';      // 剪枝
        if(i != 0)
            dfs(i-1, j, node, board);
        if(j != 0)
            dfs(i, j-1, node, board);
        if(i != length-1)
            dfs(i+1, j, node, board);
        if(j != width-1)
            dfs(i, j+1, node, board);
        board[i][j] = c;     // 递归前先剪枝，递归后恢复，不影响后面的
    }

    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        length = board.size();
        width = board[0].size();
        TrieNode* root = new TrieNode();
        for(string word: words){
            TrieNode *cur = root;
            for(int i = 0; i < word.size();  i++){
                int index = word[i] - 'a';
                if(cur->children[index]==0)
                    cur->children[index] = new TrieNode();
                cur = cur->children[index];
            }
            cur->word = word;     // 可以节省一个递归时的参数，此题用这个比设置isEnd更好一些
        }

        for(int i = 0; i < length; i++){     // vector.size()
            for(int j = 0; j < width; j++){
                dfs(i, j, root, board);
            }
        }
        return result;
    }
};

//int main(){
//    vector<vector<char>> board = {{'a','b'},{'a','a'}};
//    vector<string> words = {"aba","baa","bab","aaab","aaa","aaaa","aaba"};
//    Solution solution;
//    solution.findWords(board, words);
//    return 0;
//}