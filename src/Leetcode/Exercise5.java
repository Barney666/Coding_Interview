package Leetcode;

/**
 * 最长回文子串
 *
 *《 动 态 规 划 》
 * 如果它是回文串，并且长度大于2，那么将它首尾的两个字母去除之后，它仍然是个回文串
 * p(i,j) = p(i+1,j-1) && (Si==Sj)
 *
 * */
public class Exercise5 {
    public String longestPalindrome(String s) {
        int size = s.length();
        boolean[][] record = new boolean[size][size];
        String result = "";
        for(int diff=0; diff<size; diff++){    // 我们是从长度较短的字符串向长度较长的字符串进行转移的，因此一定要注意动态规划的循环顺序！
            for(int i=0 ;i+diff<size; i++){
                int j = i+diff;     // 注意这个手法
                switch (diff){
                    case 0:
                        record[i][j] = true;
                        break;
                    case 1:
                        record[i][j] = (s.charAt(i)==s.charAt(j));
                        break;
                    default:
                        record[i][j] = (record[i+1][j-1] && (s.charAt(i)==s.charAt(j)));
                        break;
                }
                if(record[i][j] && diff+1>result.length()){
                    result = s.substring(i,j+1);
                }
            }
        }
        return result;
    }
}
