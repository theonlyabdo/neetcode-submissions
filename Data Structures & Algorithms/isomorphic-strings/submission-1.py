class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        k = {}

        for i in range(len(s)):
            if s[i] in k:
                if k[s[i]] != t[i]:
                    return False
            else:
                if t[i] in k.values():
                    return False
                k[s[i]] = t[i]

        return True
