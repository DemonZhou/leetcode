# Definition for a binary tree node.
<<<<<<< HEAD
class TreeNode(object):
=======
class TreeNode:
>>>>>>> 4c9a2d276b1ddf2472647468ab660e7d695451cc
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

<<<<<<< HEAD
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
            
=======
class Solution:
    def levelOrder(self, root: TreeNode) -> 'List[List[int]]':
        if not root:
            return []
        res = []
        q = [root]
        while q:
            next_q = []
            res_child = []
            for n in q:
                res_child.append(n.val)
                if n.left:
                    next_q.append(n.left)
                if n.right:
                    next_q.append(n.right)
            res.append(res_child)
            q = next_q
        return res
>>>>>>> 4c9a2d276b1ddf2472647468ab660e7d695451cc
