import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]
        for item in nums:
            heapq.heappush(heap,-item)
        result=0
        print(heap)

        for i in range(k):
            result=heapq.heappop(heap)

        return -result

sol=Solution()

print(sol.findKthLargest([3,2,3,1,2,4,5,5,6],4))