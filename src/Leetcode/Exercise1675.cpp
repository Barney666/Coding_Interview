#include <vector>
#include <set>

using namespace std;

/**
 * 当我们把所有奇数变大成偶数再把最大的偶数从大缩小，最终最大值为奇数，其实蕴含者两件事：
 * 1）假如奇数变大后比原本的偶数大（或者奇数本来就比原本的偶数大），那么在缩小的过程中一定会打成原型（因为我们最终最大值为奇数值），结局不变，只不过我们考虑了奇数变成最大偶数的区间长度情况。
 * 2）假如奇数变大后都没有超过原来的偶数，那么得到的区间长度一定比直接计算的长度更小，之后缩小偶数要么让区间长度更小，要么不是，无论怎样，我们都在维护最短长度，最后也一定得到最短长度。
 * 也就是说先把所有的数变成偶数，再逐渐减小最大偶数为奇数这种操作让计算区间长度走完了所有的可能性。
 *
 * 让所有的偶数先变成奇数，然后再让奇数变成偶数也是可以的，只要保证策略的单向性就能利用贪心算法做出正确的结果。
 * */

class Solution {
public:
    int minimumDeviation(vector<int>& nums) {
        set<int> set;       // 默认从小到大排
        for(int num: nums)
            set.insert(num % 2 == 0 ? num : num * 2);       // 把所有数都变成其可变化范围的最大值
        int result = *set.rbegin() - * set.begin();            // 最大值减最小值，用*迭代器得到元素的值，注意最大值不是*set.end()，要用反向迭代器
        while(result > 0 && *set.rbegin() % 2 == 0){           // 不断缩小当前的最大值，直到不能缩小，其间一直维护偏移量值
            int temp_max = *set.rbegin();
            set.erase(temp_max);
            set.insert(temp_max / 2);
            result = min(result, *set.rbegin() - * set.begin());
        }
        return result;
    }
};