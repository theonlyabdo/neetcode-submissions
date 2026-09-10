class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {'+','-','/','*'}

        st = []
        for t in tokens:
            if t in operations and len(st)>=2:
                num1 = st.pop()
                num2 = st.pop()

                if t == '+':
                    st.append(num1 + num2)
                elif t == '-':
                    st.append(num2 - num1)
                elif t == '/':
                    st.append(int(num2 / num1))
                else:
                    st.append(num2 * num1)
            else:
                st.append(int(t))
        return st[0]