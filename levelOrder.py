# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> 'List[List[int]]':
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