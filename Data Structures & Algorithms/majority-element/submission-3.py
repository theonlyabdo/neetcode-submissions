class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mymap = {}

        for num in nums:
            if num not in mymap:
                mymap[num] = 0
            mymap[num] += 1
    
        most, mostfreq = nums[0], 0
        for num, freq in mymap.items():
            if freq >= mostfreq:
                most = num
            mostfreq = max(freq,mostfreq)

        return most