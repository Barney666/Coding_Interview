#include <iostream>

using namespace std;

class Solution {
public:
    bool canWinNim(int n) {
        return (n % 4) != 0;        // 如果堆中石头的数量不能被4整除，那么你总是可以赢得 Nim 游戏的胜利。
    }
};
