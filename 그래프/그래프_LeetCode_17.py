class Solution:
    def letterCombinations(self, digits: str):
        dic={'2':'abc','3':'def','4':'ghi','5':'jkl',
        '6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        result=[]
        
        if digits=='':
            return []

        def dfs(depth, word):
            if depth==len(digits):
                result.append(word)
                return

            for i in range(len(dic[digits[depth]])):
                dfs(depth+1,word+dic[digits[depth]][i])

            
        dfs(0,"")

        return result
            


sol=Solution()

print(sol.letterCombinations("23"))

