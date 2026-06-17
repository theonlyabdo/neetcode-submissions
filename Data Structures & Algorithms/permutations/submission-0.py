class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)

        def backtrack():
            if n == len(sol):
                res.append(sol[:])
                return
            
            for num in nums:
                if num in sol:
                    continue
                
                sol.append(num)
                backtrack()
                sol.pop()
        
        backtrack()
        return res