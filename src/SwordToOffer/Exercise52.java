package SwordToOffer;

/**
 * 正则表达式匹配
 *【我的代码idea上跑一点问题没有 相同代码相同用例跑在牛客网上就是完全相反的结果 老子吐了】
 * */
public class Exercise52 {

    public boolean match(char[] str, char[] pattern) {     // 能过牛客网的代码 下面那个第二个是*的 return3个递归的或 想法挺好
        if (str == null || pattern == null) {
            return false;
        }
        int strIndex = 0;
        int patternIndex = 0;
        return matchCore(str, strIndex, pattern, patternIndex);
    }
    public boolean matchCore(char[] str, int strIndex, char[] pattern, int patternIndex) {
        //有效性检验：str到尾，pattern到尾，匹配成功
        if (strIndex == str.length && patternIndex == pattern.length) {
            return true;
        }
        //pattern先到尾，匹配失败
        if (strIndex != str.length && patternIndex == pattern.length) {
            return false;
        }
        //模式第2个是*，且字符串第1个跟模式第1个匹配,分3种匹配模式；如不匹配，模式后移2位
        if (patternIndex + 1 < pattern.length && pattern[patternIndex + 1] == '*') {
            if ((strIndex != str.length && pattern[patternIndex] == str[strIndex]) || (pattern[patternIndex] == '.' && strIndex != str.length)) {
                return matchCore(str, strIndex, pattern, patternIndex + 2)//模式后移2，视为x*匹配0个字符
                        || matchCore(str, strIndex + 1, pattern, patternIndex + 2)//视为模式匹配1个字符
                        || matchCore(str, strIndex + 1, pattern, patternIndex);//*匹配1个，再匹配str中的下一个
            } else {
                return matchCore(str, strIndex, pattern, patternIndex + 2);
            }
        }
        //模式第2个不是*，且字符串第1个跟模式第1个匹配，则都后移1位，否则直接返回false
        if ((strIndex != str.length && pattern[patternIndex] == str[strIndex]) || (pattern[patternIndex] == '.' && strIndex != str.length)) {
            return matchCore(str, strIndex + 1, pattern, patternIndex + 1);
        }
        return false;
    }
//    public boolean match(char[] str, char[] pattern){     // 我的代码
//        int sIndex=0;
//        int pIndex=0;
//
//        while(sIndex<str.length && pIndex<pattern.length){
//            char c1=str[sIndex];
//            char c2=pattern[pIndex];
//            if(c2=='.' || c1==c2){
//                sIndex++;
//                pIndex++;
//                if(pIndex<pattern.length && pattern[pIndex]=='*'){
//                    while (sIndex<str.length && c1==str[sIndex])
//                        sIndex++;
//                    pIndex++;
//                }
//            }
//            else{
//                if(pIndex<pattern.length-1 && pattern[pIndex+1]=='*')
//                    pIndex+=2;
//                else
//                    return false;
//            }
//        }
//        while (sIndex==str.length && pIndex<pattern.length && pattern[pIndex]==str[sIndex-1])
//            pIndex++;     // 防止 "" , ".*" 这种存在
//        if(sIndex==str.length && pIndex==pattern.length)
//            return true;
//        return false;
//    }
}
