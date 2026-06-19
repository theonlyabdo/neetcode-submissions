class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        
        if n == 2:
            return max(nums[0],nums[1])
        
        memo = {0:nums[0], 1: max(nums[0], nums[1])}
        def steal(i):
            if i in memo:
                return memo[i]
            else:
                memo[i] = max(nums[i] + steal(i-2), steal(i-1))
                return memo[i]
        
        return steal(n-1)
