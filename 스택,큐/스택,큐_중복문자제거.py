
from os import dup
from collections import Counter

#스택을 사용한 방법
def solution(s:str):
    counter,seen,stack=Counter(s),set(), []
    
    for char in s:
        #문자 카운트 하나 감소시켜주고, 문자가 이미 등장한 거면 continue
        counter[char]-=1
        if char in seen:
            continue

        #뒤에 붙일 문자가 남아있으면  스택에서 제거
        while stack and char<stack[-1] and counter[stack[-1]]>0:
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)
    
    return ''.join(stack)

            

print(solution('cbacdcbc'))
