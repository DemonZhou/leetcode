# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isSymmetricEX(root.left,root.right)
    def isSymmetricEX(self,r1,r2):
        if not r1 and not r2:
            return True

        if not r1 and r2:
            return False
        if not r2 and r1:
            return False
        
        return r1.val == r2.val and self.isSymmetricEX(r1.left, r2.right) and self.isSymmetricEX(r1.right,r2.left)
        