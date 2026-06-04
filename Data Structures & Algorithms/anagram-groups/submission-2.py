class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for str in strs:
            k = tuple(sorted(str))
            if k not in group:
                group[k] = []
            group[k].append(str)

        return list(group.values())
