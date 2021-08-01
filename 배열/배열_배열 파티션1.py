#정렬 후 두개씩 차례로 묶어주면 끝 
def sol(nums:list) ->  int:
    nums.sort()

    count,sum=0,0
    for i in range(len(nums)-1,-1,-2):
        count+=1

        sum+=min(nums[i],nums[i-1])

        if count==len(nums)//2:
            return sum

#python다운 방식
def sol2(nums:list) -> int:
    return sum(sorted(nums)[::2])

testCase=[1,4,3,2,5]

print(sol(testCase))