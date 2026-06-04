class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        l,r = 0,1
        while r != len(prices):
            if prices[l] > prices[r]:
                l = r
            buy = prices[r] - prices[l]
            p = max(buy,p)
            r+=1
        return p
