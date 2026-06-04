class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        long = 0

        for num in nums:
            if num - 1 not in s:
                l = 0
                while l + num in s:
                    l += 1
                long = max(l,long)
        return long
             
            