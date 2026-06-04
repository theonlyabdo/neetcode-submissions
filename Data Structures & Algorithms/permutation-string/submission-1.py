class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = []
        if len(s1) > len(s2):
            return False
        l, r = 0, len(s1) 
        c1 = Counter(s1)
        while r <= len(s2):
            scompare = s2[l:r]
            c2 = Counter(scompare)
            print(f"c1:{c1}, c2:{c2}")
            if c2 == c1:
                return True
            l += 1
            r += 1
        return False
        

        
        