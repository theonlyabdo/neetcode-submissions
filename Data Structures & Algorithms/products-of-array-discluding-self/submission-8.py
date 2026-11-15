class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pp = [1] * n
        for i in range(1,n):
            pp[i] = nums[i-1] * pp[i-1]

        sp = [1] * n
        for i in range(n-2, -1,-1):
            sp[i] = nums[i+1] * sp[i+1]

        ans = []
        for i in range(n):
            ans.append(sp[i] * pp[i])
        
        return ans


# [1, 2, 4, 6]
# [1, 2, 8,48]
# [,,,6]