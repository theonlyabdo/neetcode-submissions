class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n= nums.size();
        int xored = 0;

        for (int i = 0; i <= n; ++i){
            xored ^= i;
        } 

        for (int i = 0; i <n; ++i){
            xored ^= nums[i];
        }

        return xored;
     
    }
};
