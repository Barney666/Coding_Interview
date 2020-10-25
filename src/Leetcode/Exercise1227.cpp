#include <iostream>
#include <string>
#include <vector>

using namespace std;

/**
 * 有 n 位乘客即将登机，飞机正好有 n 个座位。第一位乘客的票丢了，他随便选了一个座位坐下。
 * 剩下的乘客将会：
 * 如果他们自己的座位还空着，就坐到自己的座位上 ; 当他们自己的座位被占用时，随机选择其他座位。
 * 问：第 n 位乘客坐在自己的座位上的概率是多少？
 *
 *
 * 假设共有n个座位，令f(i)表示第一个人选择第i个人的座位时，第n个座位被其他人（1到n-1）占用的概率。
 * 显然f(n)=1，即如果第一个人选择第n个座位，那么第n个座位必然是被其他占用了。
 * f(n-1)=1/2，即如果1选择n-1，则2到n-2会对号入座，第n-1个人选择的时候有两种选择（1和n），选n的概率为1/2。
 * f(n-2)=1/3+1/3f(n-1)=1/2，即如果第一个人选择第n-2个座位，那么第n-2个人有三种选择（1，n-1，n），每个都是1/3。
 * 如果选择n，那么概率为1/3；如果选择n-1/1座位，则第n-1个人做选择时，和第1个人选择n-1/1情况是一样的，即f(n-1)。
 * 以此类推：
 * f(n-3)=1/4+1/4f(n-1)+1/4f(n-2)=1/2
 * ...
 * ...
 * ...
 * f(2)=1/2
 * f(1)=0
 * 因此第n个座位被其他人占用的概率为1/n[f(2)+f(3)+...+f(n)]=1/2。
 *
 *
 * 这题直接背下来吧...
 * */

class Solution {
public:
    double nthPersonGetsNthSeat(int n) {
        return n==1 ? 1 : 0.5;
    }
};