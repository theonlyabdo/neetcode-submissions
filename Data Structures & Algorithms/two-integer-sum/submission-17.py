class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            seen[nums[i]] = i
        
        for i in range(len(nums)):
            t_comp = target - nums[i]
            if t_comp in seen and seen[t_comp] != i:
                return [i, seen[t_comp]]
        return []