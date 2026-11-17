class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = set()
        ans = []
        nums.sort()

        for i in range(len(nums)):
            l, r = i+1, len(nums) - 1
            
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                tri = (nums[i], nums[l], nums[r])

                if total == 0 and tri not in s:
                    s.add(tri)
                    ans.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                
                elif total < 0:
                    l += 1
                
                else:
                    r -= 1
        return ans