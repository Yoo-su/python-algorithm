from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=set()

        nums1.sort()

        for item in nums2:
            left,right=0,len(nums1)-1
            while left<=right:
                mid=left+(right-left)//2

                if nums1[mid]>item:
                    right=mid-1
                elif nums1[mid]<item:
                    left=mid+1
                elif nums1[mid]==item:
                    res.add(item)
                    break
        
        return res

sol=Solution()

print(sol.intersection([1,2,2,1],[2,2]))


                