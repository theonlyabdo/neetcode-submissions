class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}

        for i in range(len(nums)):
            s[nums[i]] = i

        for i in range(len(nums)):
            t_comp = target - nums[i]
            if t_comp in s and i != s[t_comp]:
                return [i,s[t_comp]]
        
        return []