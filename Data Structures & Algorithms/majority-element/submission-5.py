class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        most = nums[0]
        mymap = {}

        for num in nums:
            mymap[num] = mymap.get(num, 0) + 1

            if mymap[num] >= mymap[most]:
                most = num
        return most
        