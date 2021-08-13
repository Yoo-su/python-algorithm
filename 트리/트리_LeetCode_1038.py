class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    value=0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            #맨 우측으로 이동
            self.bstToGst(root.right)

            #누적값에 현재 노드의 값을 더헤주고
            self.value+=root.val

            #노드의 값을 현재까지의 누적값으로 설정
            root.val=self.value

            #왼쪽도 확인해서 누적값 업데이트
            self.bstToGst(root.left)

        return root
        
        



            