# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode,lo = float('-inf'),hi = float('inf')) -> bool:
        if root == None:
            return True
        if root.val >= hi or root.val <= lo:
            return False
        return self.isValidBST(root.left,lo,min(hi,root.val)) and self.isValidBST(root.right,max(lo,root.val),hi)
        
        