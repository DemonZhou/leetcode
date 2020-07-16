# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x    
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.hashmap = {}
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def dfs(node,summlist):
            if not node:
                return 0
            
            summlist = [node.val + num for num in summlist] + [node.val]
            return summlist.count(sum) + dfs(node.left,summlist) + dfs(node.right,summlist)
        return dfs(root,[])
       