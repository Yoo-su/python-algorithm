#enumerate 쓰면 더 좋다는거 알아두자.
def solution(temperatures:list):
    stack=[]
    result=[0]*len(temperatures)

    """핵심은 스택에 온도와 인덱스를 튜플형태로 같이 넣는다는 것,
        그리고 while문을 통해 이전 온도들이 현재 온도보다 낮은동안
        다 걸린 날짜를 처리해준다는 것"""
    for i in range(len(temperatures)):
        while stack and stack[-1][0]<temperatures[i]:
            tmp=stack.pop()

            #result배열에서의 자기 인덱스에 걸린 일수 기입
            result[tmp[1]]=i-tmp[1]

        stack.append((temperatures[i],i))    

    return result


T=[73,74,75,71,69,72,76,73]

res=solution(T)
