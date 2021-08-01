from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    longest:int=0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node)->int:
            if not node:
                return 0

            left=dfs(node.left)
            right=dfs(node.right)

            #현재 노드 기준 가장 긴 경로는 왼쪽 최대깊이+오른쪽 최대깊이로 계산
            self.longest=max(self.longest, left+right)

            #왼쪽과 오른쪽 중 더 큰 깊이값에 1을 더해(현재노드) 리턴
            return max(left,right)+1


        dfs(root)
        return self.longest
