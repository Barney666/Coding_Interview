class Solution {
public:
    int minimumBoxes(int n) {       // 现在的时间复杂度是sqrt(n)，两个while循环其实可以用二分法优化的，这样时间复杂度可以达到log(n)
        int layer = 1;
        int cell = 0;
        while (true){       // 看总数为n的有多少层
            int cur_layer_cell = (1 + layer) * layer / 2;       // 每一层最多可存数量就是1+2+...+layer
            if(cell + cur_layer_cell > n)
                break;
            cell += cur_layer_cell;
            layer++;
        }
        layer--;        // 先堆成较小的饱和堆，再考虑没堆进去的
        int ground_cell = (1 + layer) * layer / 2;      // 当前最下面一层有多少个块，此时可能总数没到n
        int new_cell = 0;
        while (cell < n){
            ground_cell++;              // 最下层多放一个
            cell += (new_cell + 1);     // 除了第一次只能多放一个以外，剩下下面每多放一个，上一层就还能再放一个，这里很重要
            new_cell++;                 // 从较小的饱和堆逐渐向下一个饱和堆增加
        }
        return ground_cell;
    }
};