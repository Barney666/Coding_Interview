#include <string>
#include <regex>

using namespace std;

class Solution {
public:
    string validIPAddress(string IP) {      /*   c++的正则中含有\的元字符，都要写成\\   */
        regex ip4_more_dot("(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){4}");         // 最后多一个点，这样整洁一点，不然还要单拎出一个
        regex ip6_more_dot("([0-9a-fA-F]{1,4}\\:){8}");     // 最后多个冒号，单拎出一个"([0-9a-fA-F]{1,4}\\:){7}[0-9a-fA-F]{1,4}"太丑了
        if(regex_match(IP + ".", ip4_more_dot))
            return "IPv4";
        else if(regex_match(IP + ":", ip6_more_dot))
            return "IPv6";
        else
            return "Neither";
    }
};