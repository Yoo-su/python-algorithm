from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    result=0
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0
            
            left,right=dfs(node.left), dfs(node.right)

            if node.left!=None and node.left.val==node.val:
                left+=1 
            else:
                left=0   
            if node.right!=None and node.right.val==node.val:
                right+=1
            else:
                right=0

            self.result=max(self.result, left+right)

            #단순 직경을 구할 땐 자기자신을 고려해 +1을 해줬지만 이 문제에선 val이 같은 경우 +1
            return max(left,right)

        dfs(root)
        return self.result


            