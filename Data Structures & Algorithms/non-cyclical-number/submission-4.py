class Solution:
    def isHappy(self, n: int) -> bool:

        def sumOfDigits(n):
            total = 0

            while n > 0:
                digit = n % 10
                n //= 10
                total += digit ** 2

            return total

        slow = n
        fast = sumOfDigits(n)

        while fast != 1 and slow != fast:
            slow = sumOfDigits(slow)
            fast = sumOfDigits(sumOfDigits(fast))

        return fast == 1