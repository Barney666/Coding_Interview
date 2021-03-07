class Solution {
public:
    int numOfWays(int n) {
        int mod = 1000000007;       // 最好别写10^9+7
        int arr[n][2];
        arr[0][0] = 6;
        arr[0][1] = 6;
        for(int i = 1; i < n; i++){
            arr[i][0] = (2l * arr[i-1][0] + 2l * arr[i-1][1]) % mod;        // 这里2和3要用long，然后再转int？不然会溢出
            arr[i][1] = (2l * arr[i-1][0] + 3l * arr[i-1][1]) % mod;
        }
        return (arr[n-1][0] + arr[n-1][1]) % mod;
    }
};