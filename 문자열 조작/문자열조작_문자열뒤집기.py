import sys
import collections

#투 포인터를 이용한 swap
def solution1(arr):
    left,right=0,len(arr)-1
    
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1


#파이썬다운 방식
def solution2(arr):
    arr.reverse()
