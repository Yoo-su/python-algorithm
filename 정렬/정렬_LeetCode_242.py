from typing import List

def quick(nums, left, right):
    if left>=right:
        return
    
    pivot=nums[left]
    print(pivot)
    l, r = left+1, right

    while l<r:
        while l<right and nums[l]<=pivot:
            l+=1
        while r>left and nums[r]>pivot:
            r-=1

        if l<r:
            nums[l] , nums[r] = nums[r] , nums[l]

    if pivot>nums[r]:
        nums[left], nums[r] = nums[r], pivot
        
    quick(nums,left,r-1)
    quick(nums,r+1,right)

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        quick(nums,0,len(nums)-1)

            
sol=Solution()
sol.sortColors([6,4,2,5,8])
