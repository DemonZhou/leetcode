# Definition for a binary tree node.
import sys
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        diff = sys.maxsize
        res = None
        while root:
            if root.val <= p.val:
                root = root.right
            elif root.val > p.val and diff > root.val - p.val: 
                diff = root.val - p.val
                res = root
                root = root.left
            
            
        return res
                 
                