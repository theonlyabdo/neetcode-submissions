import heapq
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        result = []

        for i in range(len(nums)):
            # Push current element
            heapq.heappush(heap, (-nums[i], i))

            # Remove elements outside window
            while heap[0][1] <= i - k:
                heapq.heappop(heap)

            # Start recording after first full window
            if i >= k - 1:
                result.append(-heap[0][0])

        return result
