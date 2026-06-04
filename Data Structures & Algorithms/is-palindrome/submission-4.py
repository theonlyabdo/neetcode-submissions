class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for c in s:
            if c.isalnum():
                result += c
        result = result.lower()

        l = 0
        r = len(result) - 1
        #print(f"{r} {result}")
        while l <= r:
            #print(f"{result[l]} and {result[r]}")
            if result[l] != result[r]:
                print(f"{result[l]} != {result[r]}")
                return False
            r -= 1
            l += 1
        return True
        