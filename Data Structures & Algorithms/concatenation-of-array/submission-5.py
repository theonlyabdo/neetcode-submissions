class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums) * 2
        n = len(nums)

        for i in range(n):
            ans[i] = ans[i+n] = nums[i]
        
        return ans