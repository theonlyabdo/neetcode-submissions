class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ss = [1] * n
        ps = [1] * n
        for i in range(1,n):
            ps[i] = ps[i-1] * nums[i-1]
       
        for i in range(n-2,-1,-1):
            ss[i] = ss[i+1] * nums[i+1]
        
        sol = []
        for i in range(n):
            sol.append(ss[i]*ps[i])
        
        return sol