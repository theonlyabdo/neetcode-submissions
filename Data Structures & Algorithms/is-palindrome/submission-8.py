class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for c in s:
            if c.isalnum():
                st += c.lower()

        n = len(st)
        if n % 2 == 0:
            return st[:n//2] == st[n//2:][::-1]
        else:
            return st[:n//2] == st[n//2+1:][::-1]