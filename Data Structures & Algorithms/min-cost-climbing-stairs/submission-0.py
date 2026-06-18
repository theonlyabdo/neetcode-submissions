class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        mincost = [0,0]
        for i in range(2,n+1):
            nextcost = min(mincost[i-2] + cost[i-2], 
                           cost[i-1] + mincost[i-1])
            
            mincost.append(nextcost)
        return mincost[-1]