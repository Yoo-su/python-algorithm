from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points,key=lambda x:abs(x[0]**2+x[1]**2))[:k]

    
    def kClosest2(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]

        for (x,y) in points:
            dist=x**2 + y**2
            heapq.heappush(heap, (dist,x,y))

        result=[]
        for _ in range(k):
            (dist, x, y)=heapq.heappop(heap)
            result.append((x,y))

        return result





sol=Solution()

print(sol.kClosest([[3,3],[5,-1],[-2,4]],2))