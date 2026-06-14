class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # first find the break point
        while l < r:
            m = l + (r - l) // 2

            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        
        breakpoint = l

        l, r = 0, len(nums) - 1
        if target >= nums[breakpoint] and target <= nums[r]:
            l = breakpoint
        else:
            r = breakpoint
        
        while l <= r:
            m = l + ( r - l ) // 2

            if target == nums[m]:
                return m
            
            elif target > nums[m]:
                l = m + 1
        
            else:
                r = m - 1
        return -1
        

