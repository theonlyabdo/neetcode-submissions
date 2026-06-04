class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        op = {'+', '-', '*', '/'}

        for t in tokens:
            if t in op:
                num2 = numbers.pop()
                num1 = numbers.pop()

                if t == '+':
                    numbers.append(int(num1 + num2))
                elif t == '-':
                    numbers.append(int(num1 - num2))
                elif t == '*':
                    numbers.append(int(num1 * num2))
                else:
                    numbers.append(int(num1/num2))
            else:
                numbers.append(int(t))
        return numbers[-1]