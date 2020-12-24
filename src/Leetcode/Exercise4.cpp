#include <iostream>
#include <vector>

using namespace std;


/* 如果对时间复杂度的要求有log，通常都需要用到二分查找，这道题也不例外。
 *
 * 使用一个小trick，可以避免讨论奇偶：
 * 我们分别找第 (m+n+1)/2个数，和(m+n+2)/2个数，然后求其平均值即可，这对奇偶数均适用。
 * 假如 m+n 为奇数的话，那么其实 (m+n+1) / 2 和 (m+n+2) / 2 的值相等，相当于两个相同的数字相加再除以2，还是其本身。*/
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int find_num = (nums1.size() + nums2.size()) / 2;

    }
};