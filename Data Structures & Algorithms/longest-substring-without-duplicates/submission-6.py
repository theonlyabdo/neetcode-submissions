class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()

        maxlen, l = 0, 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            w = (r - l) + 1
            maxlen = max(maxlen, w)
            seen.add(s[r])
        return maxlen