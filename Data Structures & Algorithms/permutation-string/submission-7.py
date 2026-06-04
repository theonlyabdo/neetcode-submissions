class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l,r = 0 , len(s1)
        c1 = Counter(s1)

        while r <= len(s2):
            if Counter(s2[l:r]) == c1:
                return True
            l += 1
            r += 1
        return False
        