#include <vector>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min_price = INT32_MAX;
        int max_diff = 0;           // 注意这块是0，不然为prices空的时候会有问题
        for(int num: prices){
            min_price = min(min_price, num);
            max_diff = max(max_diff, num - min_price);
        }
        return max_diff;
    }
};

