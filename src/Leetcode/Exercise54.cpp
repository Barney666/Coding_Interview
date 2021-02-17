#include <vector>

using namespace std;


class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int length = matrix.size();
        int width = matrix[0].size();
        int layer = 0;
        int time = (min(length, width) + 1) / 2;        // 这里很关键
        vector<int> result;
        while (layer < time){
            for(int i = layer; i < width - layer; i++)
                result.push_back(matrix[layer][i]);
            for(int i = layer + 1; i < length - layer; i++)
                result.push_back(matrix[i][width - 1 - layer]);
            // length - 1 - layer != layer 这个判断条件很关键，是指上下两行不重复，否则只有一行那种的这块不能再打印了，会重复。
            for(int i = width - 1 - layer - 1; i >= layer && (length - 1 - layer != layer); i--)
                result.push_back(matrix[length - 1 - layer][i]);
            for(int i = length - 1 - layer - 1; i >= layer + 1 && (width - 1 - layer != layer); i--)    // width - 1 - layer != layer 即左右两行
                result.push_back(matrix[i][layer]);
            layer++;
        }
        return result;
    }
};