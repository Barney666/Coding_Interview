#include <vector>
#include <string>
#include <cmath>

using namespace std;

/**
 * Hierholzer算法如下：
 * 我们从节点u开始，任意地经过还未经过的边，直到我们「无路可走」。此时我们一定回到了节点，这是因为所有节点的入度和出度都相等。
 * 回到节点u之后，我们得到了一条从u开始到u结束的回路，这条回路上仍然有些节点有未经过的出边。
 * 我们从某个这样的节点v开始，继续得到一条从v开始到v结束的回路，再嵌入之前的回路中，即u→⋯→v→⋯→u变为u→⋯→v→⋯→v→⋯→u
 * 以此类推，直到没有节点有未经过的出边，此时我们就找到了一条欧拉回路。
 *
 * */

class Solution {
public:
    int node_num;
    string result = "";
    int k_base;

    void dfs(int cur_num, vector<bool>& visited_vector){
        int cur_node = cur_num % node_num;
        // 这里是根据cur_num来看到哪个节点了，cur_node就是cur_num化成k进制的后n-1位，cur_num是存在vector中的边，cur_node是图中的节点
        for(int i = 0; i < k_base; i++){         // 这个节点的k-1条边
            int cur_num = cur_node * k_base + i;     // 现在所在节点数字后面加一个i，因此在化成十进制时cur_node要先乘个k
            if(!visited_vector[cur_num]){
                visited_vector[cur_num] = true;
                dfs(cur_num, visited_vector);
                result += (i + '0');
            }
        }
    }

    string crackSafe(int n, int k) {
        k_base = k;
        node_num = pow(k ,n-1);         // 以n-1位的数作为图的每一个节点
        vector<bool> visited_vector(node_num * k, 0);         // 记录每一条边是否被访问过
        // 虽然最后是经过所有节点，但Hierholzer算法是根据边来看是否迭代完成的，所以这里记录的是边。
        dfs(0, visited_vector);
        result.append(n-1, 0);      // 补充开始节点，n-1个0
        return result;      // 递归中是从后往前加的字符串，但也是正确的最短字符串，所以也没必要reverse一下
    }
};
