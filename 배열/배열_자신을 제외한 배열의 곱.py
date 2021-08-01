#어떻게 풀었는지 보고 풀어도 이해가 어렵다.
def sol(nums:list):
    out=[]

    tmp=1
    for i in range(len(nums)):
        out.append(tmp)
        tmp*=nums[i]

    tmp=1
    for i in range(len(nums)-1,-1,-1):
        out[i]*=(tmp)
        tmp*=nums[i]

    return out

testCase=[1,2,3,4]

print(sol(testCase))