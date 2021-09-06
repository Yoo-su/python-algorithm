from typing import List
import heapq

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap=[]
        res=[]

        for p in people:
            #파이썬이 최소힙만 지원해서 음수로 넣음
            heapq.heappush(heap,(-p[0], p[1]))

        #제일 키큰넘부터 빼서 리스트에 끼어맞추면 된다
        while heap:
            p=heapq.heappop(heap)
            res.insert(p[1], [-p[0],p[1]])

        return res        


sol=Solution()
print(sol.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))