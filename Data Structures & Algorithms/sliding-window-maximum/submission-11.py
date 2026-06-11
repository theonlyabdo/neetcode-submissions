import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k - 1
        sol = []

        while r < len(nums):
            heap = [-x for x in nums[l:r+1]]
            heapq.heapify(heap)

            sol.append(-heapq.heappop(heap))

            l += 1
            r += 1

        return sol