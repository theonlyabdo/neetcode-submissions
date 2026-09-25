class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mymap = {}

        for i in range(len(nums)):
            mymap[nums[i]] = i
        
        for i in range(len(nums)):
            tcom = target - nums[i]
            if tcom in mymap and i != mymap[tcom]:
                return [i, mymap[tcom]]
        return [-1]