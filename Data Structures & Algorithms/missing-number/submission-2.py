class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xored = 0
        for i in range(n+1):
            xored ^= i
            
        for i in range(n):
            xored ^= nums[i]
            
        return xored