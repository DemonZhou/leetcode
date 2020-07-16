class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ans = set()
        self.findChar(digits,0,"",ans)
        return list(ans)

    def findChar(self, digits,start,path, ans):
        dic = {
            '2' : ["a", "b", "c"],
            '3' : ["d", "e", "f"],
            '4' : ["g", "h", "i"],
            '5' : ["j", "k", "l"],
            '6' : ["m", "n", "o"],
            '7' : ["p", "q" ,"r","s"],
            '8' : ["t", "u" , "v"],
            '9' : ["w", "x" , "y" , "z"]

        }
        if start < len(digits) - 1:
            for c in dic[digits[start]]:
                self.findChar(digits,start + 1,path + c, ans)
        elif start == len(digits) - 1:
            for c in dic[digits[start]]:
                ans.add(path + c)