from typing import List
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        dic=defaultdict(list)
        visited=set()
        ordered=[]

        for a,b in prerequisites:
            dic[a].append(b)
        
        global check
        check=True

        def dfs(course):
            global check
            
            #순환구조인지 판단하기 위해 DFS 수행. 
            if dic[course]:
                dfs(dic[course].pop(0))

            if course in visited:
                check=False
                return
            visited.add(course)
            

        keys=list(dic.keys())

        #키가 더이상 없을 때까지 반복, 하지만 중간에 순환구조 발견 시 False 반환
        while keys:
            key=keys.pop(0)
            #하나의 키에 대한 연결요소가 더이상 없을 때까지 dfs 수행
            while dic[key]:
                dfs(key)
                
                if check==False:
                    return False
            
                check=True
                visited.clear()
            
        return True


sol=Solution()
print(sol.canFinish(5,[[1,4],[2,4],[3,1],[3,2]]))   #True
print(sol.canFinish(2,[[1,0],[0,1]]))    #False
print(sol.canFinish(3,[[2,1],[1,0]]))   #True
print(sol.canFinish(3,[[1,0],[2,0],[0,2]]))   #False
print(sol.canFinish(3,[[0,1],[0,2],[1,2]]))    #True
print(sol.canFinish(4,[[2,0],[1,0],[3,1],[3,2],[1,3]]))