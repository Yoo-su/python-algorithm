from typing import List
import functools

class Solution():
    def largestNumber(self, nums):
        nums=list(map(str,nums))
        
        nums.sort(key=lambda x:x*10, reverse=True)
        print(list(map(lambda x:x*10,nums)))
        return str(int(''.join(nums)))

    def largestNumber2(self, nums):
        nums=list(map(str,nums))
        
        def custom(n1:str, n2:str):
            if n1[0]>n2[0]:
                return True
            elif n1+n2<n2+n1:
                return -1
            else:
                return 0

        nums.sort(key=functools.cmp_to_key(custom), reverse=True)
        
        return str(int(''.join(nums)))

sol=Solution()

print(sol.largestNumber2([5,51,53,9,4]))
        
