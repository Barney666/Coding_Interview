#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int start = 0;
        int total_gas = 0;
        int cur_gas = 0;
        for(int i = 0; i < gas.size(); i++){
            int left = gas[i] - cost[i];
            total_gas += left;
            cur_gas += left;
            // 如果这步cur_gas小于0了，就把起点设为下一个加油点，因为是环线所以前面的不用管，开始为0的油都能走到这，所以起点在哪都肯定没问题
            if(cur_gas < 0){
                start = i + 1;
                cur_gas = 0;
            }
        }
        return total_gas >= 0 ? start : -1;
    }
};