#include <vector>

using namespace std;


class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        int dp[n][5];
        dp[0][0] = 0;
        dp[0][1] = -prices[0];
        dp[0][2] = 0;
        // 卖出的操作一定是收获利润，整个股票买卖最差情况也就是没有盈利即全程无操作现金为0，从递推公式中可以看出每次是取最大值，那么既然是收获利润如果比0还小了就没有必要收获这个利润了。
        dp[0][3] = -prices[0];
        dp[0][4] = 0;
        for(int i = 1; i < n; i++){
            dp[i][0] = dp[i-1][0];                                  // 不做任何操作
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i]);     // 第一次买入
            // dp[i][1]，表示的是第i天，买入股票的状态，并不是说一定要第i天买入股票
            dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i]);     // 第一次卖出
            dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i]);     // 第二次买入
            dp[i][4] = max(dp[i-1][4], dp[i-1][3] + prices[i]);     // 第二次卖出
        }
        return dp[n-1][4];      // 全部交易结束后，持有股票的收益一定低于不持有股票的收益
    }
};

