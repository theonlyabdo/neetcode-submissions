class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = []
        l = r = 0
        n, m = len(word1), len(word2)
        while r < m or l< n:
            if l<n : s.append(word1[l])
            if r<m : s.append(word2[r])
            
            l += 1
            r += 1
        
        return "".join(s)