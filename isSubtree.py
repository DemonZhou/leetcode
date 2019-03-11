# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False
        if self.cmpTree(s,t):
            return True
        return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
    
    def cmpTree(self, root: TreeNode, t:TreeNode)-> bool:
        if root == None and t != None:
            return False
        if root != None and t == None:
            return False
        if root == None and t == None:
            return True
        return root.val == t.val and self.cmpTree(root.left,t.left) and self.cmpTree(root.right,t.right)
        