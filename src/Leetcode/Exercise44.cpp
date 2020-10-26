#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
        int s_length = s.size();
        int p_length = p.size();
        bool dp[s_length+1][p_length+1];    // dp[i][j]表示字符串s的前i个字符能否与模式p前j个字符相匹配
        //注意是前i个和前j个，不是index为i/j，因此后面在s/p上用i/j时要减1
        memset(dp, false, sizeof(dp));    // dp[i][0]为false，dp[0][j]只要不是p[j]*就是false
        // memset是对连续空间赋值，所以只能用于直接定义的二维数组,因为[][]这样定义内存是连续的，嵌套一维那种定义就要定义一次一维memset一次
        dp[0][0] = true;
        int index = 1;
        while (index < p_length+1 && p[index-1] == '*'){  // 因为星号才能匹配空字符串，所以只有当p的前j个字符均为*时，dp[0][j]才为真
            dp[0][index] = true;
            index++;
        }
        for(int i = 1; i < s_length + 1; i++){
            for(int j = 1; j < p_length + 1; j++){
                if(s[i-1]==p[j-1] || p[j-1]=='?')
                    dp[i][j] = dp[i-1][j-1];
                else if(p[j-1] == '*')
                    dp[i][j] = (dp[i-1][j] || dp[i][j-1]);
            }
        }
        return dp[s_length][p_length];
    }
};