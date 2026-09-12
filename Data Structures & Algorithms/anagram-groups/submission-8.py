class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mymap = {}

        for s in strs:
            key = tuple(sorted(s))
            if key not in mymap:
                mymap[key] = []
            mymap[key].append(s)

        return list(mymap.values())