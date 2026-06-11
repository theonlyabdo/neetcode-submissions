class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'}': '{', ']':'[', ')':'('}
        st = []
        
        for char in s:
            if char in pairs:
               if not st or pairs[char] != st.pop():
                return False

            else:
                st.append(char)
                
        if st: return False
        return True