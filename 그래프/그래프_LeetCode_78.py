from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results=[]

        def dfs(start,arr):
            results.append(arr)

            for i in range(start, len(nums)):
                dfs(i+1, arr+[nums[i]])

        dfs(0,[])
        return results

sol=Solution()
print(sol.subsets([1,2,3]))