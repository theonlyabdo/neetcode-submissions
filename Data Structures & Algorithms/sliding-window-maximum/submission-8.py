class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l,r,n = 0, k, len(nums)
        sol = []
        while r <= n:
            #print(f"{l}, {r}")
            c = float("-inf")
            for i in range(l,r):
                c = max(c,nums[i])
            sol.append(c)
            l += 1
            r += 1
        return sol
                