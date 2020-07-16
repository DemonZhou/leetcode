class Solution(object):
    def __init__(self):
        self.ans = []
    
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        output = [[]]
        
        for num in nums:
            output += [curr + [num] for curr in output]
        
        return output
