class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for nums in matrix:
            l, r = 0, len(nums) -1
            
            while l <= r:
                m = l + (r - l) // 2
                print(nums[m])
                if nums[m] == target:
                    return True
                
                elif nums[m] < target:
                    l = m + 1
                
                else:
                    r = m - 1

        return False