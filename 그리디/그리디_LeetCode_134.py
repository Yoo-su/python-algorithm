from typing import List
import heapq

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1

        start,fuel=0,0

        #i가 유일한 출발점인 경우 더이상 start가 변경될 일이 없다.
        for i in range(len(gas)):
            if gas[i]+fuel<cost[i]:
                start=i+1
                fuel=0
            else:
                fuel+=gas[i]-cost[i]
        
        return start

sol=Solution()

print(sol.canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))