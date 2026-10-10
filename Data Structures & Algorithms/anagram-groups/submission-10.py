class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mymab = {}

        for s in strs:
            k = tuple(sorted(s))
            if k not in mymab:
                mymab[k] = []
            mymab[k].append(s)
        
        return list(mymab.values())

             