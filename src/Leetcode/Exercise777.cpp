#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    bool canTransform(string start, string end) {
        int start_point = 0;
        int end_point = 0;
        while (start_point < start.size() && end_point < end.size()){
            // 'L'、'R'分别理解为一个队伍中面向左和面向右的人，'X'理解为队伍中的空挡
            while (start[start_point] == 'X')
                start_point++;
            while (end[end_point] == 'X')
                end_point++;
            if(start[start_point] != end[end_point])    // 字符串中的'L'和'R'是不会互相穿插的，也就是除了'X'的相对位置是不变的
                return false;
            if(start[start_point] == 'L' && start_point < end_point)    // 'L'只能往左走
                return false;
            if(start[start_point] == 'R' && start_point > end_point)    // 'R'只能往右走
                return false;
            start_point++;
            end_point++;
        }
        // 最后不能有除了'X'以外的字母，从start_point/end_point下标开始查找
        return (start.find('L',start_point) == -1 && start.find('R',start_point) == -1 && end.find('L', end_point) == -1 && end.find('R', end_point) == -1);
    }
};