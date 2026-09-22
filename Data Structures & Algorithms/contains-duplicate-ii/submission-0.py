class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mymap = {}

        for i in range(len(nums)):
            if nums[i] in mymap:
                j = mymap[nums[i]]
                if abs(i - j) <= k:
                    return True
            mymap[nums[i]] = i
        return False