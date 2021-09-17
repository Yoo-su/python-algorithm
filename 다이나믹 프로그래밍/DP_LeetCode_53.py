from typing import List
import sys

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best=-sys.maxsize
        cur_sum=0

        for num in nums:
            cur_sum=max(num,cur_sum+num)
            best=max(best,cur_sum)

        return best