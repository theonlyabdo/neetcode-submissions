class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = defaultdict(int)
        n = len(nums)

        for num in nums:
            c[num] += 1
            if c[num] >= n/2:
                return num
        return 0