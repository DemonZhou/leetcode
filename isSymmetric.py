# Definition for a binary tree node.

import operator
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def cmpSubtree(self,left:TreeNode,right:TreeNode) -> bool:
        if left == None and right == None:
            return True
        if left == None or right == None:
            return False
        if left.val == right.val:
            return self.cmpSubtree(left.left,right.right) and self.cmpSubtree(left.right,right.left)
        else:
            return False
    

    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.cmpSubtree(root.left,root.right)