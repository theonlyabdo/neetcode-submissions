class Solution {
    public int missingNumber(int[] nums) {
        int n= nums.length;
        int xored = 0;

        for (int i = 0; i <= n; ++i){
            xored ^= i;
        } 

        for (int i = 0; i <n; ++i){
            xored ^= nums[i];
        }

        return xored;
  
    }
}
