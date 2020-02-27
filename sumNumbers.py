# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return self.sumSubtree(root,0)
    def sumSubtree(self,root: TreeNode,currsum:int) ->int:
        if root == None:
            return 0
        currsum = currsum * 10 + root.val
        if root.left == None and root.right == None:
            return currsum
        return self.sumSubtree(root.left,currsum) + self.sumSubtree(root.right,currsum)
        