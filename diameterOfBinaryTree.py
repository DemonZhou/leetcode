# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 1
        if not root:
            return 0
        
        def getMaxDepth(node):
            if not node:
                return 0
            L = getMaxDepth(node.left)
            R = getMaxDepth(node.right)
            self.ans = max(self.ans , L + R + 1)
            return max(L , R) + 1
        getMaxDepth(root)
        return self.ans - 1