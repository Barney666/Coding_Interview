#include <iostream>
#include <string>

using namespace std;

class Solution {    // 纯nt题
public:
    int findLUSlength(string a, string b) {
        if(a == b)
            return -1;    // 如果两个字符串相同，则没有特殊子序列，返回 -1
        if(a.size() == b.size())
            return a.size();    // 这种情况下，一个字符串一定不会是另外一个字符串的子序列，因此可以将任意一个字符串看作是特殊子序列
        return max(a.size(), b.size());    // 长的字符串一定不会是短字符串的子序列，因此可以将长字符串看作是特殊子序列
    }
};