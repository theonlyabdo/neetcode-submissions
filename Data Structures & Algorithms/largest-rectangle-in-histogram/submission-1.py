class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0

        for l in range(len(heights)):
            minHeight = float("inf")

            for r in range(l, len(heights)):
                minHeight = min(minHeight, heights[r])
                maxArea = max(
                    maxArea,
                    minHeight * (r - l + 1)
                )

        return int(maxArea)