# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def robEx(node):
            if not node:
                return [0, 0]
            dp = [0 , 0]

            left = robEx(node.left)
            right = robEx(node.right)

            dp[0] = max(left[1],left[0]) + max(right[0], right[1])
            dp[1] = left[0] + right[0] + node.val

            return dp
        res = robEx(root)
        return max(res[0], res[1])

