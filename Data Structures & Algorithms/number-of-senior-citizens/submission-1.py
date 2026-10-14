class Solution:
    def countSeniors(self, details: List[str]) -> int:
        seniors = 0
        for s in details:
            # print(f"{s} {s[12]}{s[13]}")
            if int(s[11]) > 6 or (int(s[11]) == 6 and int(s[12])>0):
                seniors += 1
            
        
        return seniors