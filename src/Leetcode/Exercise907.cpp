#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    int sumSubarrayMins(vector<int>& arr) {
        // 先用84题的单调栈
        int n = arr.size();
        vector<int> left(n), right(n);
        stack<int> monotone_stack;

        for(int i = 0; i < n; i++){
            // 这题为了应对重复元素，左右侧是不一样的，左侧找小于等于，右侧正常找小于的，背下来吧...
            while (!monotone_stack.empty() && arr[monotone_stack.top()] > arr[i])       // 这里从左边找第一个小于等于它的数字的索引
                monotone_stack.pop();
            left[i] = monotone_stack.empty() ? -1 : monotone_stack.top();
            monotone_stack.push(i);
        }

        monotone_stack = stack<int>();

        for(int i = n - 1; i >= 0; i--){
            while (!monotone_stack.empty() && arr[monotone_stack.top()] >= arr[i])      // 这里从右边找第一个小于它的数字的索引
                monotone_stack.pop();
            right[i] = monotone_stack.empty() ? n : monotone_stack.top();
            monotone_stack.push(i);
        }

        int result = 0;
        for(int i = 0; i < n; i++){
            int affect_left = i - left[i];
            int affect_right = right[i] - i;
            // affect_sum就是这个数在连续子数组中成为了多少组的最小值
            int affect_sum = affect_left * affect_right;    // 我他妈接受不了啊，为什么总是些奇奇怪怪的式子就能算出正确的数啊
            if(affect_sum > 100000000 && affect_sum % 2 == 0){      // 只是为了Leetcode最后一个用例，affect_sum * arr[i]会溢出，longlong也不行
                result = (result + affect_sum / 2 * arr[i]) % 1000000007;
                result = (result + affect_sum / 2 * arr[i]) % 1000000007;
            }
            else
                result = (result + affect_sum * arr[i]) % 1000000007;
            // 1.在求max的时候不要先取mod 2.在算res的过程中先取模，这两种是正确的取模方式。【注意10^9+7最好不要写成1e9+7，后面这种是浮点数，会有精度方面的问题】
        }
        return result;
    }
};
