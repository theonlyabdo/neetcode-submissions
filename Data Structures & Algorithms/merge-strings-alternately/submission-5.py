class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l,r = 0,0
        n,m = len(word1), len(word2)
        s = []
        while l < n and r < m:
            s.append(word1[l])
            s.append(word2[r])
            l += 1
            r += 1
        
        while l < n:
            s.append(word1[l])
            l+= 1
        
        while r <m:
            s.append(word2[r])
            r+=1

        return ''.join(s)