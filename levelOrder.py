# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root
            return []
        res = []

        quene = []
        level = 1

        quene.append(root)

        while len(quene) > 0:
            level = len(quene)
            res.append([])
            for i in range(level):
                node = quene.pop(0)
                res[-1].append(node.val)
                if node.left: quene.append(node.left)
                if node.right: quene.append(node.right)
        return res
            
