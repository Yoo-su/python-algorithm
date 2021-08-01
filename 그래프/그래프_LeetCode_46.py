from itertools import permutations

class Solution:
    def permute(self, nums):
        results=[]
        
        def dfs(depth,main):
            if depth==len(nums)-1:
                results.append(main)
                return
            
            sub=list(set(nums)-set(main))
            
            for e in sub:
                next_main=main+[e]
                dfs(depth+1,next_main)
        
        for e in nums:
            dfs(0,[e])
        
        return results

sol=Solution()
print(list(permutations([1,2,3])))