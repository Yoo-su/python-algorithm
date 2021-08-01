from collections import Counter


def sol(nums:list,k:int):
    result=[]
    c=Counter(nums)
    
    #(숫자, 숫자 등장횟수) 튜플을 result에 삽입
    for item in c:
        result.append((item, c[item]))
    
    #등장 횟수를 기준으로 정렬
    result.sort(key=lambda x:x[1])

    realResult=[]

    #많이 등장한 순서대로 k개까지 pop해서 뽑음 
    for i in range(len(result)):
        if len(realResult)==k:
            break
        realResult.append(result.pop()[0])
    
    return realResult

print(sol([3,0,1,0],1))
