class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            m = (r-l) + l // 2
            # print(f"m: {m}, num[m]:{nums[m]}")

            if nums[m] == target:
                # print(f"nums[m]: {nums[m]} == target:{target} ")
                return m
            
            elif nums[m] > target:
                # print(f"nums[m]: {nums[m]} > target:{target} ")
                r = m - 1
            
            else:
                # print(f"nums[m]: {nums[m]} < target:{target} ")
                l = m + 1
        return -1