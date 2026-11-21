class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        op = {'(':')','{':'}','[':']'}

        for c in s:
            if c in op:
                st.append(c)
            else:
                
                if not st or op[st.pop()] != c:
                    return False 
        
        return len(st) == 0