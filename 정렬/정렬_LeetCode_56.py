from typing import List
from collections import deque

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res=[]

        for item in intervals:
            if res and res[-1][1]>=item[1]:
                continue
            elif res and res[-1][1]>=item[0]:
                res[-1][1]=item[1]
            else:
                res.append(item)

        return res