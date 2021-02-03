/**
 * 化学公式解析【把中括号变成小括号就是Leetcode726原子的数量】
 *
 * 给定一个用字符串展示的化学公式，计算每种元素的个数。
 * 规则如下：
 * 元素命名采用驼峰命名，例如 Mg
 * () 代表内部的基团，代表阴离子团
 * [] 代表模内部链节通过化学键的连接，并聚合
 * 例如：H2O => H2O1 Mg(OH)2 => H2Mg1O2
 * 输入描述:
 * 化学公式的字符串表达式，例如：K4[ON(SO3)2]2
 * 输出描述:
 * 元素名称及个数：K4N2O14S4，并且按照元素名称升序排列
 * 测试用例
 * 输入
 * K4[ON(SO3)2]2
 * 输出
 * K4N2O14S4
 *
 * */
#include <iostream>
#include <string>
#include <stack>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

// Leetcode726
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
//        if(pair.second != 1)        // 注意这块是1的话最后不要
//            result += to_string(pair.second);
        result += to_string(pair.second);       // 字节这题的输出要输出1
    }
    return result;
}

int main(){
    string input;
    cin >> input;
    replace(input.begin(), input.end(), '[', '(');      // #include<algorithm>中的replace算法实现string中某个字符全部换成新的
    replace(input.begin(), input.end(), ']', ')');
    cout << countOfAtoms(input);
}