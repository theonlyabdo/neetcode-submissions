class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in range(len(stones)):
            heapq.heappush(heap,-stones[i])
        
        while len(heap) >= 2:
            st1 = -heapq.heappop(heap)
            st2 = -heapq.heappop(heap)
            if st1 == st2:
                continue
            else:
                maxstone = max(st1,st2)
                minstone = min(st2,st1)
                heapq.heappush(heap,-(maxstone - minstone))
        if len(heap) == 1: return -heap[0]
        else: return 0