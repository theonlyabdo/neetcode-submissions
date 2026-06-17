class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        n = len(candidates)
        candidates.sort()

        def backtrack(i, cursum):
            if cursum == target:
                res.append(sol[:])
                return
            
            if i == n or cursum > target:
                return
            
            # include candidates[i]
            sol.append(candidates[i])
            backtrack(i+1, candidates[i] + cursum)
            sol.pop() 

            # skip candidates[i] 
            while i+1 < n and candidates[i] == candidates[1+i]:
                i += 1
            backtrack(i + 1, cursum)
        
        backtrack(0, 0)
        return res