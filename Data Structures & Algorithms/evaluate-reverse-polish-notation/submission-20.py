class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = set('/*-+')
        st = []

        for t in tokens:
            if t in op:
                n1 = st.pop()
                n2 = st.pop()
                if t == '-':
                    st.append(n2 - n1)
                elif t == '+':
                    st.append(n2 + n1)
                elif t == '*':
                    st.append(n2 * n1)
                else:
                    st.append(int(n2 / n1))
            else:
                st.append(int(t))
        return st.pop()