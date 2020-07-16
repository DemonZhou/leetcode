# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        index = { element : i for i,element in enumerate(inorder)}

        def  buildTreeEx(preorder_left, preorder_right,inorder_left,inorder_right):
            
            if preorder_left > preorder_right:
                return None

            preorder_root = preorder_left

            root = TreeNode(preorder[preorder_root])

            inorder_root = index[preorder[preorder_root]]

            size_left = inorder_root - inorder_left
            size_right = inorder_right - inorder_root

            root.left = buildTreeEx(preorder_root + 1, preorder_left + size_left , inorder_left, inorder_root - 1)
            root.right = buildTreeEx(preorder_root + size_left + 1, preorder_root + size_left + size_right, inorder_root + 1, inorder_root + size_right)

            return root

        N = len(preorder)

        return buildTreeEx(0, N - 1, 0 , N - 1)