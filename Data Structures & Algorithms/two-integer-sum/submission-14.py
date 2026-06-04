class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            seen[nums[i]] = i
        
        for i in range (len(nums)):
            t_com = target - nums[i]
            if t_com in seen and i != seen[t_com]:
                return [i,seen[t_com]]
        
        return []