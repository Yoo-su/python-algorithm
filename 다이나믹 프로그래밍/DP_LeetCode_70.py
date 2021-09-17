from collections import defaultdict

class Solution:
    dp=defaultdict(int)

    #메모이제이션을 활용한다
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        
        if self.dp[n]:
            return self.dp[n]
        
        self.dp[n]=self.climbStairs(n-2)+self.climbStairs(n-1)
        return self.dp[n]


        
sol=Solution()
print(sol.climbStairs(5))
