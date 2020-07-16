# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Union(object):
    def __init__(self):
        self.parent = {}
        self.level = {}

    def add(self, root, level):
        if not root:
            return
        if root in self.parent:
            return
        self.parent[root] = root
        self.level[root] = level

    def union(self,root,child):
        if not root or not child:
            return
        self.parent[child] = root
        
    
    def find(self,child):
        if child not in self.parent:
            return None
        return self.parent[child] , self.level[child]

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if not root:
            return None
        
        if p == q:
            return p

        unionSet = Union()

        def PreOrder(node ,level):
            if not node:
                return 
            unionSet.add(node,level)
            unionSet.add(node.left, level + 1)
            unionSet.add(node.right, level + 1)

            unionSet.union(node, node.left)
            unionSet.union(node, node.right)

            PreOrder(node.left , level + 1)
            PreOrder(node.right , level + 1)
        
        PreOrder(root, 0)

        p_p , level_p = unionSet.find(p)
        p_q , level_q = unionSet.find(q)

        if level_p > level_q:
            for _ in range(level_p - level_q):
                p , t = unionSet.find(p)
        elif level_q < level_p:
            for _ in range(level_q - level_p):
                q , t = unionSet.find(q)
        
        while p != q:
            p , t = unionSet.find(p)
            q , t = unionSet.find(q)

        return p
            