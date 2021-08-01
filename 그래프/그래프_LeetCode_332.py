from typing import List
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        result=[]
        dic=defaultdict(list)
        
        for a,b in sorted(tickets):
            dic[a].append(b)

        def dfs(a):
            while dic[a]:
                dfs(dic[a].pop(0))
            result.append(a)
        
        dfs('JFK')
        print(result)
        return result[::-1]


sol=Solution()
r=sol.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","YOO"]])
print(r)

"""모든 티켓이 한번은 사용된다는 가정이 문제에 포함된다.
마지막 티켓을 제외하고 연결이 안되는 티켓은 없다.
"""