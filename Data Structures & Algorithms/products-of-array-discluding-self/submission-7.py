class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        suff = [1] * n
        for i in range(n-2,-1, -1):
            suff[i] = suff[i+1] * nums[i+1]
            
        pref = [1] * n
        for i in range(1,n):
            pref[i] = pref[i-1] * nums[i-1]
        
        res = [1] * n
        for i in range(n):
            res[i] = pref[i] * suff[i]

        return res


# array:    [ 1, 2, 4, 6]
# SP:       [ 1, 1, 2, 8]
# PP:       [48,24, 6, 1]
# Res:      [48,24,12, 1]