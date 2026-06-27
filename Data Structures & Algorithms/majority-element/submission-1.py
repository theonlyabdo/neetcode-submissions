class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        n = len(nums)
        for num, freq in c.items():
            if freq >= n/2:
                return num
        return 0
        