class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for c in s:
            if c.isalnum():
                st += c.lower()
        
        l,r = 0, len(st)-1
        while l <= r:
            if st[l] != st[r]:
                return False
            l+=1
            r-=1
        return True

        # n = len(st)
        # print(st[0:n//2])
        # print(st[n:n//2:-1])
        # return st[0:n//2] == st[n:n//2:-1]
       
        
        
