#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int length = nums.size();
        int temp_max = 0;
        // 依次遍历数组中的每一个位置，并实时维护最远可以到达的位置。
        // 对于当前遍历到的位置x，如果它在最远可以到达的位置的范围内，那么我们就可以从起点通过若干次跳跃到达该位置，
        // 因此我们可以用x+nums[x] 更新最远可以到达的位置
        for(int i = 0; i < length; i++){
            int num = nums[i];
            if(i > temp_max)
                continue;
            int cur_max = i + num;
            if(cur_max > temp_max)
                temp_max = cur_max;
            if(temp_max >= length-1)
                return true;
        }
        return false;
    }
};