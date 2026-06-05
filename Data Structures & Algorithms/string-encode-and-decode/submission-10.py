class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for string in strs:
            n = len(string)
            s = s + "n" + str(n) + '#' + string
        return s

    def decode(self, s: str) -> List[str]:
        sol = []
        i = 0
        while i < len(s):
            if s[i] == "n":
                i += 1
                j = i
                while s[j] != '#':
                    j += 1
                l = int(s[i:j])
                i = 1 + j + l
                sol.append(s[j+1:i])
        return sol