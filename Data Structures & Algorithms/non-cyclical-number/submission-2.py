class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n != 1:
            st = str(n)
            ln = len(st)
            sm = 0
            
            for i in range(ln):
                sm += int(st[i])*int(st[i])
            
            if sm in seen:
                return False
            
            seen.add(sm)
            n = sm
        return True
