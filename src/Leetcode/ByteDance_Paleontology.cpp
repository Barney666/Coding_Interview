/**
 * 古生物血缘远近判定【其实就是Leetcode72编辑距离】
 *
 * DNA 是由 ACGT 四种核苷酸组成，例如 AAAGTCTGAC，假定自然环境下 DNA 发生异变的情况有：
 * 1. 基因缺失一个核苷酸
 * 2. 基因新增一个核苷酸
 * 3. 基因替换一个核苷酸
 * 且发生概率相同。
 * 古生物学家 Sam 得到了若干条相似 DNA 序列，Sam 认为一个 DNA 序列向另外一个 DNA 序列转变所需的最小异变情况数可以代表其物种血缘相近程度，异变情况数越少，血缘越相近，
 * 请帮助 Sam 实现获取两条 DNA 序列的最小异变情况数的算法。
 * 输入描述:
 * 每个样例只有一行，两个 DNA 序列字符串以英文逗号“,”分割
 * 输出描述:
 * 输出转变所需的最少情况数，类型是数字
 * 测试用例:
 * 输入
 * ACT,AGCT
 * 输出
 * 1
 * 数据范围：
 * 每个 DNA 序列不超过 100 个字符
 * */

#include <iostream>
#include <string>

using namespace std;

int main(){
    string input_word;
    cin >> input_word;
    int pos = input_word.find(',');
    string word1 = input_word.substr(0, pos);
    string word2 = input_word.substr(pos+1, input_word.size());
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
    cout << dp[row][column];
}