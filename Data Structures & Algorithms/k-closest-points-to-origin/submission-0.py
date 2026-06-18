class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distanceheap = []

        for i in range(len(points)) :
            distance = (points[i][0] **2 + points[i][1] **2) ** 0.5
            heapq.heappush(distanceheap, (distance, i))
        
        sol = []
        while len(sol) < k:
            distance, i = heapq.heappop(distanceheap)
            sol.append(points[i])
        
        return sol