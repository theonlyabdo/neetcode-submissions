class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        maxheap = []

        for num,freq in frequency.items():
            heapq.heappush(maxheap, (-freq,num))
        
        ans = []
        for i in range(k):
            c,n = heapq.heappop(maxheap)
            ans.append(n)

        return ans