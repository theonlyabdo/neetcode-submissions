class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for i in range(len(stones)):
            heapq.heappush(maxHeap, -stones[i])
        
        #print(maxHeap)
        while len(maxHeap) >= 2:
            stone1 = -1 * heapq.heappop(maxHeap) 
            stone2 = -1 * heapq.heappop(maxHeap)
            if stone1 == stone2:
                continue
            elif  stone1 > stone2:
                newstone = stone1 - stone2
                heapq.heappush(maxHeap,-newstone)
            
        return -maxHeap[0] if maxHeap else 0