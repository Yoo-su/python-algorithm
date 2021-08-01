import collections 

def solution(strings:list):
    #defaultdict 인자로 주는 것 -> 딕셔너리에서 value의 타입
    myDict=collections.defaultdict(list)

    for word in strings:
        #문자열 sort결과는 리스트형태임을 기억하자
        tmp=''.join(sorted(word))

        myDict[tmp].append(word)

    return list(myDict.values())


inputEX=["eat","tea","tan","ate","nat","bat"]
print(solution(inputEX))

