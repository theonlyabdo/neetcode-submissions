class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        prof = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                buy = prices[r] - prices[l]
                prof = max(prof,buy)
            else:
                l = r
            r+=1
        return prof


                         
            
            
        '''
            [7,1,5,3,6,4]
        '''