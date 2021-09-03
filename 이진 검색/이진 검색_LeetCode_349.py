from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=set()

        nums1.sort()

        for item in nums2:
            check=False
            left,right=0,len(nums1)-1
            while not check and left<=right:
                mid=left+(right-left)//2

                #print(left, right, mid, nums1[mid])
                if nums1[mid]>item:
                    right=mid-1
                elif nums1[mid]<item:
                    left=mid+1
                elif nums1[mid]==item:
                    check=True
                    res.add(item)
                    
        return res

    def intersection2(self, nums1, nums2):
        res=set()

        nums1.sort()
        nums2.sort()
        i=j=0

        while i<len(nums1) and j<len(nums2):
            if nums1[i]>nums2[j]:
                j+=1
            elif nums1[i]<nums2[j]:
                i+=1
            else:
                res.add(nums1[i])
                i+=1
                j+=1
        return res




sol=Solution()

print(sol.intersection([4,9,5],[9,4,9,8,4]))


                