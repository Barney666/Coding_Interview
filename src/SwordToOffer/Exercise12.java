package SwordToOffer;

/**
 * 数值的整数次方
 *
 * */
public class Exercise12 {
    public double Power(double base, int exponent) {
        if(base==0)   // 0的次方为0
            return 0;
        if(exponent==0)
            return 1;
        boolean isNegative=false;
        if(exponent<0){
            exponent=-exponent;
            isNegative=true;
        }
        double result=base;
        for(int i=0;i<exponent-1;i++)
            result*=base;
        if(isNegative)
            return 1/result;
        return result;
    }
}
