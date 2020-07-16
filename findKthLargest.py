class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def quicksort(i, j, n):
            pivot = nums[j]
            storeindex = i
            for x in range(i,j):
                if nums[x] <= pivot:
                    #swap
                    nums[x] , nums[storeindex] = nums[storeindex], nums[x]
                    storeindex += 1
            nums[storeindex], nums[j] = nums[j] ,nums[storeindex]
            
            if j - storeindex + 1 == n :
                return nums[storeindex]
            if j - storeindex + 1 > n:
                return quicksort(storeindex + 1, j , n)
            else:
                return quicksort(i , storeindex - 1, n - (j - storeindex + 1))

        res = quicksort(0, len(nums) - 1,k)
        return res

Sol = Solution()
print(Sol.findKthLargest( [3,2,3,1,2,4,5,5,6], 4))
            