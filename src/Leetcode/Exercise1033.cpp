#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> numMovesStones(int a, int b, int c) {
        if(b < a)  swap(a, b);
        if(c < b)  swap(b, c);
        if(b < a)  swap(a, b);

        int min;
        if(a == b-1 == c-2)
            min = 0;
        else if(a+2 == b || b+2 ==c)     // 3,6,1 => 1,3,6：把6变成2即可
            min = 1;
        else
            min = (b==a+1 ? 0 : 1) + (c==b+1 ? 0 : 1);
        int max = (b - a -1) + (c - b - 1);
        vector<int> result = {min, max};
        return result;
    }
};