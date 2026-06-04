class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            hash_map[nums[i]] = i
        
        for i in range(len(nums)):
             t_complement = target - nums[i]
             if t_complement in hash_map and i != hash_map[t_complement]:
                return [i, hash_map[t_complement]]
        return []        

        