class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            l = len(s)
            encoded_str += 'n' + str(l) + '#' + s

        return encoded_str


    def decode(self, s: str) -> List[str]:
        sol = []
        i = 0
        while i != len(s):
            if (s[i] == 'n'):
                i += 1  # skip the 'n'
                j = i
                while s[j] != '#':  # read until '#'
                    j += 1
                l = int(s[i:j])

                sol.append(s[j+1:j+l+1])  # skip '#'
                i = 1 + j + l
            #print(sol)
        return sol

