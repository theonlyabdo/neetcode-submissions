class Solution:

    def encode(self, strs: List[str]) -> str:
        st = ''

        for s in strs:
            st = st + str(len(s)) + '#' + s

        return st

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0

        while i < len(s):
            n = ''

            # Read the length
            while s[i] != '#':
                n += s[i]
                i += 1

            # Skip '#'
            i += 1

            # Read the string
            length = int(n)
            res.append(s[i:i + length])

            # Move to the next encoded string
            i += length

        return res