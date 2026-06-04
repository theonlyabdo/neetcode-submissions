class Solution:
    def maxArea(self, heights: list[int]) -> int:
        i = 0
        j = len(heights)-1
        amount = 0

        while i <= j:
            cur = (j - i) * min(heights[i], heights[j])
            amount = max(amount, cur)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return amount