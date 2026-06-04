class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strd = ""
        for d in digits:
            strd += str(d)
        res = str(int(strd) + 1)
        sol = []
        for d in res:
            sol.append(int(d))
        return sol
        
        