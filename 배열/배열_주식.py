import sys

#부르트포스, 시간초과
def sol(nums:list):
    result=0
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            result=max(result,nums[j]-nums[i])

    return result

#O(n)의 결과를 내는 방법..
"""생각해내기 어려운 방법이다..
"""
def sol2(nums:list):
    profit=0
    min_profit=sys.maxsize

    for item in nums:
        #가장 작은 값을 매번 비교하며 찾음
        min_profit=min(item, min_profit)

        #이익도 매번 새로 확인한다. 현재 item에서 최소값을 빼서 나온 이익과 이전 이익 중 큰값 선택
        profit=max(profit, item-min_profit)
    
    return profit


testCase=[7,1,5,3,6,4]
print(sol2(testCase))