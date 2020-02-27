'''
https://leetcode.com/explore/interview/card/google/59/array-and-strings/3057/

'''

class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """

        l =list(S)
        
        for i,s,t in sorted(zip(indexes,sources,targets),reverse=True):
            if S[i:i + len(s)] == s:
                S = S[:i] + t + S[i+len(s):]
        return "".join(S)

        
print(Solution().findReplaceString("vmokgggqzp",[3,5,1],["kg","ggq","mo"],["s","so","bfr"]))
                


            
