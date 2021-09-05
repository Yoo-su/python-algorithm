from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #필요한 문자 각각의 개수
        need=Counter(t)
        
        #필요한 문자 전체 개수
        missing=len(t)

        left=start=end=0

        for right, char in enumerate(s,1):
            missing-=need[char]>0
            need[char]-=1

            if missing==0:
                while left<right and need[s[left]]<0:
                    print(need[s[left]])
                    need[s[left]]+=1
                    left+=1 

                #이 조건을 통해 더 짧은 결과가 있으면 업데이트한다.
                if not end or right-left<=end - start:
                    #구간 업데이트
                    start,end=left,right
                
                    need[s[left]]+=1

                    #다음 탐색을 위해 +1
                    missing+=1
                    left+=1
        return s[start:end]
        

sol=Solution()

sol.minWindow("ADOBECODEBANC","ABC")
