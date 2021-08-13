from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    result=0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root:
            if root.val>=low and root.val<=high:
                self.result+=root.val
                self.rangeSumBST(root.left,low,high)
                self.rangeSumBST(root.right,low,high)
            elif root.val<low:
                self.rangeSumBST(root.right,low,high)
            else:
                self.rangeSumBST(root.left,low,high)
        
        return self.result