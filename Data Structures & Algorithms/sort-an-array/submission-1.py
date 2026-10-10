class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        s = nums.copy()
        heapq.heapify(s)

        for i in range(len(nums)):
            nums[i] = heapq.heappop(s)
        

        return nums