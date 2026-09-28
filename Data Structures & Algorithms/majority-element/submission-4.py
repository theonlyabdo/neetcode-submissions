class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
    
        most, mostfreq = nums[0], 0
        for num, freq in count.items():
            if freq >= mostfreq:
                most = num
            mostfreq = max(freq,mostfreq)

        return most