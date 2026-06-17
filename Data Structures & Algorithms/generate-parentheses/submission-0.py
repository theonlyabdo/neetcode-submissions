class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sol, res = [], []


        def beacktrack(openp,closep):
            if len(sol) == n*2:
                res.append("".join(sol))
                return
            
            if openp < n:
                sol.append('(')
                beacktrack(openp+1, closep)
                sol.pop()
            
            if closep < openp:
                sol.append(')')
                beacktrack(openp, closep+1)
                sol.pop()
            
        
        beacktrack(0,0)
        return res