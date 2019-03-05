# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findMax(self,nums:'List[int]') :
        max_val = max(nums)
        max_index = nums.index(max_val)
        return max_val,max_index
    
    def constructLeftTree(self,nums:'List[int]',root:TreeNode) :
        if len(nums) == 0:
            return None
        max_val, max_index = self.findMax(nums)
        leftnode = TreeNode(max_val)
        root.left = leftnode
        self.constructLeftTree(nums[:max_index],leftnode)
        self.constructRightTree(nums[max_index + 1:],leftnode)


    def constructRightTree(self,nums:'List[int]',root:TreeNode) -> TreeNode:
        if len(nums) == 0:
            return None
        max_val, max_index = self.findMax(nums)
        rightnode = TreeNode(max_val)
        root.right = rightnode
        self.constructLeftTree(nums[:max_index],rightnode)
        self.constructRightTree(nums[max_index + 1:],rightnode)

    def constructMaximumBinaryTree(self, nums: 'List[int]') -> TreeNode:
        max_val,max_index = self.findMax(nums)
        root = TreeNode(max_val)
        self.constructLeftTree(nums[:max_index],root)
        self.constructRightTree(nums[max_index+1:],root)
        return root
        