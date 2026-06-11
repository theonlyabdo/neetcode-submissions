class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = set('+-*/')
        st = []
        
        for token in tokens:
            if token in op:
                num2 = st.pop()
                num1 = st.pop()

                if token == '+': st.append(num1 + num2)

                if token == '-': st.append(num1 - num2)

                if token == '*': st.append(num1 * num2)

                if token == '/': st.append(int(num1 / num2))
            else:
                st.append(int(token))
        return st[-1]