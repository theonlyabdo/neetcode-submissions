class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0,0
        profit = 0

        while r!=len(prices):
            if prices[l] > prices[r]:
                l = r
            buy = prices[r] - prices[l]
            profit = max(profit,buy)
            r+=1
        return profit
                