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

