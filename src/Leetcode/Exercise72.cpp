#include <string>

using namespace std;

class Solution {
public:
    int minDistance(string word1, string word2) {
        int row = word1.size();
        int column = word2.size();
        // dp[i][j] 代表 word1 到 i 位置转换成 word2 到 j 位置需要最少步数
        int dp[row + 1][column + 1];
        // 行和列的第一个元素都是代表空字符串，所以第一行、第一列要单独考虑
        for(int i = 0; i < column + 1; i++)
            dp[0][i] = i;
        for(int i = 0; i < row + 1; i++)
            dp[i][0] = i;
        for(int i = 1; i < row + 1; i++){            // 注意边界条件都是得+1
            for(int j = 1; j < column + 1; j++){
                if(word1[i-1] != word2[j-1])
                    // dp[i-1][j-1] 表示替换操作，dp[i-1][j] 表示删除操作，dp[i][j-1] 表示插入操作，这个很重要！
                    dp[i][j] = 1 + min(min(dp[i-1][j], dp[i-1][j-1]), dp[i][j-1]);      // 注意得加1
                else
                    dp[i][j] = dp[i-1][j-1];
            }
        }
        return dp[row][column]; 
    }
};