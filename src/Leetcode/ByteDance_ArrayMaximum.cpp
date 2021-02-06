/**
 * 数组组成最大数
 *
 * 给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。
 * 示例 1:
 * 输入: [10,1,2]
 * 输出: 2110
 * 示例 2:
 * 输入: [3,30,34,5,9]
 * 输出: 9534330
 *
 * */
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool comp(const string& a, const string& b){
    string temp1 = a + b;       // 想让"3">"30"这么整就行，不用一个一个0加再看
    string temp2 = b + a;
    return temp1 > temp2;       // 由大到小排
}

int main(){
    string input;
    cin >> input;
    if(input.size() <= 2)
        return 0;
    input = input.substr(1, input.size() - 2);
    vector<string> v;           //    set<string, greater<string>> s;  如果用这样会出现30>3，就是303而不是330了，只能自己写comp
    string temp_str = "";

    for(int i = 0; i < input.size(); i++){
        if(i == input.size() - 1){      // 这里循环要是foreach就会漏掉最后一个，注意这种小bug
            temp_str += input[i];
            v.push_back(temp_str);
        }
        else if(input[i] == ','){
            v.push_back(temp_str);
            temp_str = "";
        }
        else
            temp_str += input[i];
    }
    sort(v.begin(), v.end(), comp);
    for(auto iter = v.begin(); iter != v.end(); iter++)
        cout << *iter;
}