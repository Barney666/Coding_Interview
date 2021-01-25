#include <iostream>
#include <vector>

using namespace std;


class Solution {
public:
    int trap(vector<int>& height) {
        /* 动态规划 */
//        if(height.size() == 0)
//            return 0;
//        int size = height.size();
//        int left_max[size];
//        int right_max[size];
//        // 注意这个题左右是没有边界的，所以第一个和最后一个必存不了水，默认都是0【不写下面两行在leetcode上会有问题...】
//        left_max[0] = 0;
//        right_max[size - 1] = 0;
//        for(int i = 1; i < size - 1; i++)       // 注意这两次遍历的边界，直接把头尾忽略
//            left_max[i] = max(left_max[i - 1], height[i - 1]);          // 注意不是height[i]
//        for(int i = size - 2; i > 0; i--)
//            right_max[i] = max(right_max[i + 1], height[i + 1]);        // 注意不是height[i]
//        int sum = 0;
//        for(int i = 1; i < size - 1; i++){
//            int min_border = min(left_max[i], right_max[i]);        // 小tips：这种变量不要取min这种名字，和函数名一样会编译错误
//            if(min_border > height[i])
//                sum += (min_border - height[i]);
//        }
//        return sum;

        /* 双指针【相对dp而言，优化了空间复杂度】 */
        int sum = 0;
        if(height.size() == 0)
            return sum;
        int size = height.size();
        int left_max = 0;
        int right_max = 0;
        // 双指针的话头和尾不能忽略，因为总共只遍历一次，忽略的话会影响max的判断
        int cur_left = 0;
        int cur_right = size - 1;
        while (cur_left <= cur_right){
            // 当我们从左往右处理到cur_left下标时，左边的最大值left_max对它而言是可信的，但right_max对它而言是不可信的
            // 即它左边最大值一定是left_max，右边最大值“大于等于”right_max
            // 如果left_max<right_max成立，那么它就知道自己能存多少水了。无论右边将来会不会出现更大的right_max，都不影响这个结果，此时处理cur_left
            if(left_max < right_max){
                sum += max(0, left_max - height[cur_left]);
                left_max = max(left_max, height[cur_left]);
                cur_left++;
            }
            else{           // 从右边往左更新right_max
                sum += max(0, right_max - height[cur_right]);
                right_max = max(right_max, height[cur_right]);
                cur_right--;
            }
        }
        return sum;
    }
};