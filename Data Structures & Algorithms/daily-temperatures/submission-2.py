class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while st and st[-1][0] < temperatures[i]:
                st_temp, st_ind = st.pop()
                result[st_ind] = i - st_ind
            st.append((temp,i))
            

        return result