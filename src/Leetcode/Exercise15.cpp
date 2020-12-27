#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        if(nums.size() < 3)    // 若数组长度小于3，返回空
            return result;
        sort(nums.begin(), nums.end());    // 对数组进行排序，默认是升序
        int index = 0;
        while (index < nums.size()){
            if(nums[index] > 0)      // 因为已经排序好，所以后面不可能有三个数加和等于0，直接返回
                return result;
            int left_point = index + 1;
            int right_point = nums.size() - 1;
            while (left_point < right_point){
                int sum = nums[index] + nums[left_point] + nums[right_point];
                if(sum > 0)             //若和大于0，说明nums[right_ponint]太大
                    right_point--;
                else if(sum < 0)        //若和小于0，说明nums[left_ponint]太小
                    left_point++;
                else{
                    vector<int> item;
                    item.push_back(nums[index]);
                    item.push_back(nums[left_point]);
                    item.push_back(nums[right_point]);
                    result.push_back(item);
                    while (left_point < right_point && nums[left_point] == nums[left_point+1])      // 避免重复的
                        left_point++;
                    while (left_point < right_point && nums[right_point-1] == nums[right_point])    // 避免重复的
                        right_point--;
                    left_point++;
                    right_point--;
                }
            }
            while (index + 1 < nums.size() && nums[index] == nums[index+1])    // 对于重复元素，跳过
                index++;
            index++;
        }
        return result;
    }
};