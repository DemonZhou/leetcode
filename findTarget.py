# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        Set = set()
        return self.dfs(root,Set,k)

    def dfs(self,root:TreeNode,Set,k:int) ->bool:
        if root == None:
            return False
        if k - root.val in Set:
            return True
        Set.add(root.val)
        return self.dfs(root.left,Set,k) or self.dfs(root.right,Set,k)
        