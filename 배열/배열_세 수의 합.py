import sys
import collections
import timeit

"""먼저 배열을 정렬한 후 합이 0이 되는 세 수를 찾는다.
정렬이 되어있으므로 몇가지 고려할 게 있다. 다음에 올 수들은 현재 인덱스의 수보다
같거나 클 것이므로 중복된 수가 나온다면 패스해야 한다. 

시간복잡도를 줄이기 위해 투포인터 방식을 사용하고, 기준이 되는 것은 현재 인덱스 i이다.
세 수의 합이 0보다 작으면 left를 +1해주고, 0보다 크면 right을 -1해준다. 
세 수의 합이 0이 되는 경우는 결과 리스트에 추가해주고 그 떄의 left와 right 각각의 오른, 왼쪽에
중복된 수가 있으면 다 넘겨줘야한다. 다 넘기고 다음 수를 보기 위해 다시 각각을 +1, -1 해주는 것.
"""
def sol(nums:list):
    start=timeit.default_timer()
    result=[]
    nums.sort()

    for i in range(len(nums)-2):
        #이미 정렬된 배열이므로 중복 피해야함 다음에 오는 수들은 다 더 큰 양수라서
        if i>0 and nums[i]==nums[i-1]:
            continue

        left,right=i+1,len(nums)-1
        while left<right:
            sum=nums[i]+nums[left]+nums[right]

            if sum<0:
                left+=1
            elif sum>0:
                right-=1
            else:
                result.append([nums[i],nums[left],nums[right]])

                while left<right and nums[left]==nums[left+1]:
                    left+=1
                while left<right and nums[right]==nums[right-1]:
                    right-=1
                left,right=left+1,right-1

    delay=timeit.default_timer()-start     
    print(delay)
    return result


testCase=[-1,0,1,2,-1,-4]

res=sol(testCase)

print(res)