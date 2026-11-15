class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        frequency = Counter(nums)

        for num, freq in frequency.items():
            heapq.heappush(heap, (-freq,num))
        
        ans = []
        for i in range(k):
            freq, num = heapq.heappop(heap)
            ans.append((num))
        
        return ans