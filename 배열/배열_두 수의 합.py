##여러 방법들

#브루트 포스
def sol1(nums:list,target:int):
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]


#파이썬 in 사용
def sol2(nums:list, target:int):
    for i,n in enumerate(nums):
        need=target-n

        if need in nums[i+1:]:
            return [i,nums[i+1:].index(need)+i+1]

        
#추가 딕셔너리 사용
def sol3(nums:list, target:int):
    myDict={}

    #원래 배열에서의 원소를 키로, 인덱스를 value로..
    for i,num in enumerate(nums):
        need=target-num
        if need in myDict:
            return [myDict[need],i]
        myDict[num]=i
        
    


test=[2,7,11,13]
target=9
print(sol3(test,target))