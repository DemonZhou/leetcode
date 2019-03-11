# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def verticalOrder(self, root: TreeNode) -> 'List[List[int]]':
        cols = collections.defaultdict(list)
        q = [(root,0)]
        for n,i in q:
            if n:
                cols[i].append(n.val)
                q += (n.left,i - 1) , (n.right,i + 1)
        return [ cols[i] for i in sorted(cols)]