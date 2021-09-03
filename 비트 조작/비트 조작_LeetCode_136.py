from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result=0
        
        #0으로 시작해서 모든 리스트 요소와 XOR연산을 한 후엔 짝이 맞지 않는 요소만 남는다
        for num in nums:
            result^=num
        
        return result
    
sol=Solution()
sol.singleNumber([3,1,2,1,2])