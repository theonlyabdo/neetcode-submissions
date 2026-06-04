class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = []
       
        for row in matrix:
            s = set(row)
            if target in s:
                nums = row
        
        return True if nums else False
        # if not nums:
        #     return False
       