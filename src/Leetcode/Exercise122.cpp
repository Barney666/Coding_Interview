#include <vector>

using namespace std;

/**
 * dp[i][0]表示表示第i天交易完后手里没有股票的最大利润，dp[i][1]表示表示第i天交易完后手里持有股票的最大利润
 *
 * 对于dp[i][0]，如果这一天交易完后手里没有股票，
 * 那么可能的转移状态为前一天已经没有股票，或者前一天结束的时候手里持有一支股票，这时候我们要将其卖出。
 *
 * 对于dp[i][1]，如果这一天交易完后手里持有股票，
 * 那么可能的转移状态为前一天已经持有一支股票，或者前一天结束时还没有股票，这时候我们要将其买入。
 *
 * */


class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        int dp[n][2];
        dp[0][0] = 0;
        dp[0][1] = -prices[0];
        for(int i = 1; i < n; i++){
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i]);
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i]);
        }
        return dp[n-1][0];      // 全部交易结束后，持有股票的收益一定低于不持有股票的收益
    }
};

