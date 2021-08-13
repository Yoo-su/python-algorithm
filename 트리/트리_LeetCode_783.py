from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    pre=float('-inf')
    result=float('inf')
    
    #중위순회가 핵심
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if not root:
            return

        self.minDiffInBST(root.left)

        self.result=min(self.result, abs(root.val-self.pre))

        self.pre=root.val

        self.minDiffInBST(root.right)

        return self.result


            
            