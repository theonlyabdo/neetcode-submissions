class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = set()
        res = []
        nums.sort()

        for i in range(len(nums)):
            j, k = 1 + i, len(nums)-1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                tri = (nums[i], nums[j], nums[k]) 

                if (total == 0 and tri not in s):
                    s.add(tri)
                    res.append(list(tri))
                    j += 1   # ✅ move pointers
                    k -= 1
                

                elif total < 0:
                    j += 1
                else:
                    k -= 1
        return list(res)

                    