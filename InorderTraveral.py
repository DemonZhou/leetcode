# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []

        def traversal(node):
            if node:
                traversal(node.left)
                res.append(node.val)
                traversal(node.right)
        
        traversal(root)
        return res