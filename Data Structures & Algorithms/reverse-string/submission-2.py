class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        st = []
        for i in range(len(s)):
            st.append(s[i])
        for i in range(len(s)):
            s[i] = st.pop()