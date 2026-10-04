class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfDigits(n):
            total = 0
            while( n > 0):
                carry = n % 10
                n = n // 10
                total = total + ( carry ** 2 )
            return total
        
        seen = set()
        happy = 0
        
        while(n != 1):
            happy = sumOfDigits(n)
            if happy in seen:
                return False
            else:
                seen.add(happy)
                n = happy
        return True

            