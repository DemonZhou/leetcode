# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        def findRight(node):
            if not node:
                return None
            
            if not node.right and not node.left:
                return node

            if not node.right:
                return findRight(node.right)
            else:
                return findRight(node.left)

        if not root:
            return

        head = root
        while head:
            if head.left:
                node = findRight(head.left)
                node.right = head.right
                head.right = node
                head.left = None

            head = head.right
            