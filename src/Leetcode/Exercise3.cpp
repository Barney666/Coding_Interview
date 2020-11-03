#include <iostream>
#include <string>
#include <unordered_map>    // hash_map

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s){
        int max_length = 0;
        unordered_map<char,int> hash_map;      // 利用hash_map优化滑动窗口，也可用数组(桶)来优化，例：int[26]代表'a'-'z'这种
        int left, right = 0;       // 滑动窗口左右指针
        int temp_length = 0;
        while (left < s.length() && right < s.length()){
            char c = s.at(right);
            if(hash_map.find(c) != hash_map.end() && hash_map[c] >= left){   // find()返回值是迭代器，如果找不到这个key就返回end()
                left = hash_map[c] + 1;
                temp_length = right - left;
            }
            hash_map[c] = right;      // 比hash_map.insert(pair<char,int>(c,right))更省事
            right++;
            temp_length++;
            max_length = max(temp_length, max_length);
        }
        return max_length;
    }
};