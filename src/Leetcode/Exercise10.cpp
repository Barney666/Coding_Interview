#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
        int s_length = s.size();
        int p_length = p.size();

        auto match = [](char c1, char c2){    // 借助lambda构造函数,[]表示未定义任何变量，[&]表示用到任何的外部变量都隐式按引用捕获
            return c2=='.' || c1==c2;
        };

        bool dp[s_length+1][p_length+1];    // dp[i][j]表示字符串s的前i个字符能否与模式p前j个字符相匹配
        // 注意是前i个和前j个，不是index为i/j，因此后面在s/p上用i/j时要减1
        memset(dp, false, sizeof(dp));    // 默认false
        // memset是对连续空间赋值，所以只能用于直接定义的二维数组,因为[][]这样定义内存是连续的，嵌套一维那种定义就要定义一次一维memset一次
        dp[0][0] = true;
        int index = 1;
        while (index < p_length+1){      // 只可能是右端是星号，它干掉一个字符后，把p变为空串
            if(p[index-1] == '*'){
                if(index == 1)
                    dp[0][index] = true;
                else
                    dp[0][index] = dp[0][index-2];
            }
            index++;
        }
        for(int i = 1; i < s_length + 1; i++){
            for(int j = 1; j < p_length + 1; j++){
                if(match(s[i-1], p[j-1]))
                    dp[i][j] = dp[i-1][j-1];
                else if(p[j-1] == '*'){
                    if(match(s[i-1], p[j-2]))     // 有机会是'*'造成重复的情况
                        dp[i][j] = dp[i][j-2] || dp[i][j-1] || dp[i-1][j];   // 没有匹配 || 单个字符匹配 || 多个字符匹配
                    else
                        dp[i][j] = dp[i][j-2];    // 没有匹配，p[j-1]的'*'把p[j-2]干没了
                        // 这块不能和上面合起来，不然上面一旦有true即使这个表达式为false，也会是true了
                }
            }
        }
        return dp[s_length][p_length];
    }
};