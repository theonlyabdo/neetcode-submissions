class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        ops = {"+", "-", "*", "/"}

        for c in tokens:
            if c not in ops:
                st.append(int(c))
            else:
                b = st.pop()
                a = st.pop()

                if c == "+":
                    st.append(int(b+a))
                elif c == "-":
                    st.append(int(a-b))
                elif c == "*":
                    st.append(int(b*a))
                else:
                    st.append(int(a/b))
        return st[-1]
                    

