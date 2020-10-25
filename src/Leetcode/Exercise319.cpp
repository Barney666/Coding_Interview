#include <iostream>

using namespace std;

class Solution {
public:
    int bulbSwitch(int n) {
        return sqrt(n);       // 非完全平方数字有偶数个因子，所以只有完全平方数能够满足被操作奇数次，也就是最后只有完全平方数会亮着
    }
};
