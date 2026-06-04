class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in num_set:
                l = 0
                while num + l in num_set:
                    l+=1
                longest = max(l,longest)
        return longest