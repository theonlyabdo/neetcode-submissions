class Solution:
    def isValid(self, s: str) -> bool:
        st =[]
        opening = set('[{(')
        closing = set(')}]')

        for c in s:
            if c in opening:
                st.append(c)
            
            elif c in closing and len(st) != 0:
                pop = st.pop()
                if (pop == '[' and c != ']' ) or (pop == '(' and c != ')' ) or (pop == '{' and c != '}'):
                    return False
            
            elif c in closing and len(st) == 0:
                return False
        
        if len(st) != 0:
            return False
        return True