class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        size = 1

        for r in range(1,len(nums)):
            if nums[r] != nums[r-1]:
                nums[size] = nums[r]
                size +=1

        return size 