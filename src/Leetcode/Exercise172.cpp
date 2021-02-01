class Solution {
public:
    // 这个题其实就是找有多少个5，但不能直接返回n/5，因为25，125等有多个5，所以要逐步看。
    int trailingZeroes(int n) {
        int result = 0;
        while(n > 0) {
            result += (n / 5);
            n /= 5;
        }
        return result;
    }
};