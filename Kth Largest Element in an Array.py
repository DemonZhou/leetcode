'''

https://leetcode.com/explore/interview/card/google/59/array-and-strings/361/

'''
class Solution(object):

    def quickSelect(self, nums, lo , hi, k):

        pivot = lo
        l = lo + 1
        r = hi
        
        while l <= r:
            while l <= r and nums[l] >= nums[pivot]:
                l += 1
            while l <= r and nums[r] <= nums[pivot]:
                r -= 1
            if l <= r :
                nums[l], nums[r] = nums[r] , nums[l]
                l += 1
                r -= 1
        nums[pivot], nums[r] = nums[r] , nums[pivot]
        if r == k - 1:
            return nums[r]
        elif r > k - 1:
            return self.quickSelect(nums,lo,r - 1,k)
        elif r < k - 1:
            return self.quickSelect(nums,r + 1 , hi,k)
        
            


    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        return self.quickSelect(nums,0,len(nums) - 1,k)
print(Solution().findKthLargest([3,2,1,5,6,4],2))