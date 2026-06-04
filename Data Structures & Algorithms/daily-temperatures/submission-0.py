class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []

        for l in range(len(temperatures)):
            found = False
            for r in range(l + 1, len(temperatures)):
                if temperatures[r] > temperatures[l]:
                    res.append(r - l)
                    found = True
                    break

            if not found:
                res.append(0)

        return res