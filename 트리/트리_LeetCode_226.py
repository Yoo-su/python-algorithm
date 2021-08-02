# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def dfsInvert(node):
            if not node:
                return
            
            node.left,node.right=node.right,node.left
            dfsInvert(node.left)
            dfsInvert(node.right)

        dfsInvert(root)

        return root

"""
트리의 리프노드부터 좌우를 변경하며 위로 올라간다. deque를 쓰면 책 예제처럼 24ms의 결과를 낼 수 있을 것 같다. 
"""
