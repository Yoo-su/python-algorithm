from collections import deque
 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root:TreeNode) -> int:
        if root is None:
            return 0
        deq=deque([root])
        depth=0
        
        while deq:
            depth+=1

            for _ in range(len(deq)):
                cur_root=deq.popleft()
                if cur_root.left:
                    deq.append(cur_root.left)
                if cur_root.right:
                    deq.append(cur_root.right)


        return depth

sol=Solution()

print(sol.maxDepth([3,9,0,20,None,None,15,7]))