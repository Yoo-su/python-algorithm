import sys

def solution(s:str):
    stack=[]
    table={'(':')', '{':'}','[':']'}

    for item in s:
        #여는괄호면 스택에 push
        if item in table:
            stack.append(item)
        #닫는괄호인데 스택이 비었거나, 매칭 안되면 False
        elif not stack or table[stack.pop()]!=item:
            return False
    
    #여는괄호 남았으면 False
    if stack:
        return False
    return True

test='['

print(solution(test))