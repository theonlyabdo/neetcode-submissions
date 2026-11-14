class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        
        for i in range(len(nums)):
            m[nums[i]] = i
        
        for i in range(len(nums)):
            tcomp = target - nums[i]
            if tcomp in m and m[tcomp] != i:
                return [i,m[tcomp]]