from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq, ans = deque(), []

        for i in range(len(nums)):
            # 앞에서부터 out of window -> 제거
            while deq and i-deq[0] == k:
                deq.popleft()

            # 뒤에서부터 현재 추가할 숫자보다 작으면 -> 제거 (deq에 불필요한 숫자 없도록!)
            while deq and nums[deq[-1]] <= nums[i]:
                deq.pop()

            deq.append(i) # 현재 숫자 추가( (i, num[i])로 저장해도 되나, 숫자 위치 저장만 해 space 줄임)

            # 출력 부분 (현재 위치 >= window size일 때)
            if i+1 >= k:
                ans.append(nums[deq[0]])  # 맨 앞은 현재 window 에서 가장 큰 수

        return ans
            

        
        
            



    
sol=Solution()

print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))