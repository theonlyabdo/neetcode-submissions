class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # hash map to store  counter
        count = {}
        res = 0

        l = 0
        for r in range(len(s)):
            # do the counter
            count[s[r]] =  1 + count.get(s[r],0)

            # compre k to number of swaps and if exceeds shrink from left
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            res = max((r-l)+1, res)
        return res
             


        