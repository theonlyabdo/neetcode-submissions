class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        replacments = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)

            if (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            replacments = max((r-l)+1,replacments)
        return replacments 

# so first we had to count the occurance of a charecter 
# in the string while expanding the window size, 
# then we can compare the width of window to the maximum occured character
# if exceeded k, then we move l and count it down
# then we update our maximum replacments