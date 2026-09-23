class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) >= 2:
            st1 = -heapq.heappop(heap)
            st2 = -heapq.heappop(heap)

            if st1 != st2:
                heapq.heappush(heap, -(st1 - st2))

        if heap:
            return -heap[0]

        return 0