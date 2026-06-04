class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []

        for n, c in freq.items():
            heapq.heappush(heap,(-c, n))

        sol= []
        for i in range(k):
            sol.append(heapq.heappop(heap)[1])     

        return sol      
            