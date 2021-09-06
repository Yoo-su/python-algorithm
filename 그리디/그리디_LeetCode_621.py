from typing import List
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """이 문제 아이디어는 다음과 같다. 
        가장 많이 존재하는 문자를 n을 고려해서 먼저 세워보고, idle에
        남은 문자들을 채우면 된다. 그다음 카운터를 보면서 동일 수만큼 나타난 문자가 있으면 +1씩 해준다
        n이 0인 경우를 고려해 특별히 처리한다.
        """
        res=0
        counter=Counter(tasks)

        max=counter.most_common(1)[0][1]

        res=(max-1)*(n+1)

        for task in counter:
            if counter[task]==max:
                res+=1
    
        if res<len(tasks):
            res=len(tasks)
        return res
    