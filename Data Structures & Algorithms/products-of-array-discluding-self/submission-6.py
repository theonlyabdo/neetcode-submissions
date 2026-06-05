class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # suffix product
        sp = [1] * n
        for i in range(n-2,-1,-1):
            sp[i] = sp[i+1] * nums[1+i]
        # print(sp)

        # prefix product
        pp = [1] * n
        for i in range(1,n):
            pp[i] = pp[i-1] * nums[i-1]
        # print(pp)


        sol = []
        for i in range(n):
            sol.append(sp[i]*pp[i])
        return sol