#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int n = heights.size();
        vector<int> left(n), right(n);      // 每一根柱子的左右侧最近的小于其高度的柱子
        stack<int> monotone_stack;          // 单调栈

        for(int i = 0; i < n; i++){
            while (!monotone_stack.empty() && heights[monotone_stack.top()] >= heights[i])       // 注意是大于等于
                monotone_stack.pop();
            left[i] = monotone_stack.empty() ? -1 : monotone_stack.top();       // 栈为空时，left存入哨兵，位置为-1
            monotone_stack.push(i);         // 栈里存的是index
        }

        monotone_stack = stack<int>();

        for(int i = n - 1; i >= 0; i--){
            while (!monotone_stack.empty() && heights[monotone_stack.top()] >= heights[i])
                monotone_stack.pop();
            right[i] = monotone_stack.empty() ? n : monotone_stack.top();       // 栈为空时，right存入哨兵，位置为n
            monotone_stack.push(i);         // 栈里存的是index
        }

        int result = 0;
        for(int i = 0; i < n; i++)
            result = max(result, (right[i] - left[i] - 1) * heights[i]);        // 这里就是前面哨兵很神奇的一点了，用right[i]-left[i]-1就是正确的宽度
        return result;
    }
};