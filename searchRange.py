class Solution(object):
    def __init__(self):
        self.left = -1
        self.right = -1
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        N = len(nums)

        def search(start,end):
            if start > end:
                return

            mid = (start + end) // 2

            if nums[mid] < target:
                search(mid + 1,end)
            elif  nums[mid] > target:
                search(start, mid - 1)
            else:
                self.right = max(self.right , mid)
                if self.left >= 0:
                    self.left = min(self.left , mid)
                else:
                    self.left = mid
                search(mid + 1,end)
                search(start, mid - 1)
        
        search(0,N - 1)
        
        return [self.left, self.right]