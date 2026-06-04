class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = {}

        for s in strs:
            k = tuple(sorted(s))
            if k not in sol:
                sol[k] = []
            sol[k].append(s)
        return list(sol.values())
            