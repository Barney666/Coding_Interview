#include <string>
#include <stack>
#include <map>
#include <vector>

using namespace std;

class Solution {
public:
    string countOfAtoms(string formula) {
        map<string, int> count;         // map红黑树自动按key从小到大排序，很爽
        stack<pair<string, int>> stack;
        int index = 0;
        while (index < formula.size()){
            if(formula[index] == '('){
                stack.push(pair<string, int>("(", 0));
                index++;
            }
            else if(formula[index] == ')'){
                index++;
                int multi = 0;
                while ('0' <= formula[index] && formula[index] <= '9'){
                    multi *= 10;
                    multi += formula[index] - '0';
                    index++;
                }
                multi = (multi == 0) ? 1 : multi;     // 默认1个
                vector<pair<string, int>> temp;
                while (stack.top().first != "("){
                    temp.push_back(stack.top());
                    stack.pop();
                }
                stack.pop();
                for(pair<string, int> pair: temp){
                    pair.second *= multi;
                    stack.push(pair);
                }
            }
            else{
                string element = string(1, formula[index]);     // 构造函数里有个string（size_t,char）
                index++;
                while ('a' <= formula[index] && formula[index] <= 'z'){
                    element += formula[index];
                    index++;
                }
                int num = 0;
                while ('0' <= formula[index] && formula[index] <= '9'){
                    num *= 10;
                    num += formula[index] - '0';
                    index++;
                }
                num = (num == 0) ? 1 : num;     // 默认1个
                if(!stack.empty())          // 是在括号里的
                    stack.push(pair<string, int>(element, num));
                else{
                    auto iterator = count.find(element);
                    if(iterator == count.end())
                        count[element] = num;
                    else
                        count[element] += num;
                }
            }
        }
        while (!stack.empty()){
            pair<string, int> pair = stack.top();
            stack.pop();
            string element = pair.first;
            int num = pair.second;
            auto iterator = count.find(element);
            if(iterator == count.end())
                count[element] = num;
            else
                count[element] += num;
        }
        string result = "";
        for(auto pair: count){
            result += pair.first;
            if(pair.second != 1)        // 注意这块是1的话最后不要
                result += to_string(pair.second);
        }
        return result;
    }
};