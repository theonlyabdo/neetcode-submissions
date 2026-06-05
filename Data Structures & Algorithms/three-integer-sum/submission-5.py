class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        s = set()

        for i in range(len(nums)):
            j = i+1
            k = len(nums) - 1
            while j < k:
                tri = (nums[i], nums[j], nums[k])
                if nums[i] + nums[j] + nums[k] == 0 and tri not in s:
                    result.append(list(tri))
                    s.add(tri)
                    k -= 1
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
        return result
                    
            