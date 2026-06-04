class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        maxheap = []

        for num, fr in freq.items():
            heapq.heappush(maxheap, (-fr, num))

        ans = []
        for i in range(k):
            f, n = heapq.heappop(maxheap)
            ans.append(n)

        return ans