from collections import deque

class TreeNode(object):
    def __init__(self,x) -> None:
        self.val=x
        self.left=None
        self.right=None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '#'
        deq=deque([root])
        result=['#']

        while deq:
            node=deq.popleft()
            if node:
                result.append(str(node.val))
                deq.append(node.left)
                deq.append(node.right)
            else:
                result.append('#')
        
        return result


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data=='#':
            return None
        deq=deque(data[1:])
        root=TreeNode(deq.popleft())

        index,trees=0,[root]
        
        while deq:
            node=deq.popleft()
            node2=deq.popleft()

            if node!='#':
                tree=TreeNode(node)
                trees[index].left=tree
                trees.append(tree)
            if node2!='#':
                tree2=TreeNode(node2)
                trees[index].right=tree2
                trees.append(tree2)
            
            index+=1

        return trees[0]