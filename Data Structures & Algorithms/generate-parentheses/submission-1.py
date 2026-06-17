class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(openp, closep, cur):
            if len(cur) == n *2:
                res.append(cur)
                return 
            
            if openp < n:
                backtrack(openp+1, closep,cur+'(')


            if closep < openp:
                backtrack(openp, closep+1,cur+')')
        
        backtrack(0,0, "")
        return res


