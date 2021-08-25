def quickSort(nums):
    def partition(l, r):
        left,right=l,r
        if left>=right:
            return
        
        pivot=nums[l]
        
        while left<right:
            while nums[left]<=pivot and left<r:
                left+=1
            while nums[right]>=pivot and right>l:
                right-=1

            #left, right 값 swap
            if left<=right:
                nums[left], nums[right]= nums[right], nums[left]

        #pivot 배치
        nums[right],nums[l]=nums[l], nums[right]
        
        partition(l,right-1)
        partition(right+1,r)

    partition(0,len(nums)-1)

    return nums

test=[5,4,3,2,1,8,8,9,11,11,7,6]

print(quickSort(test))

