class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ''
        l = r = 0
        n, m = len(word1), len(word2)
        while r < m and l< n:
            s = s + word1[l] + word2[r]
            l += 1
            r += 1
        
        if r < m:
            s = s + word2[r:m]
        
        if l < n:
            s = s + word1[l:n]
        
        return s