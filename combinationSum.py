class Solution(object):
    def __init__(self):
        self.res = []
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        if not candidates:
            return []

        candidates.sort()

        N = len(candidates)

        def search(i, k, path):
            if i >= N:
                return
            
            pivot = candidates[i]
            if pivot == k:
                path.append(pivot)
                if path not in self.res:
                    self.res.append(path)
                return
            elif pivot > k:
                return
            elif pivot < k:
                search(i , k - pivot, path + [pivot])
                search(i + 1, k - pivot, path + [pivot])
                search(i + 1, k, path)
            
        search(0 , target , [])
        return self.res
print(Solution().combinationSum( [2,3,5],8))

