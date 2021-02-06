#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<string> v;
    int pair;

    void recursion(int left, int right, string temp_str){
        if(left == right){
            if(left == pair)
                v.push_back(temp_str);
            else
                recursion(left + 1, right, temp_str + "(");
        }
        else if(left > right){
            if(left != pair){
                recursion(left + 1, right, temp_str + "(");
                recursion(left, right + 1, temp_str + ")");
            }
            else
                recursion(left, right + 1, temp_str + ")");
        }
    }

    vector<string> generateParenthesis(int n) {
        pair = n;
        recursion(0, 0, "");
        return v;
    }
};