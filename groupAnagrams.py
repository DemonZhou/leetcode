class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for s in strs:
            if tuple(sorted(s)) not in dic:
                dic[tuple(sorted(s))] = []
            dic[tuple(sorted(s))].append(s)
        
        return dic.values()
    
print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))