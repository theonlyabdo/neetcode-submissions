class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        op ="{[(" 
        cl =")]}" 
        for c in s:
            if c in op:
                stack.append(c)
                print(stack)
            elif c in cl and len(stack) != 0:
                pop = stack.pop()
                if (pop == '[' and c != ']' ) or (pop == '(' and c != ')' ) or (pop == '{' and c != '}'):
                    return False
            elif c in cl and len(stack) == 0:
                return False
        if len(stack) != 0:
            return False
        else:
            return True

                      

            
        