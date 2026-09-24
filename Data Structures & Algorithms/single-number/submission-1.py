class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = nums[0]
        for i in range(1,len(nums)):
            ans = ans ^ nums[i]
            print(f"{ans},")
        print(2 ^ 3)
        print((((2 ^ 3) ^ 3)^6)^2)
        return ans