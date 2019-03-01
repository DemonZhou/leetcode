import sys
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def closestValue(self, root: TreeNode, target: float) -> int:
        dif = sys.maxsize
        res = None
        while root:
            if dif > abs(root.val - target):
                dif = abs(root.val - target)
                res = root.val
            if target < root.val:
                root = root.left
            elif target >= root.val:
                root = root.right
        return res