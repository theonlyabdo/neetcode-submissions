class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        i =0
        for j in range(1, len(nums)):
            if nums[i] == nums[j]:
                return True
            i+=1
        return False
            
        