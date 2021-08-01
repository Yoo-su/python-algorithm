from typing import List
import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=defaultdict(list)
        
        for a,b,c in times:
            graph[a].append((b,c))
        
        Q=[(0,k)]
        dist=defaultdict(int)
        while Q:
            print(dist)
            time,node=heapq.heappop(Q)

            #해당 노드로 가는 최소비용에 대한 정보가 등록되어 있지 않으면 등록
            if node not in dist:
                dist[node]=time
                for a,b in graph[node]:
                    alt=time+b
                    heapq.heappush(Q,(alt,a))

        if len(dist)==n:
            return max(dist.values())
        return -1


"""
다익스트라 알고리즘의 구현에서 핵심이 되는 부분을 정리해보자.
출발 노드로부터 시작해 도달 가능한 인접 노드들 중 최소 비용으로 갈 수 있는
노드를 선택하는데, 이 최소 비용 노드를 선택하기 위해 우선순위 큐(heapq)를 사용한다.

하나의 노드를 선택해 이동했으면 해당 노드와 인접해 있는 다른 노드들로 가는 비용을 다시 계산한다. 
heapq에 삽입하면 자동으로 
"""