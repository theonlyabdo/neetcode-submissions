class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distanceheap = []

        for point in points :
            distance = (point[0] **2 + point[1] **2) ** 0.5
            heapq.heappush(distanceheap, (distance, point))
        
        sol = []
        while len(sol) < k:
            _, point = heapq.heappop(distanceheap)
            sol.append(point)
        
        return sol