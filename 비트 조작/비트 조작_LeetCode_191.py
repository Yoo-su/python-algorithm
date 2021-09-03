class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n^0).count("1")


sol=Solution()
sol.hammingWeight("00000000000000000000000000001011")