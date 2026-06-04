class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        heap = []

        #print(frequency.keys())
        for num, count in frequency.items():
            heapq.heappush(heap, (-count, num))

        ans = []
        for i in range(k):
            c, n = heapq.heappop(heap)
            ans.append(n)
        return ans
        