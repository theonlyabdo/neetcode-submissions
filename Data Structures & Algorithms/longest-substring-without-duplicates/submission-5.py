class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left, maxlen = 0,0 
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            w = (right - left) + 1
            maxlen = max(maxlen,w)
            seen.add(s[right])
        return maxlen