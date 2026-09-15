class Solution:
    def isValid(self, s: str) -> bool:
        myMap = {'}':'{', ')':'(', ']':'['}
        st = []


        for c in s:
            if c in myMap.values():
                st.append(c)
            
            else:
                if not st or myMap[c] != st[-1]:
                    return False
                
                st.pop()
        
        return len(st) == 0