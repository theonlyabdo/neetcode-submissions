class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)

        def backtrack(i, cursum):
            if cursum == target:
                res.append(sol[:])
                return
            
            if i >= n or cursum > target:
                return
            
            sol.append(nums[i])
            backtrack(i, nums[i] + cursum)
            sol.pop()

            backtrack(i + 1, cursum)
        
        backtrack(0, 0)
        return res