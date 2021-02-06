#include <vector>
#include <numeric>

using namespace std;

class Solution {
public:
    int shoppingOffers(vector<int>& price, vector<vector<int>>& special, vector<int>& needs) {
        int result = inner_product(price.begin(), price.end(), needs.begin(), 0);       // 初值为0，计算price与needs的内积，每个都单买的最大值

        for(vector<int> combination: special){
            // 其实这里有挺多重复计算的，可以用vector<int> needs作为key，result作为value，整一个map，保留每次的计算结果，但我觉得有点der
            vector<int> next_need(needs.size());
            bool available = true;
            for(int i = 0; i < combination.size() - 1; i++){
                if(combination[i] > needs[i]){
                    available = false;
                    break;
                }
                else
                    next_need[i] = needs[i] - combination[i];
            }
            if(available)       // 递归解决后面的
                result = min(result, combination[combination.size()-1] + shoppingOffers(price, special, next_need));
        }

        return result;
    }
};