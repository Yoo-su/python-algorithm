from collections import defaultdict, deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n<=1:
            return [0]

        dic = defaultdict(list)

        for a, b in edges:
            dic[a].append(b)
            dic[b].append(a)

        leaves = deque()

        for i in range(n):
            if len(dic[i]) == 1:
                leaves.append(i)

        #최소높이를 만드는 루트가 최대 두개가 나올 수 있기 때문에 조건을 이렇게 설정
        while n > 2:
            n -= len(leaves)
            new_leaves = deque()

            for leaf in leaves:
                #리프노드의 이웃을 추출
                neighbor = dic[leaf].pop()

                #해당 이웃 노드에서 리프를 제거
                dic[neighbor].remove(leaf)

                #이웃노드녀석이 리프가 되었으면 새로운 리프노드 리스트에 추가해준다
                if len(dic[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves
        
        return leaves


sol = Solution()

#print(sol.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]))
print(sol.findMinHeightTrees(6,[[3,0],[3,1],[3,2],[3,4],[5,4]]))
