class Solution:
    def findMin(self, nums: List[int]) -> int:
        tmp = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                tmp = min(tmp, nums[l])
                break

            m = l + (r - l) //2

            tmp = min(tmp, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1

            else:
                r = m - 1
        return tmp
