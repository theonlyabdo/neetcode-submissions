class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        nums = []
        for i in range(rows):
            s = set(matrix[i])
            if target in s:
                nums = matrix[i]
                break
        if len(nums) == 0:
            return False 

        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return True
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return False
