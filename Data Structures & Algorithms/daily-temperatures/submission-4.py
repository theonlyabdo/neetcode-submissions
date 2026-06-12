class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        sol = []

        for l in range(len(temperatures)):
            found = False
            for r in range(l+1, len(temperatures)):
                if temperatures[r]> temperatures[l]:
                    sol.append(r-l)
                    found = True
                    break
            if not found: 
                sol.append(0)
        return sol