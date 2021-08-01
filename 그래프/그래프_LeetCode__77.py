from itertools import combinations
class Solution:
    def combine(self, n: int, k: int):
        nums=[num+1 for num in range(n)]
        result=[]

        def dfs(start,depth,combination):
            if depth==k:
                result.append(combination)
                return

            for i in range(start, len(nums)):
                dfs(i+1,depth+1,combination+[nums[i]])

        dfs(0,0,[])
        return result
        
sol=Solution()
#print(list(map(list,combinations([1,2,3,4],2))))
print(sol.combine(4,2))

"""
입력 (4,2)를 예로 들어보자. [1,2,3,4]에서 크기 2의 조합을 구하는 과정이다.
먼저 dfs(0,0,[]) 호출을 통해 시작하게 되면 for i in range(0,4)의 반복문 안에서 

깊이0 // dfs(1,1,[]+[1]), dfs(1,1,[]+[2]), dfs(1,1,[]+[3]), dfs(1,1,[]+[4])이 차례로 호출된다. 

깊이1 // dfs(2,2,[1]+[2]), dfs(2,2,[1]+[3]), dfs(2,2,[1]+[4])  이런식으로 최종 깊이에 도달할 떄까지
조합을 구한다. 

"""