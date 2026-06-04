class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [1] * n
        suff = [1] * n
        sol = []

        # prefix sum array
        for i in range(1, n):
            pref[i] = pref[i-1] * nums[i-1]

        # suffix sum array
        for i in range(n-2,-1,-1):
            suff[i] = suff[i+1] * nums[i+1]

        # using prefix array with suffix array
        for i in range(n):
            sol.append(pref[i]*suff[i])

        return sol