package SwordToOffer;

/**
 * 圆圈中剩下的数
 *【我只能想到模拟的方式orz 但复杂度太高了】
 *
 * 递归推理：
 * f(i, m)是每次递归留下第几个元素
 * 那么，我们可以求解 f(i-1, m)，就可以知道对于剩下的 i-1 个元素，最终会留下第几个元素 【注意是留 这里是逆向思维 取递归的结果】
 * 我们设答案为 x = f(i-1, m)，此时我们也就可以知道对于长度为i的序列，最后会被留下的一个元素是：第 (x+m) % i 个元素。
 * 可以自己写一个公式硬推 每次删完一个 把第一个看作index为0 找映射关系 然后找逆
 * 所以也就可以找到规律：
 * f[1] = 0
 * f[2] = (f[1] + m) % 2
 * f[3] = (f[2] + m) % 3
 * ...
 * f[n] = (f[n-1] + m) % n
 * */
public class Exercise46 {
    public int LastRemaining_Solution(int n, int m) {     // n是总人数 m是每次挑的第几个
        if(n<=0)
            return -1;
        int index = 0;
        for(int i=2;i<=n;i++)
            index = (index + m) % i;
        return index;
    }
}
