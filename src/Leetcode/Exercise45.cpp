#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    int jump(vector<int>& nums) {
        int length = nums.size();
        int temp_max = 0, cur_end= 0;
        int step = 0;
        // 在遍历数组时，我们不访问最后一个元素，这是因为在访问最后一个元素之前，我们的边界一定大于等于最后一个位置，否则就无法跳到最后一个位置了。
        for(int i = 0; i < length - 1; i++){
            if(temp_max >= i){    // 没有这个if也能过，但似乎加上更合理一些
                temp_max = max(temp_max, i + nums[i]);
                // cur_end为当前能够到达的最大下标位置，记为边界，每次到达边界就是一次step结束，一次step中是在寻找下一个能跳到的最远的位置
                // 因为这个题是要最少步骤，所以每次跳肯定选能跳最远的那个
                if(i == cur_end){
                    cur_end = temp_max;
                    step++;
                }
            }
        }
        return step;
    }
};