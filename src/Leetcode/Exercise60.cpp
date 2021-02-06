#include <vector>
#include <string>

using namespace std;

/**
 * 康托展开与逆展开：https://blog.csdn.net/ltrbless/article/details/87696372
 * 本题是逆展开
 * */
class Solution {
public:
    int factorial(int num){
        if(num == 0)
            return 1;
        return num * factorial(num - 1);
    }

    string getPermutation(int n, int k) {
        k -= 1;         // 先把顺序号减1，因为康托展开里的初始序列编号为0，这样才能用下面的公式
        string result = "";
        vector<int> record_vector;
        for(int i = 1; i <= n; i++)     // 注意这里是<=
            record_vector.push_back(i);
        for(int i = n - 1; i >= 0; i--){
            int fac = factorial(i);
            int less_num = k / fac;     // 有多少比这个数小的数，正好还可以当vector的index
            k %= fac;
            int num = record_vector[less_num];
            record_vector.erase(record_vector.begin() + less_num, record_vector.begin() + less_num + 1);
            result += to_string(num);
        }
        return result;
    }
};