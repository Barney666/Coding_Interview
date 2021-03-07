#include <vector>
#include <unordered_map>
#include <queue>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution {
public:
    int numBusesToDestination(vector<vector<int>>& routes, int source, int target) {
        if(source == target)
            return 0;
        int bus_num = routes.size();
        vector<bool> bus_used(bus_num, false);      // 记录用过的公交车
        unordered_map<int, vector<int>> station_by_bus;      // 记录每个站点都有哪些公交车可到达
        queue<int> accessible_station;      // BFS记录现在可以到达的站点
        accessible_station.push(source);
        int result = 1;     // 最小是1，已经把source加到queue中了

        for(int i = 0; i < bus_num; i++)
            for(int station: routes[i])
                station_by_bus[station].push_back(i);

        while (!accessible_station.empty()){
            for(int i = accessible_station.size(); i > 0; i--){     // 这样可以不用因为里面会把queue的长度增加，而单独定义一个变量记录长度
                int station = accessible_station.front();
                accessible_station.pop();
                for(auto bus: station_by_bus[station]){     // 这里是关键思想，先根据站点会有哪些公交车，再到routes中看这个公交车还能去哪
                    if(!bus_used[bus]){
                        bus_used[bus] = true;
                        for(int next_station: routes[bus]){
                            if(next_station == target)
                                return result;
                            else
                                accessible_station.push(next_station);
                        }
                    }
                }
            }
            result++;           // 一轮完事
        }
        return -1;
    }
};