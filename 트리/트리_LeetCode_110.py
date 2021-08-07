from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def check(node):
            if not node:
                return 0

            left = check(node.left)
            right = check(node.right)

            """자식노드를 가지는 어떤 노드 입장에서 자식간 불균형이 있으면 
            -1 값을 가지게 되므로 left와 right이 -1 인 경우도 포함"""
            if left == -1 or right == -1 or abs(left-right) > 1:
                return -1

            return max(left, right)+1

        return check(root) != -1
