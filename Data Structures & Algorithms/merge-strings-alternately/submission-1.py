class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = []
        l = r = 0
        n, m = len(word1), len(word2)
        while r < m and l< n:
            s.append(word1[l])
            s.append(word2[r])
            l += 1
            r += 1
        
        s.append(word1[l:])
        s.append(word2[r:])
        
        return "".join(s)