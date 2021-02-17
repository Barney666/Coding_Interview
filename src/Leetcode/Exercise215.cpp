#include <vector>
#include <queue>
#include <algorithm>

using namespace std;


class Solution {
public:
    vector<int> quick_sort_big(vector<int> v, int left, int right, int k){     // 因为这个只要第k大的，所以可以只递归右侧，不然正常快排会超时
        int original_left = left;
        int original_right = right;
        int basis = v[left];
        int count = 0;
        while (left != right){
            if(count % 2 == 0){     // 先右侧
                while (left != right){
                    if(v[right] < basis){
                        v[left] = v[right];
                        break;
                    }
                    else right--;
                }
            }
            else{
                while (left != right){
                    if(v[left] > basis){
                        v[right] = v[left];
                        break;
                    }
                    else left++;
                }
            }
            count++;
        }
        v[left] = basis;
        if(original_right - left >= k)
            return quick_sort_big(v, left + 1, original_right, k);
        else{
            vector<int> result;
            if(original_left <= left - 1){        // 左侧剩的数至少一个
                vector<int> left_v = quick_sort_big(v, original_left, left - 1, k);
                result.insert(result.end(), left_v.begin(), left_v.end());       // 合并，将其压入
            }
            result.push_back(basis);
            if(left + 1 <= original_right){        // 右侧剩的数至少一个
                vector<int> right_v = quick_sort_big(v, left + 1, original_right, k);
                result.insert(result.end(), right_v.begin(), right_v.end());     // 合并，将其压入
            }
            return result;
        }
    }


    int findKthLargest(vector<int>& nums, int k) {
//        priority_queue<int> pq;      // 默认大根堆
//        for(int num: nums)
//            pq.push(num);
//        for(int i = 0; i < k - 1; i++){
//            pq.pop();
//        }
//        return pq.top();
        vector<int> v = quick_sort_big(nums, 0, nums.size() - 1, k);
        return v[v.size() - k];
    }
};