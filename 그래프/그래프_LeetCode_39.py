from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results=[]

        def dfs(start,combination):
            if sum(combination)==target:
                results.append(combination)
                return
            elif sum(combination)>target:
                return

            for i in range(start,len(candidates)):
                dfs(i,combination+[candidates[i]])
            
        dfs(0,[])

        return results



sol=Solution()

print(sol.combinationSum([2,3,5],8))