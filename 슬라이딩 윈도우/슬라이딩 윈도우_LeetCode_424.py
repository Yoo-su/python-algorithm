from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=right=0
        counts=Counter()

        for right in range(1,len(s)+1):
            #현재 문자 카운트 +1
            counts[s[right-1]]+=1

            #현재 최다 등장 문자 빈도수
            max_char_n=counts.most_common(1)[0][1]

            """k번만 변경해서 만들 수 없는 경우 다음 탐색을 위해
                left가 보고있는 문자의 카운트를 감소시키고 left는 하나 증가"""
            if right-left-max_char_n>k:
                #left를 하나 증가시키니까 그 자리에 있던 문자 등장 빈도도 하나 없애는 것
                counts[s[left]]-=1
                left+=1
        return right-left

    def replay(self, s:str, k:int)->int:
        left=right=0
        max_len=0
        counter=Counter()

        for right in range(len(s)):
            counter[s[right]]+=1

            #최다 등장 문자의 등장 횟수
            top_appear_n=counter.most_common(1)[0][1]

            if (right+1)-left-top_appear_n>k:
                counter[s[left]]-=1
                left+=1

        return (right+1)-left

        
        
