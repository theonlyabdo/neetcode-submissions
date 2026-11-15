class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)

        for s in strs:
            k = tuple(sorted(s))
            if k in m:
                m[k].append(s)
            else:
                m[k] = [s]
        
        return list(m.values())